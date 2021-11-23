
from flask import Flask, request
import json
import os, sys

app = Flask(__name__)

path = '../wis-advanced-python-2021-2022/students/'
json_files = os.listdir(path)


# create a dictionary of 'name: data' pairs
def dict_name_data():
    search = request.form.get('search')
    name_data_dict = {}
    for json_file in json_files:
        with open(os.path.join(path, json_file)) as jfile:
            jdata = json.load(jfile)

            search_in_data = any(search in key for key in jdata.keys())
            if search_in_data:
                # format the .json data for display 
                display = '<ul>'
                for key, value in jdata.items():
                    display += f'<li><b>{key}:</b> {value}</li>'
                display += '</ul>'
            
                # add name, data pairs to dictionary
                if "name" in jdata.keys():
                    name_data_dict[jdata["name"]] = display

    return name_data_dict


@app.route("/")
def index():
    return '<h1><a href="/search">Student Search Engine</a></h1>'

@app.route("/search", methods=['GET'])
def search_get():
    return '''
           <form method="POST" action="/search">
           <input name="search">
           <input type="submit" value="Search">
           </form>
           '''

@app.route("/search", methods=['POST'])
def name_links():
    name_data_dict = dict_name_data()
    if not name_data_dict:
        return '<h2>Sorry, your search did not match any entry. Please try something else!</h2>'
    else:
        links = '<h2>These students match your search:</h2><ul>'
        for name, data in name_data_dict.items():
            links += f'<li><a href="/user/{data}">{name}</a></li>'
        links += '</ul>'
    return links

@app.route("/user/<path:fullpath>")
def api_info(fullpath):
    return fullpath
