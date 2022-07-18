
from msilib.schema import Error
from urllib import response
from flask import Flask, redirect, url_for, request , Response
from matplotlib.font_manager import json_dump
import pymongo
import json

app = Flask(__name__)

try:
    mongo=pymongo.MongoClient(host="localhost", 
    port=27017, 
    serverSelectionTimeoutMS=1000)

    db=mongo.company

    mongo.server_info() #trigger exception if cannot connect to db
    print("Connected to mongodb")

except:    
    print(f"Error cannot connect to db {mongo.server_info()}")

######
@app.route('/users', methods=['GET'])
def get_some_users():
    try:
        data = list(db.users.find())
        print(data)
        # return str(data)
        return Response(json.dumps(data), 
        mimetype='application/json')
    except Exception as e: 
        print(f"Error {e}")
        return Response(response=json.dumps(
            {"error": str(e)}),
            status=500, mimetype="application/json")





@app.route('/users', methods=["POST"])
def create_user():
    try:
        # user= {"name": request.json["name"], "email": request.json["email"]}
        # user = {"name": "A", "lastname": "B"}
        user = {"name": request.form["name"], 
        "lastname": request.form["lastname"]}
        dbResponse = db.users.insert_one(user)
        # for att in dir(dbResponse):
        #     print(att)
        return Response(
            response=json.dumps(
                {"message": "User created successfully", "id": f"{dbResponse.inserted_id}"}
            ),
            status=200,
            mimetype="application/json"
        )
        # return f"User created with id {dbResponse.inserted_id}"
        
    except:
        pass
        return "fail"


@app.route('/', methods=["GET"])
def hello_world():
    return "Eagle is gay"


######
if __name__=="__main__":
    app.run(debug=True)