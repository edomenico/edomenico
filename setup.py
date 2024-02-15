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

access_token = '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'

hub = Github(access_token) # Github(user, pass)

# Displaying all the existing Repositories and files
for repo in hub.get_user().get_repos():
    # Displaying repo name
    print("Repository [{}]".format(repo.edomenico))
    print("_" * 50)
    # Displaying Contents
    print("[Contents]")
    count = 1
    for content in repo.get_contents(""):
        print("{}. {} [{}]".format(count, content.path, content.type))
        if content.type == 'dir':
            new_count = 1
            # Displaying contents of sub-director
            for sub_content in repo.get_contents(content.path):
                print("    {}. {} [{}]".format(new_count, sub_content.path, sub_content.type))
                new_count += 1
                # Displaying contents of sub directory of sub directory
                if sub_content.type == 'dir':
                    another_count = 1
                    for datain in repo.get_contents(sub_content.path):
                        print("        {}. {} [{}]".format(another_count, datain.path, datain.type))
                        another_count += 1

        count += 1
    print("-" * 50)

