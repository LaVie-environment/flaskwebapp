#!/usr/bin/env python3

"""
Configuration management - separates settings from code
"""
class Config:
    """Base configuration"""
    AVAILABLE_LANGUAGES = ["Python", "JavaScript", "Ruby", "Java"]
    MIN_STARS = 40000
    SORT_BY = "stars"
    ORDER = "desc"