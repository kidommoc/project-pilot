#!/usr/bin/env python3
"""
Extract module dependencies from source code.

Usage:
    python extract-dependencies.py --src <source_dir> --output <output.json>

Output:
    JSON file with module call relationships and import dependencies.
"""

import argparse
import json
import os
import re
from pathlib import Path
from typing import Dict, List, Set


def extract_python_imports(file_path: Path) -> Dict[str, List[str]]:
    """Extract import statements from a Python file."""
    imports = {"internal": [], "external": []}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Match: from X import Y / import X
        import_pattern = r'^(?:from\s+([\w.]+)\s+import|import\s+([\w.]+))'
        
        for line in content.split('\n'):
            line = line.strip()
            match = re.match(import_pattern, line)
            if match:
                module = match.group(1) or match.group(2)
                # Check if internal (starts with project root)
                if module and not module.startswith(('os', 'sys', 'json', 're', 'typing', 'pathlib')):
                    imports["internal"].append(module)
                elif module:
                    imports["external"].append(module)
    except Exception as e:
        print(f"Warning: Could not parse {file_path}: {e}")
    
    return imports


def extract_python_calls(file_path: Path) -> List[Dict]:
    """Extract function calls from a Python file."""
    calls = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Match: module.function() or self.function()
        call_pattern = r'([\w.]+)\.([\w_]+)\s*\('
        
        for match in re.finditer(call_pattern, content):
            module = match.group(1)
            function = match.group(2)
            
            # Skip common built-ins
            if module not in ('self', 'os', 'sys', 'json', 're', 'Path'):
                calls.append({
                    "caller": file_path.stem,
                    "module": module,
                    "function": function
                })
    except Exception as e:
        print(f"Warning: Could not parse {file_path}: {e}")
    
    return calls


def extract_typescript_imports(file_path: Path) -> Dict[str, List[str]]:
    """Extract import statements from a TypeScript file."""
    imports = {"internal": [], "external": []}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Match: import X from 'Y' or import { X } from 'Y'
        import_pattern = r'import\s+(?:\{[^}]+\}|\w+)\s+from\s+[\'"]([^\'"]+)[\'"]'
        
        for match in re.finditer(import_pattern, content):
            module = match.group(1)
            if module.startswith('.'):
                imports["internal"].append(module)
            else:
                imports["external"].append(module)
    except Exception as e:
        print(f"Warning: Could not parse {file_path}: {e}")
    
    return imports


def scan_directory(src_dir: Path) -> Dict:
    """Scan directory for dependencies."""
    graph = {
        "modules": {},
        "call_relationships": [],
        "import_dependencies": [],
        "circular_deps": []
    }
    
    # Scan Python files
    for py_file in src_dir.rglob('*.py'):
        if '__pycache__' in str(py_file):
            continue
        
        module_name = py_file.stem
        rel_path = str(py_file.relative_to(src_dir))
        
        imports = extract_python_imports(py_file)
        calls = extract_python_calls(py_file)
        
        graph["modules"][module_name] = {
            "path": rel_path,
            "language": "python",
            "imports": imports,
            "calls": calls
        }
        
        # Add to import dependencies
        for imp in imports["internal"]:
            graph["import_dependencies"].append({
                "from": module_name,
                "to": imp.split('.')[0],
                "type": "import"
            })
        
        # Add to call relationships
        for call in calls:
            graph["call_relationships"].append({
                "caller": f"{module_name}.{call['function']}()",
                "callee": f"{call['module']}.{call['function']}()"
            })
    
    # Scan TypeScript files
    for ts_file in src_dir.rglob('*.ts'):
        if 'node_modules' in str(ts_file):
            continue
        
        module_name = ts_file.stem
        rel_path = str(ts_file.relative_to(src_dir))
        
        imports = extract_typescript_imports(ts_file)
        
        graph["modules"][module_name] = {
            "path": rel_path,
            "language": "typescript",
            "imports": imports
        }
        
        for imp in imports["internal"]:
            graph["import_dependencies"].append({
                "from": module_name,
                "to": imp.replace('./', '').split('/')[0],
                "type": "import"
            })
    
    # Detect circular dependencies
    graph["circular_deps"] = detect_circular_deps(graph["import_dependencies"])
    
    return graph


def detect_circular_deps(deps: List[Dict]) -> List[List[str]]:
    """Detect circular dependencies."""
    circular = []
    
    # Build adjacency list
    adj: Dict[str, Set[str]] = {}
    for dep in deps:
        from_mod = dep["from"]
        to_mod = dep["to"]
        if from_mod not in adj:
            adj[from_mod] = set()
        adj[from_mod].add(to_mod)
    
    # DFS to detect cycles
    def dfs(node: str, path: List[str], visited: Set[str]) -> bool:
        if node in path:
            cycle_start = path.index(node)
            circular.append(path[cycle_start:] + [node])
            return True
        
        if node in visited:
            return False
        
        visited.add(node)
        path.append(node)
        
        for neighbor in adj.get(node, []):
            dfs(neighbor, path, visited)
        
        path.pop()
        return False
    
    visited: Set[str] = set()
    for node in adj.keys():
        if node not in visited:
            dfs(node, [], visited)
    
    return circular


def main():
    parser = argparse.ArgumentParser(description='Extract module dependencies from source code')
    parser.add_argument('--src', required=True, help='Source directory to scan')
    parser.add_argument('--output', required=True, help='Output JSON file path')
    
    args = parser.parse_args()
    
    src_dir = Path(args.src)
    if not src_dir.exists():
        print(f"Error: Source directory {src_dir} does not exist")
        return 1
    
    print(f"Scanning {src_dir} for dependencies...")
    graph = scan_directory(src_dir)
    
    # Write output
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)
    
    print(f"Dependency graph written to {output_path}")
    print(f"  Modules: {len(graph['modules'])}")
    print(f"  Import dependencies: {len(graph['import_dependencies'])}")
    print(f"  Call relationships: {len(graph['call_relationships'])}")
    print(f"  Circular dependencies: {len(graph['circular_deps'])}")
    
    return 0


if __name__ == '__main__':
    exit(main())
