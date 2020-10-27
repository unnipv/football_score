import requests
import sys
import pprint
from bs4 import BeautifulSoup
team = sys.argv[1]
URL = 'https://www.google.com/search?q=' + team +'+score&oq='+team +'+score'
# URL='https://www.google.com/search?q=arsenal+score&oq=arsenal+score'
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
headers = {"user-agent" : USER_AGENT} 
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
# pprint.pprint(soup.prettify())
results=soup.find(id='search')
# pprint.pprint(results.prettify())
score_table_div = results.find('div', class_='imso-ml-c')
score_table=score_table_div.find('table',class_='ml-bs-u liveresults-sports-immersive__match-grid')

scores=[['','','',''],['','','',''],['','','',''],['','','',''],['','','',''],['','','','']]

# for elem in score_rows:
team_names=score_table.find_all('div',class_='ellipsisize kno-fb-ctx')
team_scores=score_table.find_all('div',class_='imspo_mt__t-sc')

match_iter=0
team_iter=0
score_iter=1
for name in team_names:
    scores[match_iter][team_iter]=name.text
#     print(scores[match_iter][team_iter])
    if team_iter==0:
        team_iter=2
    else:
        team_iter=0
        match_iter+=1

# print(scores)       
match_iter=0
for score in team_scores:
    scores[match_iter][score_iter]=score.text
    if score_iter==1:
        score_iter=3
    else:
        score_iter=1
        match_iter+=1

score_string=''
for match in scores:
    score_string+=match[0] + ' ' + match[1] + ' - ' + match[2] + ' ' + match[3] + '\n'
print(score_string)




