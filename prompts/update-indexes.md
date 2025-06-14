# Update Project Indexes and Documentation

Please review the project structure and update all indexes and documentation to reflect the current state. Follow this three-stage process:

## 1) ANALYZE
First, thoroughly explore the entire project structure, paying special attention to:
- The sectors/ directory and all its subdirectories
- The hierarchical organization of systems, planets, and locations
- Character and faction organization
- Session files and their naming conventions
- Plot threads and active tensions
- Game mechanics and reference materials

List all major components found and note any discrepancies between documentation and actual structure.

## 2) PLAN
Create a detailed plan for which files need updating based on your analysis. Consider:
- MASTER-INDEX.md - main project index
- Sector-specific README files
- Navigation references and cross-links
- System coordinate indexes
- NPC and faction indexes
- Timeline and revelation indexes
- Any documentation that references file paths

For each file that needs updating, identify:
- What specific changes are needed
- Which cross-references need fixing
- Whether bulk path updates can be done with sed

## 3) EXECUTE
Systematically update each file identified in your plan:
- Use sed for bulk path updates where appropriate (e.g., updating all references from old path structure to new)
- Ensure all cross-references use correct relative paths
- Verify that navigation links work correctly
- Update any outdated information about project structure
- Maintain consistency in formatting and organization

Remember to use sed for efficient bulk updates of paths, for example:
```bash
sed -i 's|old/path/pattern|new/path/pattern|g' filename.md
```

Be thorough but efficient. The goal is to ensure all documentation accurately reflects the current project structure so users can navigate the repository effectively.