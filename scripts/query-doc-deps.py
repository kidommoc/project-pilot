#!/usr/bin/env python3
"""
Query the documentation dependency graph.

Usage:
    python query-doc-deps.py --graph <graph.json> --impact <file>    # What is impacted by X?
    python query-doc-deps.py --graph <graph.json> --refs <file>     # What does X reference?
    python query-doc-deps.py --graph <graph.json> --orphaned        # Show orphaned documents
    python query-doc-deps.py --graph <graph.json> --popular         # Show highly referenced docs
"""

import argparse
import json
from pathlib import Path
from typing import Dict, List


def load_graph(graph_path: Path) -> Dict:
    """Load documentation graph from JSON file."""
    with open(graph_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def find_impacted(graph: Dict, target: str) -> List[str]:
    """Find all files that reference the target file."""
    for file_path, refs in graph.get("documents", {}).items():
        if file_path == target:
            return refs.get("referenced_by", [])
    return []


def find_references(graph: Dict, target: str) -> List[Dict]:
    """Find all files that the target references."""
    refs = []
    for ref in graph.get("references", []):
        if ref["from"] == target:
            refs.append(ref)
    return refs


def show_orphaned(graph: Dict) -> List[str]:
    """Show orphaned documents."""
    return graph.get("orphaned", [])


def show_popular(graph: Dict) -> List[Dict]:
    """Show highly referenced documents."""
    return graph.get("highly_referenced", [])


def main():
    parser = argparse.ArgumentParser(description='Query the documentation dependency graph')
    parser.add_argument('--graph', required=True, help='Documentation graph JSON file')
    parser.add_argument('--impact', help='Find files impacted by changes to a file')
    parser.add_argument('--refs', help='Find files referenced by a file')
    parser.add_argument('--orphaned', action='store_true', help='Show orphaned documents')
    parser.add_argument('--popular', action='store_true', help='Show highly referenced docs')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    graph_path = Path(args.graph)
    if not graph_path.exists():
        print(f"Error: Graph file {graph_path} does not exist")
        print("Run extract-doc-deps.py first to generate the graph.")
        return 1
    
    graph = load_graph(graph_path)
    
    results = {}
    
    if args.impact:
        impacted = find_impacted(graph, args.impact)
        results["target"] = args.impact
        results["impacted_files"] = impacted
        results["count"] = len(impacted)
        
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print(f"\nFiles impacted by changes to {args.impact}:\n")
            if impacted:
                for f in impacted:
                    print(f"  - {f}")
                print(f"\nTotal: {len(impacted)} file(s) need update")
            else:
                print("  No files reference this document")
    
    if args.refs:
        refs = find_references(graph, args.refs)
        results["target"] = args.refs
        results["references"] = refs
        results["count"] = len(refs)
        
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print(f"\nFiles referenced by {args.refs}:\n")
            if refs:
                for ref in refs:
                    print(f"  - {ref['to']} ({ref['type']})")
                print(f"\nTotal: {len(refs)} reference(s)")
            else:
                print("  No references found")
    
    if args.orphaned:
        orphaned = show_orphaned(graph)
        results["orphaned"] = orphaned
        
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print("\nOrphaned documents (not referenced by anything):\n")
            if orphaned:
                for f in orphaned:
                    print(f"  - {f}")
                print(f"\nTotal: {len(orphaned)} orphaned file(s)")
            else:
                print("  No orphaned documents. ✅")
    
    if args.popular:
        popular = show_popular(graph)
        results["popular"] = popular
        
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print("\nHighly referenced documents (3+ references):\n")
            if popular:
                for doc in popular:
                    print(f"  - {doc['file']} ({doc['referenced_by_count']} references)")
            else:
                print("  No highly referenced documents")
    
    if not (args.impact or args.refs or args.orphaned or args.popular):
        # Show summary
        if args.json:
            print(json.dumps({
                "documents": len(graph.get("documents", {})),
                "references": len(graph.get("references", [])),
                "orphaned": len(graph.get("orphaned", [])),
                "popular": len(graph.get("highly_referenced", []))
            }, indent=2))
        else:
            print("\nDocumentation Graph Summary\n")
            print(f"  Documents: {len(graph.get('documents', {}))}")
            print(f"  References: {len(graph.get('references', []))}")
            print(f"  Orphaned: {len(graph.get('orphaned', []))}")
            print(f"  Highly referenced: {len(graph.get('highly_referenced', []))}")
            print("\nUsage:")
            print("  --impact <file>     Find files impacted by changes to a file")
            print("  --refs <file>       Find files referenced by a file")
            print("  --orphaned          Show orphaned documents")
            print("  --popular           Show highly referenced documents")
    
    return 0


if __name__ == '__main__':
    exit(main())
