
import sys
import requests

def create_pull_request(repo_url, source_branch, destination_branch, pr_title):
    api_url = repo_url.replace('https://github.com/', 'https://api.github.com/repos/') + '/pulls'
    pr_data = {
        'title': pr_title,
        'head': source_branch,
        'base': destination_branch
    }
    response = requests.post(api_url, json=pr_data)
    
    if response.status_code == 201:
        print("Pull request created successfully.")
        print(response.json())
    else:
        print(f"Failed to create pull request: {response.status_code}")
        print(response.json())

if __name__ == "__main__":
    repo_url = sys.argv[1]
    source_branch = sys.argv[2]
    destination_branch = sys.argv[3]
    pr_title = sys.argv[4]
    create_pull_request(repo_url, source_branch, destination_branch, pr_title)
