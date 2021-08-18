from flask import Flask, request

app = Flask(__name__)

sql_inj_char =["=", "-", "\\", "'"]

@app.route('/v1/sanitized/input/', methods=['POST'])
def payload_post():
    payload_input = request.json['payload']
    for char in payload_input:
        if char in sql_inj_char:
            return {"result": "not sanitized"}
    return {"result": "sanitized"}

if __name__=="__main__":
    app.run(debug = True)
