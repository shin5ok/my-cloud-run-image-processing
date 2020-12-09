# Copyright 2019 Google, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START run_imageproc_controller]
import base64
import json
import os
import sys
import json
from datetime import datetime

from flask import Flask, request

# import image
import requests


app = Flask(__name__)


@app.route('/test', methods=['GET'])
def _test():
    sys.stderr.write("stderr\n")
    sys.stdout.write("stdout\n")
    print("/test is retrieved")
    return ("test", 200)

@app.route('/datetime')
def _datetime():
    return json.dumps({'datetime':datetime.now().strftime("%Y-%m-%dT%H:%M:%S")})

if __name__ == '__main__':
    PORT = int(os.getenv('PORT')) if os.getenv('PORT') else 8080
    app.run(host='127.0.0.1', port=PORT, debug=True)
