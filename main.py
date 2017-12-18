import json
from flask import Flask
from dbhelper import DBHelper

app = Flask(__name__)
DB = DBHelper('test')

@app.route('/')
def hello_world():
    try:
        data = DB.get_all_inputs()
    except Exception as e:
        print(e)
        data = None
    return json.dumps(data)

if __name__== '__main__':
    app.run(port=5000, debug=True)