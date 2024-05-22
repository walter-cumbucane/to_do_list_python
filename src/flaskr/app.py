from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route("/")
def root():
    res =  make_response(jsonify(message="Well done"), 200)
    res.headers['message'] = 'Developing an API'
    return res

def main():
    app.run(host="0.0.0.0", debug=True)


if __name__ == "__main__":
    main()