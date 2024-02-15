#from github import Github

#g = Github('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')

#repo = g.get_repo('edomenico/edomenico')

#with open('metar_trat_teste2.csv', 'r') as file:
#    data = file.read()

#repo.create_file('data/dataset.csv', 'upload csv', data, branch='main')
import pandas as pd
import requests,csv
url = 'https://api.github.com/repos/edomenico/edomenico/contents/escala1050.xlsx?ref=main'
data = requests.get(url, headers={'Authorization': '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', 'Accept': 'application/vnd.github.v3.raw'})
with open("escala1050.xlsx", 'rb') as f:
  f.write(data.content)
df = pd.read_csv('escala1050.xlsx')
print(df)

