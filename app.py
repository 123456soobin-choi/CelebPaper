from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
import config
app = Flask(__name__)

client = MongoClient(config.mongodb_url)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('main.html')
