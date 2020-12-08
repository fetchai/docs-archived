![GitHub contributors](https://img.shields.io/github/contributors-anon/fetchai/docs)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/fetchai/docs)
<a href="https://github.com/fetchai/docs/workflows/Docs%20sanity%20checks%20and%20tests">
<img alt="Docs sanity checks and tests" src="https://github.com/fetchai/docs/workflows/Docs%20sanity%20checks%20and%20tests/badge.svg?branch=master"></a>

### Cloning

This repository contains submodules. Clone with recursive strategy:

    git clone https://github.com/fetchai/docs.git --recursive && cd docs


## Updating submodules

Ensure you have the latest submodules by running:

    git submodule update --init --recursive


## Instructions for building the documentation locally

To compile and build the documentation site locally, download and install pipenv. Instructions are <a href="https://github.com/pypa/pipenv#installation" target=_blank>here</a>.

Then run `pipenv --python 3.7 && pipenv shell`, followed by `pipenv install --skip-lock`.

Then run `mkdocs serve` and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

If you run in `--strict` mode, you will receive warnings about any broken links.

Have fun.


## Making changes

- For docs in submodules (i.e. `aea`) open a PR against the relevant repo (`develop` branch) and wait untill the changes hit `master`. Then deploy.

- For docs on `docs` repo make changes directly and open PR against `master` of docs repo. Then deploy.


## Deployment

Request the `deploy.sh` script from a maintainer and run it.
