from flask import Flask
import random

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'hello test'
if __name__ == '__main__':

    port = 5000 + random.randint(0, 999)
    print(port)
    url = "http://127.0.0.1:{0}".format(port)
    print(url)
    app.run(use_reloader=False, debug=True, port=port)