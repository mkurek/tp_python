```
virtualenv tp_python
cd tp_python
source bin/activate
pip install ipython pygments tornado jinja2 pyzmq
git clone https://github.com/mkurek/tp_python 
cd tp_python
ipython nbconvert --to=slides TP.ipynb --post serve --reveal-prefix=reveal.js
```
