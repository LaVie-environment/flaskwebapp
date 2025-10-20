#!/usr/bin/env python3

"""
Abstract repository service - defines the contract
reduces coupling by allowing multiple implementations
"""
from abc import ABC, abstractmethod


class RepositoryService(ABC):
    """Abstract base class for repository data sources"""
    
    @abstractmethod
    def get_repositories(self, languages, min_stars=40000):
        """Get repositories by language and minimum stars"""
        pass