import json

# receives the response from the request.get method and parses it to simple json structure
def json_viewer(data):
    data = json.loads(data.text)
    return data

#iterates through the team name, points, and form data from the json structure and returns it as list 'league_list'
def create_array(func):
    count = 0
    league_list = []
    while count < 20:
        team_name = func['response'][0]['league']['standings'][0][count]['team']['name']
        points = func['response'][0]['league']['standings'][0][count]['points']
        form = func['response'][0]['league']['standings'][0][count]['form']
        league_list.append([count + 1, team_name, points, form])
        count += 1
    return league_list


