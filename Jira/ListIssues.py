import requests

def fetch_jira_issues(project_key):
    # Jira API endpoint for searching issues
    url = f"https://testorchestrate.atlassian.net/rest/api/2/search"

    # Jira credentials
    username = "jam414@yahoo.com"
    password = "ATATT3xFfGF0VxTQJECT1_4Lk4Y8CRqiDhf6o0AyyTaya1CipVHAgK-C6-NAMUszaSgk3UcV24qouHLFRWB5QYrcddkN6r0ElGxdZzuGfIvXKvCYDORETW8ACT7AfwVRyblOczSff32izhgvv_qr7gMqRey-yZOCR_9ApEGO3Vnd3bWAveYxYTw=8DB1D440"

    # JQL query to fetch issues of a specific project
    jql_query = f"project = {project_key} ORDER BY key ASC"

    # Request headers
    headers = {
        "Accept": "application/json"
    }

    # Request parameters
    params = {
        "jql": jql_query,
        "maxResults": 100,  # Maximum number of issues to retrieve (adjust as needed)
        "fields": "summary, key",  # Additional fields to retrieve (adjust as needed)
        "startAt": 0
    }

    # Send GET request to Jira API
    response = requests.get(url, headers=headers, params=params, auth=(username, password))

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        issues = data.get("issues", [])

        # Print the list of issues
        for issue in issues:
            issue_id = issue["key"]
            summary = issue["fields"]["summary"]
            print(f"Issue ID: {issue_id}, Summary: {summary}")

    else:
        print(f"Error: {response.status_code} - {response.text}")


# Usage example
project_key = "EMD"
fetch_jira_issues(project_key)
