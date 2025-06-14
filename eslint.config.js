import js from '@eslint/js';
import markdown from '@eslint/markdown';
import tseslint from 'typescript-eslint';

export default [
  // Base JavaScript recommended rules for .js files
  {
    ...js.configs.recommended,
    files: ['**/*.js'],
  },
  
  // TypeScript rules for .ts files
  ...tseslint.configs.recommended.map(config => ({
    ...config,
    files: ['**/*.ts'],
    rules: {
      ...config.rules,
      '@typescript-eslint/no-empty-object-type': 'off',
    }
  })),
  
  // Markdown processor configuration
  ...markdown.configs.recommended.map(config => ({
    ...config,
    rules: {
      ...config.rules,
      // Disable rules that don't work well with your documentation style
      'markdown/no-missing-label-refs': 'off', // Allow [placeholder] syntax
      'markdown/no-multiple-h1': 'warn', // Warn instead of error
      'markdown/fenced-code-language': 'warn', // Warn for missing language
      // Keep these important ones
      'markdown/no-empty-links': 'error',
      'markdown/no-html': 'off', // Allow HTML in markdown
    }
  })),
  
  // Ignore patterns
  {
    ignores: [
      '**/node_modules/**',
      'node_modules/**',
      '.yarn/**',
      'dist/**',
      '*.log',
      '**/*.log',
      'sectors/*/sector-data-backup/**', // Ignore backup directories
      '.git/**',
      '.pnp.*',
      '.yarnrc.yml',
      'yarn.lock',
      '.obsidian/**', // Ignore all Obsidian files
    ]
  }
];