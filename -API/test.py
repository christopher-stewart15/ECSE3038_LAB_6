from flask import Flask, request
from pytz import datetime
from flask_pymongo import PyMongo
from marshmallow import Schema, fields, ValidationError

import pytz
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://Chris:C.stewart1999@cluster0.qizib.mongodb.net/Chris?retryWrites=true&w=majority"
mongo = PyMongo(app)

class TankValidation(Schema):
    water_level = fields.Integer(required = True)
    tank_id = fields.Integer(required = True)



@app.route("/tank", methods = ["POST"])
def data_post():
    req = request.json
    water_level = req["water_level"] 
    percentage = ((water_level * -53)+10530)* 0.01
    percentage = int(percentage)
    database = {
        "tank_id" : req["tank_id"],
        "water_level" : percentage
    }
    tVar = datetime.datetime.now(tz=pytz.timezone('America/Jamaica'))
    tVartoString = tVar.isoformat()
    try:
        print(database)
        tankTemp = TankValidation().load(database)
        mongo.db.tanks.insert_one(tankTemp)
        return {"success": "true","msg": "Data Saved In Database Successfully", "Date": tVartoString}

    except ValidationError as ve:
        return ve.messages, 400

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0")