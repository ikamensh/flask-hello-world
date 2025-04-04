from flask import Flask, Response, request
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
    # We are supposed to get arguments like this:
    # page = request.args.get('page', default=1, type=int)
    # filter = request.args.get('filter', default='*', type=str)

    my_obj = MyPydanticObject(field1=123, field2=f"{msg}")
    json_data = my_obj.model_dump_json() # Use .json() for Pydantic V1
    return Response(json_data, mimetype='application/json')
