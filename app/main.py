from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Get a "welcome" message from an environment variable, or use a default
    welcome = os.environ.get('WELCOME_MESSAGE', 'Hello from Kubernetes!')
    return f"<h1>{welcome}</h1>"

if __name__ == '__main__':
    # Listen on all interfaces (0.0.0.0) and on port 5000
    app.run(host='0.0.0.0', port=5000)
