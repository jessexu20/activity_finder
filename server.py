# This file provided by Facebook is for non-commercial testing and evaluation
# purposes only. Facebook reserves all rights not expressly granted.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# FACEBOOK BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import json
import os
from flask import Flask, Response, request

app = Flask(__name__, static_url_path='', static_folder='')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

@app.route('/api/comments', methods=['GET', 'POST'])
def comments_handler():

    with open('comments.json', 'r') as file:
        comments = json.loads(file.read())

    if request.method == 'POST':
        comments.append(request.form.to_dict())

        with open('comments.json', 'w') as file:
            file.write(json.dumps(comments, indent=4, separators=(',', ': ')))

    return Response(json.dumps(comments), mimetype='application/json', headers={'Cache-Control': 'no-cache'})
@app.route('/events/json',methods=['GET'])
def events_handler():
    try:
        with open('photo/json','r') as file:
            data=json.loads(file.read())
            return json.dumps(data,indent=4, separators=(',', ': ')),200
    except Exception , e:
        print e
@app.route('/shutdown')
def server_shutdown():
    shutdown= request.environ.get('werkzeug.server.shutdown')
    shutdown()
    return "Server shutting down"
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=int(os.environ.get("PORT",80)))
