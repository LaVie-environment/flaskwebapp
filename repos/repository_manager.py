#!/usr/bin/env python3

"""
Repository manager - orchestrates operations
Decouples Flask from specific service implementations

"""

from repos.services import RepositoryService


class RepositoryManager:
    """Manages repository operations using dependency injection"""
    
    def __init__(self, service: RepositoryService, config):
        """
        Initialize the manager with a service and configuration.
        
        Args:
            service: A RepositoryService implementation (e.g., GitHubService)
            config: Configuration object with settings
        """
        self.service = service
        self.config = config
    
    def search(self, languages=None):
        """
        Search for repositories.
        
        Args:
            languages: List of programming languages to search for.
                      If None, uses all available languages from config.
        
        Returns:
            List of Repository objects
        """
        if languages is None:
            languages = self.config.AVAILABLE_LANGUAGES
        
        return self.service.get_repositories(
            languages,
            min_stars=self.config.MIN_STARS,
            sort=self.config.SORT_BY,
            order=self.config.ORDER
        )
    
    def get_available_languages(self):
        """
        Get list of available languages from configuration.
        
        Returns:
            List of language strings
        """
        return self.config.AVAILABLE_LANGUAGES
