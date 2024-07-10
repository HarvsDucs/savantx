from flask import Flask, render_template, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return jsonify({
        "message": "Hello Worldss"
    })

if __name__ == '__main__':
    app.run(debug=True)
    