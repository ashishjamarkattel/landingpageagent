from dataclasses import dataclass


@dataclass
class GeneratedContent:
    """Data class to hold generated content"""
    title: str
    content: str
    component_type: str
    file_path: str