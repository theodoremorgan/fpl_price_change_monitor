import requests

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
