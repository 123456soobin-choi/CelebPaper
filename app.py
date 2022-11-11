from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
import config
app = Flask(__name__)

client = MongoClient(config.mongodb_url)
db = client.dbsparta


@app.route('/')
def landing():
    return render_template('landing.html')


@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/detail')
def detail():
    return render_template('detail.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/create')
def create():
    return render_template('create.html')


if __name__ == '__main__':
    app.run()
