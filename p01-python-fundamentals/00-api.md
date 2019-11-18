# Excuse Manager API
We will create a simple stupid API for keeping track of excuses. The API will have the following endpoints:

* `GET /excuses/{id}`

  Returns:
  ```
  {
    "id": "0",
    "author": "",
    "message": ""
  }
  ```
* `GET /excuses`

  Returns:
  ```
  [
    {
        "id": "0",
        "author": "",
        "message": ""
    }
  ]
  ```
* `POST /excuses`

  Post an excuse
  ```
  {
    "message": ""
  }
  ```
* `DELETE /excuses/{id}`

  Deletes an excuse by id

## Try in Python
### Create Virtual Environment (optional)
Shell:
```
python3 -m venv sentiment
source ./bin/activate
```
### Dependencies
Shell:
```
pip3 install requests flask
```
### Tools (optional)
Install this Chrome extension: [JSON Formatter](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa) or something similar for your browser. 

## Code
Create a file called `main.py` and paste the following code:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

excuse_list = []

def replace_list(new_list):
    global excuse_list
    excuse_list = new_list

@app.route("/")
def index():
    return "Excuse Manager"

@app.route("/excuses", methods=['GET'])
def list_excuses():
    app.logger.info("listing excuses")
    return jsonify(excuse_list)

@app.route("/excuses", methods=['POST'])
def add_excuse():
    body = request.get_json()
    if('message' not in body):
        return 'message not found', 400
    excuse = {
        'id': len(excuse_list) + 1,
        'author': request.remote_addr,
        'message': body['message']
    }
    app.logger.info("adding an excuse")
    replace_list(excuse_list + [excuse])
    return '', 201

@app.route("/excuses/<int:id>", methods=['DELETE'])
def delete_excuse(id):
    app.logger.info("deleting an excuse")
    excuse = next((excuse for excuse in excuse_list if excuse['id'] == id), None)
    if(excuse is None):
        return 'excuse not found', 404
    replace_list([excuse for excuse in excuse_list if excuse['id'] != id])
    return '', 200

if __name__ == "__main__":
    app.run()
```
## Run
Shell:
```
python main.py
```
You should see something like this on the console:
```
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```
### List excuses

Visit http://127.0.0.1:5000/ in a browser to see the current list, which should be an empty list.

In a separate console, start a python3 REPL:
```
source ./bin/activate
python3
```
In the REPL:
```
>>> requests.get("http://localhost:5000/excuses").json()
```

### Add an excuse
REPL:
```
>>> requests.post("http://localhost:5000/excuses", json={'message':'central line again!'})

>>> requests.post("http://localhost:5000/excuses", json={'message':'got stung by bees'})
```
The above requests should have a 201 response:
```
<Response [201]>
```
Refresh the browser or list excuses in REPL as above.

### Fetch an excuse
Visit http://127.0.0.1:5000/1 in a browser to see an excuse by id.

REPL:
```
>>> requests.get("http://localhost:5000/excuses/1")
```
The above requests should have a 200 response (or 404 if not found).

### Delete an excuse
REPL:
```
>>> requests.delete("http://localhost:5000/excuses/1")
```
The above requests should have a 200 response (or 404 if not found).