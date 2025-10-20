#!/usr/bin/env python3

"""
A Simple Flask Web Application interface
For viewing popular GitHub Repos sorted by stars using the
GitHub Search API.

To run:
(env) $ python -m pip install -r requirements.txt
(env) $ export FLASK_ENV=development; python3 -m flask run

Flask application - now decoupled from specific implementations
"""
from flask import Flask, render_template, request

from config import Config
from repos import RepositoryManager, RepositoryException
from repos.services import GitHubService

app = Flask(__name__)

# Dependency injection - initialize services
config = Config()
github_service = GitHubService()
repo_manager = RepositoryManager(github_service, config)


@app.route('/', methods=['POST', 'GET'])
def index():
    """Handle requests - delegates to repo_manager"""
    selected_languages = (
        request.form.getlist("languages") 
        if request.method == 'POST' 
        else config.AVAILABLE_LANGUAGES
    )
    
    results = repo_manager.search(selected_languages)
    
    return render_template(
        'index.html',
        selected_languages=selected_languages,
        available_languages=repo_manager.get_available_languages(),
        results=results
    )


@app.errorhandler(RepositoryException)
def handle_repository_error(error):
    """Handle repository-related errors"""
    return render_template('error.html', message=error)


if __name__ == '__main__':
    app.run(debug=True)