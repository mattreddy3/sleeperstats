import pandas as pd
import numpy as np
import json
import csv

from sleeperpy import Drafts, User, Players, Leagues
account = User.get_user('mreddy')
sport = 'nfl'
season = 2022
league_id = 854978776533184512
league = Leagues.get_league(league_id)
draft = Drafts.get_all_drafts_for_league(league_id)
draft_id = draft[0]['draft_id']
picks = Drafts.get_all_picks_in_draft(draft_id)
sgdf = pd.read_csv('stats-general.csv')
ssdf = pd.read_csv('stats-scrimmage.csv')
spdf = pd.read_csv('stats-passing.csv')
dfStats = pd.merge(sgdf,ssdf, how = 'outer', on = 'key')
dfAllStats = dfStats.merge(spdf, how = 'outer', on = 'key')
dfAllStats.to_excel('Stats.xlsx')
# file = open('player-ref.json')
# players = json.load(file)
price = []
playerName = []

def myfunc(pick):
    amt = pick['metadata']['amount']
    return amt.zfill(3)


amounts = []
positions = []
teams = []
names = []
points22 = []
picks.sort(key=myfunc, reverse=True)
for pick in picks:
    amounts.append(pick['metadata']['amount']) 
    positions.append(pick['metadata']['position']) 
    teams.append(pick['metadata']['team'])
    names.append(pick['metadata']['first_name'] + ' ' + pick['metadata']['last_name'])
    # TODO: Add full points lookup based on custom scoring
    points22.append(10)
columns=['Amount','Position','Team','Name', '2022 Points']
# technologies =  ['Spark','Pandas','Java','Python', 'PHP']
# fee = [25000,20000,15000,15000,18000]
# duration = ['5o Days','35 Days',np.nan,'30 Days', '30 Days']
# discount = [2000,1000,800,500,800]
# columns=['Courses','Fee','Duration','Discount']
# myZipped = zip(technologies,fee,duration,discount)
# myList = list(myZipped)
# df = pd.DataFrame(list(zip(technologies,fee,duration,discount)), columns=columns)
# df.to_excel('Draft.xlsx')
df = pd.DataFrame(list(zip(amounts,positions,teams,names,points22)), columns=columns)
df.to_excel('Draft.xlsx')

print("done")
