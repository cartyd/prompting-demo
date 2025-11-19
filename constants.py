"""
Shared constants for the AI Prompt Framework Demo application.

This module contains constants used across multiple modules to avoid
circular dependencies.
"""


class Framework:
    """Framework name constants to avoid magic strings."""
    CHAIN_OF_THOUGHT = "Chain of Thought"
    TREE_OF_THOUGHT = "Tree of Thought"
    SELF_CONSISTENCY = "Self-Consistency"
    FEW_SHOT = "Few-Shot"
    REFLECTION_REVISION = "Reflection & Revision"
    
    @classmethod
    def all(cls) -> list:
        """Return all framework names as a list."""
        return [
            cls.CHAIN_OF_THOUGHT,
            cls.TREE_OF_THOUGHT,
            cls.SELF_CONSISTENCY,
            cls.FEW_SHOT,
            cls.REFLECTION_REVISION
        ]


# Interval for checking textarea resize in milliseconds
TEXTAREA_RESIZE_INTERVAL_MS = 100
