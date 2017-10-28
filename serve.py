#!/usr/bin/env python
"""
 This module serves the HTTP requests for the application.
"""

import sqlite3
import sys

from flask import Flask
from flask import render_template
from flask import request, redirect
from model.step import Step
from model.flow import Flow
from model.pipeline import Pipeline

app = Flask(__name__)

steps = []
flows = []
pipelines = []

import logging
LOGGER = logging.getLogger("DatabaseBuilder")
LOGGER.setLevel(logging.DEBUG)
SH = logging.StreamHandler(sys.stdout)
SH.setLevel(logging.DEBUG)
FORMATTER = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
SH.setFormatter(FORMATTER)
LOGGER.addHandler(SH)

def init_db():
    conn = sqlite3.connect("cat-ci.db")
    cursor = conn.cursor()
    print "Initialize Cat CI database ..."
    with open("init.sql", "r") as init_sql:
        for line in init_sql:
            if not line.startswith('#'):
                print "Executing " + line.strip() + "..."
                cursor.execute(line)
                print "Done"

def load_db():
    conn = sqlite3.connect("cat-ci.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * from Steps')
    results = cursor.fetchall()
    for step in results:
        steps.append(Step(step[1], step[3], step[2]))
    cursor.execute('SELECT * from Flows')
    results = cursor.fetchall()
    for flow in results:
        flows.append(Flow(flow[1], flow[3].split(','), flow[2]))
    cursor.execute('SELECT * from Pipelines')
    results = cursor.fetchall()
    for pipeline in results:
        pipelines.append(Pipeline(pipeline[1], pipeline[3].split(','), pipeline[2]))

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/list")
def list():
    return render_template('list.html', steps=steps, flows=flows, pipelines=pipelines)

@app.route("/step/new")
def new_step():
    return render_template('new_step.html')

@app.route("/step/add", methods=['POST'])
def add_step():
    steps.append(Step(request.form['name'],
                      request.form['step_desc'],
                      request.form['description']))
    return redirect("/list", code=302)

@app.route("/flow/new")
def new_flow():
    return render_template('new_flow.html')

@app.route("/flow/add", methods=['POST'])
def add_flow():
    flows.append(Flow(request.form['name'],
                      request.form['steps'].split(','),
                      request.form['description']))
    return redirect("/list", code=302)

@app.route("/pipeline/new")
def new_pipeline():
    return render_template('new_pipeline.html')

@app.route("/pipeline/add", methods=['POST'])
def add_pipeline():
    pipelines.append(Pipeline(request.form['name'],
                              request.form['flows'].split(','),
                              request.form['description']))
    return redirect("/list", code=302)

if __name__ == "__main__":
    try:
        init_db()
    except sqlite3.OperationalError as err:
        print "All database exists!"
    load_db()
    app.run()
