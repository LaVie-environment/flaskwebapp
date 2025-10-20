#!/usr/bin/env python3

"""
GitHub-specific implementation - changes here don't affect the rest
"""
import requests
from repos.services.repository_service import RepositoryService
from repos.models import Repository
from repos.exceptions import RateLimitException, DataSourceException


class GitHubService(RepositoryService):
    """GitHub API implementation"""
    
    def __init__(self, api_url="https://api.github.com/search/repositories"):
        self.api_url = api_url
    
    def get_repositories(self, languages, min_stars=40000, 
                        sort="stars", order="desc"):
        """Fetch repositories from GitHub API"""
        query = self._build_query(languages, min_stars)
        params = {"q": query, "sort": sort, "order": order}
        
        try:
            response = requests.get(self.api_url, params=params)
            return self._handle_response(response)
        except requests.RequestException as e:
            raise DataSourceException(str(e))
    
    def _build_query(self, languages, min_stars):
        """Construct GitHub search query"""
        query = " ".join(f"language:{lang.strip()}" for lang in languages)
        return query + f" stars:>{min_stars}"
    
    def _handle_response(self, response):
        """Process GitHub API response"""
        if response.status_code == 403:
            raise RateLimitException()
        elif response.status_code != 200:
            raise DataSourceException(response.status_code)
        
        items = response.json().get("items", [])
        return [
            Repository(item["name"], item["language"], item["stargazers_count"])
            for item in items
        ]