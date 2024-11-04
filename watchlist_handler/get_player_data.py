import requests, json, os
import pandas as pd
from datetime import date
from config import (data_dir_path, player_data_dir, watchlist_dir, date_format, fantasy_base_url)
from add_new_player import watchlist_file_name

#https://fantasy.premierleague.com/api/bootstrap-static/
# returns
# players in 'elements' - a dict of elements with numeric keys
# player id can be found in each dict - seems to equal the key + 1

# transfers_in
# transfers_in_event
# transfers_out
# transfers_out_event

# cost_change_event (net change this week? this day?)
# cost_change_event_fall (negative of above)
# cost_change_start (net change from start)
# cost_change_start_fall (negative of above)

# now_cost

today = date.today()
player_data_file_name:str = today.strftime(date_format) + '_player_data'

def download_watched_player_data_to_file(watchlist_file_path: str, target_file_path:str):

    if not os.path.exists(target_file_path):
        base_dir = os.path.dirname(target_file_path)
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        with open(target_file_path, 'w') as file: 
            data = {}
            json.dump(data,file)
    
    r = requests.get(fantasy_base_url + 'bootstrap-static/').json()
    player_data = r['elements']
    df = pd.DataFrame(player_data)
    df.drop(df.columns.difference(["first_name", "second_name", "id", "web_name", "transfers_in", "transfers_in_event", "transfers_out", "transfers_out_event", "cost_change_event", "cost_change_event_fall", "cost_change_start", "cost_change_start_fall", "now_cost"]), axis=1, inplace=True)
    #print(df)

    with open(watchlist_file_path, 'r') as file:
        player_ids = json.load(file)
        player_data = df.loc[df['id'].isin(player_ids)]
        player_data_json = player_data.to_json(orient = 'records')
    with open(target_file_path, 'w') as file:
        json.dump(json.loads(player_data_json), file, indent = 4)

def archive_data(file_path: str, target_file_path: str):

    if not os.path.exists(file_path):
        return

    if not os.path.exists(target_file_path):
        base_dir = os.path.dirname(target_file_path)
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        with open(target_file_path, 'w') as file: 
            data = {}
            json.dump(data,file)

    with open(file_path, 'r') as file:
        data = json.load(file)
    with open(target_file_path, 'w') as file:
        json.dump(data, file, indent = 4)

def download_todays_data():

    watchlist_file_path: str = data_dir_path + watchlist_dir + watchlist_file_name
    player_data_file_path: str = data_dir_path + player_data_dir + player_data_file_name
    player_data_archive_file_path: str = data_dir_path + player_data_dir + "archive/" + player_data_file_name

    archive_data(player_data_file_path, player_data_archive_file_path)

    download_watched_player_data_to_file(watchlist_file_path, player_data_file_path)

#tests 

"""
watchlist_file_path: str = data_dir_path + watchlist_dir + today.strftime(date_format) + '_watchlist' 
player_data_file_path: str = data_dir_path + player_data_dir + today.strftime(date_format) + '_player_data' 
download_watched_player_data_to_file(watchlist_file_path, player_data_file_path)
archive_data(player_data_file_path, )
"""
download_todays_data()