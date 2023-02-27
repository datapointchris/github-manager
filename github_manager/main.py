import dataset
import json

db = dataset.connect('sqlite:///github-manager.db')

table = db['repos']

keys = ['name', 'html_url', 'description', 'fork', 'url', 'created_at', 'updated_at', 'language', '']







with open('repos.json', 'r') as j:
    repo_list = []
    repos = json.load(j)
    for repo in repos:
        d = {key: repo.get(key) for key in repo if key in keys}
        repo_list.append(d)

        
for repo in repo_list:
    table.insert(repo)
