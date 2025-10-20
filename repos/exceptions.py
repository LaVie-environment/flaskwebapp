#!/usr/bin/env python3

"""
Generic exception hierarchy - reduces GitHub-specific coupling
"""
class RepositoryException(Exception):
    """Base exception for repository operations"""
    pass


class RateLimitException(RepositoryException):
    """Raised when rate limit is hit"""
    def __init__(self):
        super().__init__("Rate limit reached. Please wait a minute and try again.")


class DataSourceException(RepositoryException):
    """Generic data source error"""
    def __init__(self, status_code):
        super().__init__(f"HTTP Status Code was: {status_code}.")