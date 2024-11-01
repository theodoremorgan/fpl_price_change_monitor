import json
import os

def add_player_to_file(file_path: str, id: str):
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

#add_player_to_file("./data/watchlist/current/testtesttest.json", "1234567")
#add_player_to_file("./data/watchlist/current/testtesttest.json", "1234565")
#add_player_to_file("./data/watchlist/current/testtesttest.json", "12347")
#add_player_to_file("./data/watchlist/current/testtesttest.json", "1234567")
