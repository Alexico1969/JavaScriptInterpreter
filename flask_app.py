
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import pyduktape


app = Flask(__name__)

@app.route('/',  methods=['GET', 'POST'])
def home():
    input = ""
    output = ""

    if request.method == 'POST':
        input = request.form.get("input")
        js_input = input + 'output'
        context = pyduktape.DuktapeContext()
        try:
            output = context.eval_js(js_input)
        except:
            output = "There is an error in the code"
        print(output)

    return render_template("home.html", input = input, output = output)
