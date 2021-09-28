from flask import Flask, jsonify, request 

app = Flask(__name__)

List = [
    {
        'id':1,
        'Name':u'Pedro'
        'Contact':u'99818318383'
        'done':False
    },
    {
        'id':2,
        'Name':u'Maria'
        'Contact':u'99178286286'
        'done':False
    }
]

@app.route('/')
def hello_world():
    return "Whatsupp World!"

@app.route("/app-data",methods=["POST"])
def add_task():
   if not request.json:
       return jsonify({
           "status":"error"
           "message":"Please Provide Data!"
       },400)

contact = {
    'id':tasks[-1]['id'] + 1,
    'Name':request.json['Name']
    'Contact':request.json.get('Contact',"")
    'done':False
}
List.append(contact)
return jsonify({
    "status":"succes"
    "message":"Contact Added"
})

@app.route("/app-data")
def get_task():
    return jsonify({
        'data':List
    })

if (__name__ == "__main__"):
    app.run(debug=True)