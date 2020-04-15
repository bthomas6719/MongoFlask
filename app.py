from flask import Flask, jsonify, request, render_template
import pprint
import pymongo 
from bson.json_util import dumps
from bson.json_util import loads
import json
import pandas as pd
from bson import json_util

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client['USDA_consolidated_db']
collection = db['collection']
usda_supplies = db['USDA_consolidated_db']

fcol = {'id':True, 'Commodity':True, 'Region':True, 'Month':True, 'Year':True, 'Tenklbs':True}


@app.route("/usdaSupplies")
def supply():
    
    # write a statement that finds all the items in the db and sets it to a variable
    
    supplies = list(db.collection.find())
    #x = []
    #for product in supplies:
        
        #x.append(product) 
             
    return render_template("index.html", product=json.dumps(supplies, default=json_util.default))
    
    
if __name__ == "__main__":
    app.run(debug=True)

