import json
import os
from datetime import date
from config import (data_dir_path, watchlist_dir, date_format)

today = date.today()
watchlist_file_name = today.strftime(date_format) + '_watchlist' 

def add_player_to_list(id: str):
    today = date.today()

    watchlist_file_path: str = data_dir_path + watchlist_dir + today.strftime(date_format) + '_watchlist' 

    if not os.path.exists(watchlist_file_path):
        base_dir = os.path.dirname(watchlist_file_path)
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        with open(watchlist_file_path, 'w') as file: 
            data = []
            json.dump(data,file)
    
    with open(watchlist_file_path, 'r') as file:
        data = json.load(file)
        if id in data:
            raise Exception("this player is already on the list")
        data.append(id)
    with open(watchlist_file_path, 'w') as file:
        json.dump(data, file)
    

"""
add_player_to_list(1)
add_player_to_list(2)
add_player_to_list(3)
add_player_to_list(2)
"""
