import requests
import json
from flask import Flask,render_template
import jinja2

app = Flask(__name__)
@app.route("/student.html")
def home():

    result = requests.get("http://staging.bldt.ca/api/method/build_it.test.get_students")
    data = result.text
    data = json.loads((data))
    context ={}
    context['title'] = "Students Details"
    context['data'] = data['data']

    return render_template("student.html",**context)

app.run(debug=True)
