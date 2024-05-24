from flask import Flask, request, jsonify

app = Flask(__name__) 
app.users = {}
app.posts = []
app.idCnt = 1

@app.route("/sign-up", methods=['POST'])
def signUp():
    newUser = request.json
    newUser["id"] = app.idCnt
    app.users[app.idCnt] = newUser
    app.idCnt += 1
    return jsonify(newUser)


@app.route("/check-users", methods=['GET'])
def check_users():
    return app.users


if __name__ =='__main__':
    app.run(debug=True)