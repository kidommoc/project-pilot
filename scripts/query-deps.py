#!/usr/bin/env python3
"""
Query the dependency graph.

Usage:
    python query-deps.py --graph <graph.json> --calls <module>   # Who calls X?
    python query-deps.py --graph <graph.json> --depends <module> # What does X depend on?
    python query-deps.py --graph <graph.json> --circular         # Show circular dependencies
"""

import argparse
import json
from pathlib import Path
from typing import Dict, List, Set


def load_graph(graph_path: Path) -> Dict:
    """Load dependency graph from JSON file."""
    with open(graph_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def find_callers(graph: Dict, target: str) -> List[Dict]:
    """Find all modules that call the target module."""
    callers = []
    
    for rel in graph.get("call_relationships", []):
        callee = rel.get("callee", "")
        if target in callee or callee.startswith(f"{target}."):
            callers.append(rel)
    
    return callers


def find_dependencies(graph: Dict, target: str) -> List[Dict]:
    """Find all modules that the target depends on."""
    deps = []
    
    for dep in graph.get("import_dependencies", []):
        if dep["from"] == target:
            deps.append(dep)
    
    return deps


def find_dependents(graph: Dict, target: str) -> List[Dict]:
    """Find all modules that depend on the target."""
    dependents = []
    
    for dep in graph.get("import_dependencies", []):
        if dep["to"] == target:
            dependents.append(dep)
    
    return dependents


def show_circular(graph: Dict) -> List[List[str]]:
    """Show circular dependencies."""
    return graph.get("circular_deps", [])


def format_callers(callers: List[Dict]) -> str:
    """Format callers for display."""
    if not callers:
        return "  No callers found"
    
    lines = ["  Callers:"]
    for call in callers:
        lines.append(f"    - {call['caller']} → {call['callee']}")
    return "\n".join(lines)


def format_dependencies(deps: List[Dict]) -> str:
    """Format dependencies for display."""
    if not deps:
        return "  No dependencies found"
    
    lines = ["  Depends on:"]
    for dep in deps:
        lines.append(f"    - {dep['from']} → {dep['to']} ({dep['type']})")
    return "\n".join(lines)


def format_dependents(deps: List[Dict]) -> str:
    """Format dependents for display."""
    if not deps:
        return "  No dependents found"
    
    lines = ["  Depended on by:"]
    for dep in deps:
        lines.append(f"    - {dep['to']} → {dep['from']}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description='Query the dependency graph')
    parser.add_argument('--graph', required=True, help='Dependency graph JSON file')
    parser.add_argument('--calls', help='Find callers of a module')
    parser.add_argument('--depends', help='Find dependencies of a module')
    parser.add_argument('--dependents', help='Find modules that depend on a module')
    parser.add_argument('--circular', action='store_true', help='Show circular dependencies')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    graph_path = Path(args.graph)
    if not graph_path.exists():
        print(f"Error: Graph file {graph_path} does not exist")
        print("Run extract-dependencies.py first to generate the graph.")
        return 1
    
    graph = load_graph(graph_path)
    
    results = {}
    
    if args.calls:
        callers = find_callers(graph, args.calls)
        dependents = find_dependents(graph, args.calls)
        results["module"] = args.calls
        results["callers"] = callers
        results["depended_on_by"] = dependents
        
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print(f"\nModule: {args.calls}\n")
            print(format_callers(callers))
            print()
            print(format_dependents(dependents))
    
    if args.depends:
        deps = find_dependencies(graph, args.depends)
        results["module"] = args.depends
        results["dependencies"] = deps
        
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print(f"\nModule: {args.depends}\n")
            print(format_dependencies(deps))
    
    if args.circular:
        circular = show_circular(graph)
        results["circular_deps"] = circular
        
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            if circular:
                print("\nCircular dependencies detected:\n")
                for cycle in circular:
                    print(f"  {' → '.join(cycle)}")
            else:
                print("\nNo circular dependencies detected. ✅")
    
    if not (args.calls or args.depends or args.dependents or args.circular):
        # Show summary
        if args.json:
            print(json.dumps({
                "modules": len(graph.get("modules", {})),
                "import_deps": len(graph.get("import_dependencies", [])),
                "call_rels": len(graph.get("call_relationships", [])),
                "circular": len(graph.get("circular_deps", []))
            }, indent=2))
        else:
            print("\nDependency Graph Summary\n")
            print(f"  Modules: {len(graph.get('modules', {}))}")
            print(f"  Import dependencies: {len(graph.get('import_dependencies', []))}")
            print(f"  Call relationships: {len(graph.get('call_relationships', []))}")
            print(f"  Circular dependencies: {len(graph.get('circular_deps', []))}")
            print("\nUsage:")
            print("  --calls <module>     Find who calls this module")
            print("  --depends <module>   Find what this module depends on")
            print("  --dependents <module> Find what depends on this module")
            print("  --circular           Show circular dependencies")
    
    return 0


if __name__ == '__main__':
    exit(main())
