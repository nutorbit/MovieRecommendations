from flask_cors import CORS
from flask import Flask, request

# initial server
app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET', 'POST'])
def test():
    return 'test'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)