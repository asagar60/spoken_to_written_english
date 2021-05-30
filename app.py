# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 11:17:49 2021

@author: asaga
"""


#loading libraries
import flask
from flask import Flask, request
from spoken_to_written_english.convert_spoken_to_written_digit import convert

# https://www.tutorialspoint.com/flask
app = flask.Flask(__name__)
# render_template

@app.route('/')
def home():

    """Serve homepage template."""
    return flask.render_template('index.html')
    #return flask.render_template('index.html')

@app.route('/output', methods=['POST'])
def output():
    
    text = request.form.to_dict()['inp_text']
    output_text = convert(text)
    print(output_text)
    return flask.render_template('index.html',results=output_text)
    #return jsonify({'products': recommended_products, 'Time': difference, 'predict_list':to_predict_list, 'top5':top5_products})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)

