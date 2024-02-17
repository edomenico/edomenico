from github import Github
#from github_token import GITHUB_TOKEN


access_token = "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"
g1 = Github(access_token, base_url="https://edomenico/api/v3")



#Get org object
org = g1.get_organization('edomenico')
print(org)




