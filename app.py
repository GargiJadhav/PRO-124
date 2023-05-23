from flask import Flask , jsonify , request

app = Flask(__name__)

contacts = {

       "data":[ {
            "Contact":"8888456578",
            "Name":"Malishka",
            "Done":False,
            "id":1
        },
        {
            "Contact":"9378124568",
            "Name" : "Sherlin",
            "Done":False,
            "id":2
        }]

}


@app.route("/add-data", methods=["POST"])
def addTask():
    if not request.json:
        return jsonify(
            {
                "status":"error",
                "Message":"Kindly Enter the Contact Number !!"
            }
        )
    contact = {
        'id':contacts[-1]['id']+1,
        'Name':request.json["Name"],
        'Done':False,
        'Contact':request.json.get["Contact",""]
        
    }
    contacts.append(contact)

    return jsonify({
        "status":"success",
        "Message":"Contact Added Successfully !!"
    })

app.run()