from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def index():
    # This function is called when the root URL is accessed
    return 'Hello, Flask!'

# Check if the run.py file is being run directly
if __name__ == '__main__':
    # If true, run the Flask application
    app.run(debug=True)
