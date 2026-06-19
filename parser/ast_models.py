from dataclasses import dataclass


@dataclass
class FunctionNode:

    name: str


@dataclass
class ClassNode:

    name: str


@dataclass
class ImportNode:

    name: str