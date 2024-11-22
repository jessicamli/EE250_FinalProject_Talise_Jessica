import requests
import json

# This url is the url to make the http POST request to
url = 'http://127.0.0.1:5000/send_data'

# Make the jsons to display
grid_1 = {
    "grid": [
        "+---+---+",
        "| 1 |   |",
        "+---+---+",  
        "|   |   |",
        "+---+---+"
    ]
}

grid_2 = {
    "grid": [
        "+---+---+",
        "|   | 2 |",
        "+---+---+",  
        "|   |   |",
        "+---+---+"
    ]
}

grid_3 = {
    "grid": [
        "+---+---+",
        "|   |   |",
        "+---+---+",  
        "| 3 |   |",
        "+---+---+"
    ]
}

grid_4 = {
    "grid": [
        "+---+---+",
        "|   |   |",
        "+---+---+",  
        "|   | 4 |",
        "+---+---+"
    ]
}

# Send the post request and get the response back based on which square
# This function can be called from another file
def send_to_http(square):
    if square == 1:
        response = requests.post(url, json = grid_1)
    elif square == 2:
        response = requests.post(url, json = grid_2)
    elif square == 3:
        response = requests.post(url, json = grid_3)
    elif square == 4:
        response = requests.post(url, json = grid_4)
    else:
        return "Not a valid square"
    
    return response

