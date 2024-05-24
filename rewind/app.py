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


@app.route("/post", methods=['POST'])
def post():
    payload = request.json
    userID = int(payload['id'])
    msg = payload['msg']

    if userID not in app.users:
        return "사용자가 존재하지 않습니다.", 400
    if len(msg) > 300:
        return "300자를 초과했습니다.", 400

    app.posts.append({
        'user_id': userID,
        'tweet': msg
    })
    return '성공', 200

@app.route("/check-tweet", methods=['GET'])
def check_tweet():
    return app.posts

if __name__ =='__main__':
    app.run(debug=True)