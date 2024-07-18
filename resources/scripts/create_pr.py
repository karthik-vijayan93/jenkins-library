import sys
import requests
import os

def create_pull_request(repo_url: str, source_branch: str, destination_branch: str, pr_title: str, pr_description: str, token: str):
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
            print("Pull request created successfully.")
        else:
            print(f"Failed to create pull request: {response.status_code}")
            print(response.json())
    except Exception as e:
        print(e)

if __name__ == "__main__":
    repo_url = sys.argv[1]
    source_branch = sys.argv[2]
    destination_branch = sys.argv[3]
    pr_title = sys.argv[4]
    pr_description = sys.argv[5]
    token = os.environ['GITHUB_TOKEN']
    create_pull_request(repo_url, source_branch, destination_branch, pr_title, pr_description, token)