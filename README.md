# JavaScriptInterpreter
Test site to demonstrate how we could implement a JavaScript interpreter into the CodeWizards' Code Challenge

It uses Flask and pyduktape 0.0.6 : https://pypi.org/project/pyduktape/

Installing PyDuktape : 

$ pip install -U setuptools
$ pip install pyduktape

or

$ git clone https://github.com/stefano/pyduktape.git
$ cd pyduktape
$ pip install -U setuptools
$ python setup.py install

then

You can use it in any Python environment as :

import pyduktape

context = pyduktape.DuktapeContext()
context.eval_js("print('Hello, world!');")
