from flask import Flask, Response
from pydantic import BaseModel
import sys
from pathlib import Path
import time

api = Path(__file__).parent
root = api.parent

sys.path.append(str(root) )

from mock_package.compliance import msg
# msg = "LOCAL MSG"

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

class MyPydanticObject(BaseModel):
    field1: int
    field2: str

@app.route('/about')
def about():
    time.sleep(3)
    my_obj = MyPydanticObject(field1=123, field2=f"{msg}")
    json_data = my_obj.model_dump_json() # Use .json() for Pydantic V1
    return Response(json_data, mimetype='application/json')
