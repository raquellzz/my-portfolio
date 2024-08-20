from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

app.config.from_pyfile('config.py')