from github import Github

g = Github('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')

repo = g.get_repo('edomenico/edomenico/gh_api')

with open('metar_trat_teste2.csv', 'r') as file:
    data = file.read()

repo.create_file('data/dataset.csv', 'upload csv', data, branch='main')


