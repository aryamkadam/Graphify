# Architecture Summary

## Repository Flow

Repository
↓
Scanner Layer
↓
Parser Layer
↓
Symbol Index
↓
Knowledge Graph
↓
Risk Engine
↓
Repository Brain
↓
AI Handover Pack

## CLI Layer

Purpose: Entry point of Graphify. Handles user execution and startup.

Files:
- cli\main.py

## GRAPH_BUILDER Layer

Purpose: Builds repository intelligence including knowledge graphs, dependency analysis, risk analysis, repository brain and AI handover packs.

Files:
- graph_builder\architecture_layers.py
- graph_builder\builder.py
- graph_builder\context_pack.py
- graph_builder\critical_path.py
- graph_builder\exporter.py
- graph_builder\impact_analysis.py
- graph_builder\module_dependency_map.py
- graph_builder\query_engine.py
- graph_builder\repository_flow.py
- graph_builder\repository_graph.py
- graph_builder\repository_summary.py
- graph_builder\symbol_index.py

## PARSER Layer

Purpose: Extracts symbols, classes, functions and imports from source code.

Files:
- parser\ast_models.py
- parser\python_parser.py

## SCANNER Layer

Purpose: Discovers repository files and performs file analysis.

Files:
- scanner\classifier.py
- scanner\duplicates.py
- scanner\hash_utils.py
- scanner\ignore.py
- scanner\report.py
- scanner\scanner.py
