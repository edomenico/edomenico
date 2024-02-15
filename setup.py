from github import Github

g = Github('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')

repo = g.get_repo('edomenico/edomenico')

with open('metar_trat_teste2.csv', 'r') as file:
    data = file.read()

repo.create_file('data/dataset.csv', 'upload csv', data, branch='main')


