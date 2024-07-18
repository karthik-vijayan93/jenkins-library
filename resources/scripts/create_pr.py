import os
import sys
import requests

def create_pull_request(repo_url: str, source_branch: str, destination_branch: str, pr_title: str, pr_description: str, token: str) -> None:
    if repo_url.endswith('.git'):
        repo_url = repo_url[:-4]
    api_url = repo_url.replace('https://github.ibm.com/', 'https://api.github.ibm.com/repos/') + '/pulls'
    pr_data = {
        'title': pr_title,
        'head': source_branch,
        'base': destination_branch,
        'body': pr_description
    }
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github+json'
    }
    try:
        response = requests.post(api_url, json=pr_data, headers=headers)
        if response.status_code == 201:
            pr_url = response.json().get('html_url')
            print(f"Pull request created successfully: {pr_url}")
        else:
            print(f"failed to create pull request: {response.status_code}")
            print(response.json())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if 'GITHUB_TOKEN' not in os.environ:
        print("error: GITHUB_TOKEN environment variable not set")
        sys.exit(1)
    repo_url = sys.argv[1]
    source_branch = sys.argv[2]
    destination_branch = sys.argv[3]
    pr_title = sys.argv[4]
    pr_description = sys.argv[5]
    token = os.environ['GITHUB_TOKEN']
    if not all([repo_url, source_branch, destination_branch, pr_title, pr_description]):
        print("error: missing required arguments")
        sys.exit(1)
    create_pull_request(repo_url, source_branch, destination_branch, pr_title, pr_description, token)