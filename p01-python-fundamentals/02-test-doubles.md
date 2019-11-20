# Test Doubles
* We will use test doubles to
  * mock responses from dependencies and
  * spy on method invocations
* We will monkey-patch these test doubles to the system under test

> This workshop can be started by checking out https://github.com/rahulswarnkar/excuse-manager/tags, tag: w2

## Test Code
Update `test_main.py` with the following:
```python
from unittest import TestCase
from unittest.mock import patch, Mock
import main

class TestStringMethods(TestCase):

    @patch('service.add')
    def test_add(self, mock):
        with main.app.test_client() as c:
            c.post("/excuses",
                data = '{"message":"dummy excuse"}',
                headers = {'content-type':'application/json'})
            mock.assert_called_once()

    @patch('service.add')
    def test_add_status(self, mock):
        with main.app.test_client() as c:
            response = c.post("/excuses",
                data = '{"message":"dummy excuse"}',
                headers = {'content-type':'application/json'})
            self.assertEqual(response.status_code, 201, 'status code do not match')

    @patch('service.get_all')
    def test_list(self, mock):
        with main.app.test_client() as c:
            mock.return_value = [{"id": 1, "message":"dummy excuse"}]
            response = c.get("/excuses")
            mock.assert_called_once_with()

    @patch('service.get_all')
    def test_list_status(self, mock):
        with main.app.test_client() as c:
            mock.return_value = [{"id": 1, "message":"dummy excuse"}]
            response = c.get("/excuses")
            self.assertEqual(response.status_code, 200, 'status code do not match')

    @patch('service.get_by_id')
    def test_get_by_id(self, mock):
        with main.app.test_client() as c:
            mock.return_value = {"id": 1, "message":"dummy excuse"}
            response = c.get("/excuses/1")
            mock.assert_called_once_with(1)

    @patch('service.delete_by_id')
    def test_delete_200(self, mock):
        with main.app.test_client() as c:
            response = c.delete("/excuses/1")
            self.assertEqual(response.status_code, 200, 'status code do not match')

if __name__ == '__main__':
    unittest.main()
```
### Run Test
Shell:
```
python -m unittest
```