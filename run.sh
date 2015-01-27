#!/bin/bash
ipython nbconvert --to=slides TP.ipynb --post serve --reveal-prefix=reveal.js
