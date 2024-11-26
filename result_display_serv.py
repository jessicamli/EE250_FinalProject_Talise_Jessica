# File to be run in a terminal, creates a flask server for http communication to display the output

from flask import Flask, request, jsonify

app = Flask(__name__)

grid_data = {"grid": ["Something could be broken"]}

@app.route('/')
def index():
    # Display the grid?
    grid_text = "\n".join(grid_data["grid"])
    return f"<pre>{grid_text}</pre>"  

@app.route('/send_data', methods=['POST'])
def receive_data():
    global grid_data

    # Get the json from the POST request
    data = request.get_json()  
    
    if "grid" in data:
        # Check the data to make sure it is valid, then set the global variable
        grid_data = data  
    
    # return a response
    return "Data transmitted. Yay!!", 200

if __name__ == "__main__":
    app.run(debug=True)
