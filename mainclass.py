from flask import *
import os
app = Flask(__name__)

port = int(os.environ.get("port"))

print("Running application on port : %s".format(port))

if __name__ == 'main':
    print("Running application on port : %s".format(port))




