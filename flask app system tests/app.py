from flask import Flask, jsonify

app = Flask(__name__)
# initialise a new variable called 'app' and give it a new value of a Flask object
# identify the new Flask app with a unique "__name__" which contains path of the currently running module


@app.route('/')  # set the endpoint - homepage of the app - to "/"
def home():  # define a function which runs whenever a browser / client accesses the endpoint
    return jsonify({'message': 'Hello world'})  # jsonify turns a dictionary into a string


if __name__ == '__main__':
    # it is satisfied only when we run this specific file
    # if a file is imported, its name is not __main__ so the app.run() is not executed
    app.run()
