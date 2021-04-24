# 1. Before using GitHub API, it is required to generate a personal access token. You can visit this website to acquire one: https://github.com/settings/tokens
# 2. Before start anything, you can visit GitHub API interface to get preliminary knowledge about what information will be returned.
#   Example 1, if you would like to get developer data of "ycpss91303", you can visit the website: https://api.github.com/users/ycpss91303
#   Example 2, if you would like to get repository data of 'Visual Studio Code' from Microsoft, you can visit: https://api.github.com/repos/microsoft/vscode
#   You can visit GitHub API support website for more information: https://docs.github.com/en/rest
# 3. Install "PyGitHub" and "Requests" libraries by running: "pip install PyGithub requests" in your terminal

from pprint import pprint

# Paste the token you just generated
token = "XXXXXXXXXXXXXXXXXXXXXXXXXX"

def main():
    ###### You can unblock all runable code to invesigate the outputs. ######

    # Query user: we will use "Requests" library to perform this action
    query_user("ycpss91303")

    # Query repository: we will use "PyGitHub" library to perform this action
    query_repo('microsoft', 'vscode')


def query_repo(owner:str, project:str):
    # owner: project owner
    # project: name of project that you want to query
    ## ATTENTION: project must be owned by owner, otherwise no result will be found. ##

    from github import Github

    # Generate the instance of GitHub
    g = Github(token)
    
    # Query repo entity
    repo = g.get_repo("{}/{}".format(owner, project))
    
    # You can view the JSON format data by using "repo.raw_data"
    # pprint(repo.raw_data)
    
    # Query issues that you just found (let's queyr open issues)
    issues = repo.get_issues(state="open")

    # You can use for loop to iterate issues (ATTENTION: by doing this, you will get raw data of all issues, which are pretty lengthy)
    for issue in issues:
        # pprint(issue.raw_data)
        
        # You can obtain discussions of issues
        discussions = issue.get_comments()
        
        # Using for loop to iterate conversations and their detailed information
        for dis in discussions:
            # print out comment
            pprint(dis.raw_data)

    # Last but not least, you can query pull request and their contents
    prs = repo.get_pulls()

    for pr in prs:
        # Retrieve raw data of pull request
        # pprint(pr.raw_data)

        # Retrieve comments of pull request
        comments = pr.get_comments()
        
        for c in comments:
            pprint(c.raw_data)

def query_user(user:str):
    # user: user account, this serves an identical information throughout entire GitHub API and website
    import requests
    
    query_url = f"https://api.github.com/users/{user}"
    headers = {'Authorization': f'token {token}'}
    r = requests.get(query_url, headers=headers)
    pprint(r.json())


if __name__ == "__main__":
    main()