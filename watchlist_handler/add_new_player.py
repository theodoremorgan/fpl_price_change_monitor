import json
import os
from datetime import date
from config import (data_dir_path, watchlist_dir, date_format)


def add_player_to_list(id: str):
    today = date.today()
    print(today)
    formatted = today.strftime('%Y_%m_%d')
    print(formatted)

    file_path: str = data_dir_path + watchlist_dir + today.strftime(date_format) + '_watchlist' 

    if not os.path.exists(file_path):
        base_dir = os.path.dirname(file_path)
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        with open(file_path, 'w') as file: 
            data = {}
            json.dump(data,file)
    
    with open(file_path, 'r') as file:
        data = json.load(file)
        if id in data.keys():
            raise Exception("this player is already on the list")
        data[id] = {}
    with open(file_path, 'w') as file:
        json.dump(data, file)
    


#add_player_to_list("1234567")
#add_player_to_list("1234565")
#add_player_to_list("12347")
#add_player_to_list("1234567")
