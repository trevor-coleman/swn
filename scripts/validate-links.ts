#!/usr/bin/env node
import { glob } from 'glob';
import { readFile } from 'fs/promises';
import { resolve, dirname } from 'path';
import { existsSync } from 'fs';

interface LinkResult {
  file: string;
  line: number;
  link: string;
  type: 'internal' | 'external' | 'anchor';
  valid: boolean;
  error?: string;
}

// Regex to match markdown links
const LINK_REGEX = /\[([^\]]+)\]\(([^)]+)\)/g;
const ANCHOR_REGEX = /#[^)]+$/;

async function validateMarkdownLinks(rootDir: string): Promise<LinkResult[]> {
  const results: LinkResult[] = [];
  
  // Find all markdown files
  const files = await glob('**/*.md', { 
    cwd: rootDir,
    ignore: ['node_modules/**', '.yarn/**', '*.log']
  });

  for (const file of files) {
    const fullPath = resolve(rootDir, file);
    const content = await readFile(fullPath, 'utf-8');
    const lines = content.split('\n');
    
    let lineNumber = 0;
    for (const line of lines) {
      lineNumber++;
      let match;
      
      while ((match = LINK_REGEX.exec(line)) !== null) {
        const [, , linkPath] = match;
        
        // Skip external links
        if (linkPath.startsWith('http://') || linkPath.startsWith('https://')) {
          results.push({
            file,
            line: lineNumber,
            link: linkPath,
            type: 'external',
            valid: true // We don't validate external links
          });
          continue;
        }
        
        // Handle anchors
        if (linkPath.startsWith('#')) {
          results.push({
            file,
            line: lineNumber,
            link: linkPath,
            type: 'anchor',
            valid: true // TODO: Could validate anchors exist in file
          });
          continue;
        }
        
        // Internal link - resolve relative to current file
        const linkDir = dirname(fullPath);
        const cleanPath = linkPath.replace(ANCHOR_REGEX, ''); // Remove anchor if present
        const absoluteLinkPath = resolve(linkDir, cleanPath);
        
        const exists = existsSync(absoluteLinkPath);
        results.push({
          file,
          line: lineNumber,
          link: linkPath,
          type: 'internal',
          valid: exists,
          error: exists ? undefined : `File not found: ${absoluteLinkPath}`
        });
      }
    }
  }
  
  return results;
}

// Main function
async function main() {
  const rootDir = resolve(process.cwd());
  console.log(`Validating markdown links in: ${rootDir}\n`);
  
  try {
    const results = await validateMarkdownLinks(rootDir);
    
    // Group results
    const brokenLinks = results.filter(r => !r.valid);
    const validLinks = results.filter(r => r.valid);
    
    console.log(`Total links found: ${results.length}`);
    console.log(`Valid links: ${validLinks.length}`);
    console.log(`Broken links: ${brokenLinks.length}\n`);
    
    if (brokenLinks.length > 0) {
      console.log('Broken links found:\n');
      for (const link of brokenLinks) {
        console.log(`${link.file}:${link.line} - [${link.link}]`);
        if (link.error) {
          console.log(`  Error: ${link.error}`);
        }
      }
      process.exit(1);
    } else {
      console.log('✅ All links are valid!');
    }
  } catch (error) {
    console.error('Error validating links:', error);
    process.exit(1);
  }
}

// Run if called directly
if (require.main === module) {
  main();
}

export { validateMarkdownLinks };