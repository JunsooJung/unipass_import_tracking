from flask import Flask, render_template, request
import pandas as pd
import api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')