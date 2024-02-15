#from github import Github

#g = Github('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')

#repo = g.get_repo('edomenico/edomenico')

#with open('metar_trat_teste2.csv', 'r') as file:
#    data = file.read()

#repo.create_file('data/dataset.csv', 'upload csv', data, branch='main')
import pandas as pd
import requests
url = 'https://api.github.com/repos/edomenico/edomenico/contents/metar_trat_teste2.csv?ref=main'
data = requests.get(url, headers={'Authorization': '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', 'Accept': 'application/vnd.github.v3.raw'})
with open("metar_trat_teste2.csv", 'r') as f:
  f.write(data.content)
df = pd.read_csv('metar_trat_teste2.csv')
print(df)

