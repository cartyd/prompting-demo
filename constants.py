"""
Shared constants for the AI Prompt Framework Demo application.

This module contains constants used across multiple modules to avoid
circular dependencies.
"""


# Framework name constants to avoid magic strings
FRAMEWORK_CHAIN_OF_THOUGHT = "Chain of Thought"
FRAMEWORK_TREE_OF_THOUGHT = "Tree of Thought"
FRAMEWORK_SELF_CONSISTENCY = "Self-Consistency"
FRAMEWORK_FEW_SHOT = "Few-Shot"
FRAMEWORK_REFLECTION_REVISION = "Reflection & Revision"

# All available frameworks in order
ALL_FRAMEWORKS = [
    FRAMEWORK_CHAIN_OF_THOUGHT,
    FRAMEWORK_TREE_OF_THOUGHT,
    FRAMEWORK_SELF_CONSISTENCY,
    FRAMEWORK_FEW_SHOT,
    FRAMEWORK_REFLECTION_REVISION
]


# Available OpenAI models for selection in online mode
AVAILABLE_MODELS = [
    "gpt-5",
    "gpt-5-mini",
    "gpt-4o",
    "gpt-4o-mini",
    "gpt-4-turbo",
    "gpt-3.5-turbo"
]

# Interval for checking textarea resize in milliseconds
TEXTAREA_RESIZE_INTERVAL_MS = 100
