#!/usr/bin/env python3
"""
Extract documentation dependencies from Markdown files.

Usage:
    python extract-doc-deps.py --src <source_dir> --output <output.json>

Output:
    JSON file with document reference relationships.
"""

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Set


def extract_markdown_references(file_path: Path, base_dir: Path) -> Dict:
    """Extract references from a Markdown file."""
    refs = {
        "file": str(file_path.relative_to(base_dir)),
        "references": [],
        "referenced_by": []
    }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern 1: [text](path) - Standard Markdown links
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        
        for match in re.finditer(link_pattern, content):
            link_text = match.group(1)
            link_path = match.group(2)
            
            # Skip external links
            if link_path.startswith(('http://', 'https://', 'mailto:')):
                continue
            
            # Remove anchor (#section)
            link_path = link_path.split('#')[0]
            
            # Resolve relative path
            if link_path.startswith('./'):
                link_path = link_path[2:]
            elif link_path.startswith('../'):
                # Resolve parent directory
                parent = file_path.parent
                while link_path.startswith('../'):
                    parent = parent.parent
                    link_path = link_path[3:]
                link_path = str(parent / link_path)
            
            # Normalize path
            link_path = link_path.lstrip('/')
            
            # Check if it's a Markdown file
            if link_path.endswith('.md'):
                refs["references"].append({
                    "target": link_path,
                    "type": "markdown_link",
                    "context": link_text[:50]
                })
        
        # Pattern 2: [[Wiki Link]] - Obsidian/Zettelkasten style
        wiki_pattern = r'\[\[([^\]]+)\]\]'
        
        for match in re.finditer(wiki_pattern, content):
            wiki_link = match.group(1)
            refs["references"].append({
                "target": wiki_link + ".md",
                "type": "wiki_link",
                "context": wiki_link
            })
        
        # Pattern 3: See also / Related sections
        see_also_pattern = r'(?:See also|Related|References)[:\s]*([^\n]+)'
        
        for match in re.finditer(see_also_pattern, content, re.IGNORECASE):
            see_also_text = match.group(1)
            # Extract file references
            file_refs = re.findall(r'[\w-]+\.md', see_also_text)
            for ref in file_refs:
                refs["references"].append({
                    "target": ref,
                    "type": "see_also",
                    "context": see_also_text[:50]
                })
    
    except Exception as e:
        print(f"Warning: Could not parse {file_path}: {e}")
    
    return refs


def build_dependency_graph(docs_dir: Path) -> Dict:
    """Build complete dependency graph."""
    graph = {
        "documents": {},
        "references": [],
        "orphaned": [],
        "highly_referenced": []
    }
    
    # Collect all Markdown files
    md_files = list(docs_dir.rglob('*.md'))
    
    # Extract references from each file
    for md_file in md_files:
        if 'node_modules' in str(md_file):
            continue
        
        refs = extract_markdown_references(md_file, docs_dir)
        graph["documents"][refs["file"]] = refs
        
        # Add to reference list
        for ref in refs["references"]:
            graph["references"].append({
                "from": refs["file"],
                "to": ref["target"],
                "type": ref["type"]
            })
    
    # Build reverse index (referenced_by)
    reverse_index: Dict[str, List[str]] = {}
    for ref in graph["references"]:
        target = ref["to"]
        source = ref["from"]
        if target not in reverse_index:
            reverse_index[target] = []
        reverse_index[target].append(source)
    
    # Update documents with referenced_by
    for file_path, refs in graph["documents"].items():
        refs["referenced_by"] = reverse_index.get(file_path, [])
    
    # Find orphaned documents (not referenced by anything)
    for file_path, refs in graph["documents"].items():
        if not refs["referenced_by"] and file_path not in ['README.md']:
            graph["orphaned"].append(file_path)
    
    # Find highly referenced documents
    for file_path, refs in graph["documents"].items():
        if len(refs["referenced_by"]) >= 3:
            graph["highly_referenced"].append({
                "file": file_path,
                "referenced_by_count": len(refs["referenced_by"])
            })
    
    # Sort by reference count
    graph["highly_referenced"].sort(key=lambda x: x["referenced_by_count"], reverse=True)
    
    return graph


def find_impact_target(graph: Dict, target_file: str) -> List[str]:
    """Find all files that reference the target file."""
    for file_path, refs in graph["documents"].items():
        if file_path == target_file:
            return refs["referenced_by"]
    return []


def main():
    parser = argparse.ArgumentParser(description='Extract documentation dependencies')
    parser.add_argument('--src', required=True, help='Source directory to scan')
    parser.add_argument('--output', required=True, help='Output JSON file path')
    parser.add_argument('--impact', help='Find files impacted by changes to a specific file')
    parser.add_argument('--json', action='store_true', help='Output as JSON (for --impact)')
    
    args = parser.parse_args()
    
    docs_dir = Path(args.src)
    if not docs_dir.exists():
        print(f"Error: Source directory {docs_dir} does not exist")
        return 1
    
    print(f"Scanning {docs_dir} for documentation dependencies...")
    graph = build_dependency_graph(docs_dir)
    
    # Write full graph
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)
    
    print(f"Documentation graph written to {output_path}")
    print(f"  Documents: {len(graph['documents'])}")
    print(f"  References: {len(graph['references'])}")
    print(f"  Orphaned: {len(graph['orphaned'])}")
    print(f"  Highly referenced: {len(graph['highly_referenced'])}")
    
    # Impact analysis
    if args.impact:
        impacted = find_impact_target(graph, args.impact)
        
        if args.json:
            print(json.dumps({
                "target": args.impact,
                "impacted_files": impacted,
                "count": len(impacted)
            }, indent=2))
        else:
            print(f"\nFiles impacted by changes to {args.impact}:")
            if impacted:
                for f in impacted:
                    print(f"  - {f}")
            else:
                print("  No files reference this document")
    
    return 0


if __name__ == '__main__':
    exit(main())
