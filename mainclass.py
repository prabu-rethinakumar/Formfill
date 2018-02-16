from flask import *
import os
app = Flask(__name__)

port = int(os.environ.get("port"))


@app.route("/start")
def run_job():
    return render_template('home.html')


if __name__ == '__main__':
    print("Running application on port : {}".format(port))
    app.run(host="0.0.0.0", port=port)





