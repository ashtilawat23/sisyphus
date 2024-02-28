import requests
import os
from datetime import datetime

def create_branch(token, repo_owner, repo_name, base_branch="main"):
    """Create a new branch from the base branch."""
    branch_name = f"readme-update-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    # Get the latest commit of the base branch
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/ref/heads/{base_branch}"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    latest_commit_sha = response.json()["object"]["sha"]

    # Create a new branch
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/refs"
    data = {
        "ref": f"refs/heads/{branch_name}",
        "sha": latest_commit_sha
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Branch {branch_name} created successfully.")
        return branch_name
    else:
        print("Failed to create branch")
        print(response.text)
        return None

def create_pull_request(token, repo_owner, repo_name, branch_name, base_branch="main"):
    """Create a pull request from the new branch to the base branch."""
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"
    headers = {"Authorization": f"token {token}"}
    data = {
        "title": "Automated README update",
        "head": branch_name,
        "base": base_branch,
        "body": "This is an automated PR to update the README based on recent changes."
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Pull request created successfully.")
        print(response.json()["html_url"])
    else:
        print("Failed to create pull request")
        print(response.text)

def main():
    token = os.getenv('GITHUB_TOKEN')
    repo_owner = 'your-github-username'
    repo_name = 'your-repo-name'
    
    # Step 1: Create a new branch
    branch_name = create_branch(token, repo_owner, repo_name)
    if not branch_name:
        return

    # Steps to commit and push the updated README to the new branch would go here

    # Step 2: Create a pull request from the new branch to the main branch
    create_pull_request(token, repo_owner, repo_name, branch_name)

if __name__ == "__main__":
    main()