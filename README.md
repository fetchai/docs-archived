![GitHub contributors](https://img.shields.io/github/contributors-anon/fetchai/docs)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/fetchai/docs)
<a href="https://github.com/fetchai/docs/workflows/Docs%20sanity%20checks%20and%20tests">
<img alt="Docs sanity checks and tests" src="https://github.com/fetchai/docs/workflows/Docs%20sanity%20checks%20and%20tests/badge.svg?branch=master"></a>

### Clone

This repository contains submodules. Clone with recursive strategy:

    git clone https://github.com/fetchai/docs.git --recursive && cd docs

### Retrieve submodules

Ensure you retrieve all the submodules by running:

    git submodule update --init --recursive

### Update submodules

To update all your submodules to the latest versions of the main branch in their respective remote repos:

    git submodule update --remote

## To build the documentation locally

To compile and build the documentation site locally, download and install pipenv. Instructions are <a href="https://github.com/pypa/pipenv#installation" target=_blank>here</a>.

Then run `make new_env`. This creates a new pipenv virtual environments and installs the required dependencies.

Then `pipenv shell` to enter the pipenv virtual environment.

Then run `mkdocs serve` and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

If you run in `--strict` mode, you will receive warnings about any broken links.

## Making changes

- For docs in submodules (e.g. `aea`) open a PR against the relevant repo (`develop` branch) and wait until the changes hit `master`. Then in this repo, open a PR containing an update to the aea submodule (see [update submodule](#update-submodules) above).

- For docs on the `docs` repo, make changes directly and open a PR against `master` branch of the docs repo.

## Previews and Staging

- Any changes made to a PR will generate an ephemeral preview site on firebase, which will disappear after a couple of days.
The URL of this temporary site will be added to the PR's conversation.

- Any changes pushed to the `staging` branch will be deployed to the [preview](https://fetch-docs-preview.web.app/) website, and will not expire.

## Deployment

Request the `deploy.sh` script from a maintainer and run it.
