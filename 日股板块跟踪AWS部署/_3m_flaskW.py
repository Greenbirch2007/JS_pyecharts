#! -*- coding:utf-8 -*-
import json
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import copy
import operator

app = Flask(__name__)



@app.route('/js/j225')
def js_j225():
    return render_template('j225.html') # 在一个目录下,templates中


@app.route('/')
def index():
    return "部署测试"

@app.route('/js/j400')
def js_j400():
    return render_template('JS_Mons400.html') # 在一个目录下,templates中



@app.route('/js/normal')
def js_normal():
    return render_template('JS_Mons.html') # 在一个目录下,templates中


# 注意html必须放在templates目录下
if __name__ == '__main__':

    app.run(debug=True)





