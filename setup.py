#from github import Github

#g = Github('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')

#repo = g.get_repo('edomenico/edomenico')

#with open('metar_trat_teste2.csv', 'r') as file:
#    data = file.read()

#repo.create_file('data/dataset.csv', 'upload csv', data, branch='main')
#import pandas as pd
#import requests
#url = 'https://api.github.com/repos/edomenico/edomenico/contents/metar_trat_teste1.csv?ref=main'
#data = requests.get(url, headers={'Authorization': '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', 'Accept': 'application/vnd.github.v3.raw'})
#with open("metar_trat_teste1.csv", 'r') as f:
#  f.write(data.content)
#df = pd.read_csv(f)
#print(df)


from github import Github

# Authentication is defined via github.Auth
from github import Auth

# using an access token
auth = Auth.Token("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")

# Public Web Github
g = Github(auth=auth)
access_token = "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"

# Github Enterprise with custom hostname
g = Github(access_token, base_url="https://edomenico/api/v3")


for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))





