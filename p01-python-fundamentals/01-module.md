# Service Module
We will introduce a module for handling the retrieval and storage of excuses.
> This workshop can be started by checking out https://github.com/rahulswarnkar/excuse-manager/tags, tag: w1

## Split the Code
`main.py`
```python
from flask import Flask, request, jsonify
import service

app = Flask(__name__)

@app.route("/")
def index():
    return "Excuse Manager"

@app.route("/excuses", methods=['GET'])
def list_excuses():
    app.logger.info("listing excuses")
    return jsonify(service.get_all())

@app.route("/excuses/<int:id>", methods=['GET'])
def get_excuse(id):
    app.logger.info("getting excuse by id")
    excuse = service.get_by_id(id)
    if(excuse is None):
        return 'excuse not found', 404
    return jsonify(excuse)

@app.route("/excuses", methods=['POST'])
def add_excuse():
    body = request.get_json()
    if('message' not in body):
        return 'message not found', 400
    app.logger.info("adding an excuse")
    service.add(body)
    return '', 201

@app.route("/excuses/<int:id>", methods=['DELETE'])
def delete_excuse(id):
    app.logger.info("deleting an excuse by id")
    if(service.delete_by_id(id)):
        return '', 200
    return 'excuse not found', 404

if __name__ == "__main__":
    app.run()
```
`service.py`
```python
_excuse_list = []

def replace_list(new_list):
    global _excuse_list
    _excuse_list = new_list

def get_all():
    return _excuse_list

def get_by_id(id):
    excuse = next((excuse for excuse in _excuse_list if excuse['id'] == id), None)
    return excuse

def add(excuse):
    id = len(_excuse_list) + 1
    excuse_to_add = {
        'id': id,
        'message': excuse['message']
    }
    _excuse_list.append(excuse_to_add)

def delete_by_id(id):
    excuse = get_by_id(id)
    if(excuse is None):
        return False
    _excuse_list.remove(excuse)
    return True
```

---

## Add Test
`test_service.py`
```python
from importlib import reload
from unittest import TestCase
import service
class TestStringMethods(TestCase):

    def setUp(self):
        reload(service)

    def test_add(self):#what's wrong here?
        service.add({"message":"dummy excuse 1"})
        service.add({"message":"dummy excuse 2"})
        excuses = service.get_all()
        self.assertEqual(len(excuses), 2, "length doesn't match")
        excuse = excuses[0]
        self.assertIn('id', excuse.keys(), "id wasn't generated")

    # def test_get_all(self):
    #     pass

    # def test_get_by_id(self):
    #     pass

    # def test_delete_by_id(self):
    #     pass

if __name__ == '__main__':
    unittest.main()
```

---

## Exercise

* Add the remaining tests
* What's wrong with `test_add`?