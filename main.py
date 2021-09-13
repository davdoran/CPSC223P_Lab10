# -*- coding: utf-8 -*-
"""
Davina Doran
davdoran@csu.fullerton.edu
prof: johnwoates
CPSC 223P-01
Thu Apr 28, 2021
joates@fullerton.edu
"""


import requests
from plotly import offline

"""
import matplotlib.pyplot as plt
squares = [1,4,9,16,25,36]
input_values = [1, 2, 3, 4, 5, 6]

fig, ax = plt.subplots()

ax.set_title("Square Numbers")
ax.plot(input_values, squares, linewidth = 3)
plt.show()

"""

# make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
hders = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=hders)
print(f'Status code: {r.status_code}')

#store API response
response_dict = r.json()

#process  results
print(response_dict.keys())


#part 2
print(f"Total repositories: {response_dict['total_count']}")

#explore info about the repositories
repo_dicts = response_dict['items']
repo_names, stars = [], []
print(f"repositories reuturned: {len(repo_dicts)}")

#examine first
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")

for key in sorted(repo_dict.keys()):
    print(key)
        
print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")




#part 3
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    
#make visualization
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    'marker': {
        'color': 'rgb(60,100,150)',
        'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
        },
    'opacity': 0.6,
    }]

my_layout = {
    'title': 'Most-Starred Python Projects on Github',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'}
    }

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename = 'python_repos.html')
