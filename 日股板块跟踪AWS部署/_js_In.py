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



@app.route('/jsin')
def js_j225():
    return render_template('js_industryDT.html') # 在一个目录下,templates中


@app.route('/')
def index():
    return "部署测试"


# 注意html必须放在templates目录下
if __name__ == '__main__':

    app.run(debug=True)





