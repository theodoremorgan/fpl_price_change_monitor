import requests

#https://fantasy.premierleague.com/api/bootstrap-static/
# returns
# players in 'elements' - a dict of elements with numeric keys
# player id can be found in each dict - seems to equal the key + 1
# 
# first_name and last_name is there too


# 1. create fuzzy matching function for first and second name; to match with the first_name and seccond_named fields in 'element' from the bootstrap-static call 
# need to give a fuzzy match for first / second name (because of accents etc.)