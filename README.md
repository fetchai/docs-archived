<a href="https://github.com/fetchai/docs/workflows/Docs%20sanity%20checks%20and%20tests">
<img alt="Docs sanity checks and tests" src="https://github.com/fetchai/docs/workflows/Docs%20sanity%20checks%20and%20tests/badge.svg?branch=master">
</a>

# Fetch.ai Developer Documentation

This repo contains documentation for public Fetch.ai products.

## Get started (building the documentation locally)

1. Create and launch a clean virtual environment with Python 3.7 (any Python `>=` 3.6 works):

       pipenv --python 3.7 && pipenv shell

2. Install dependencies:

       pipenv install --skip-lock

3. Run:

       mkdocs serve

Then navigate to `http://127.0.0.1:8000` in your browser.

If you run in `--strict` mode, you will receive warnings about any broken links.

Have fun.


## Extras:

For building CSS run:

`python3 setup.py install`

`python3 setup.py build_sass`
