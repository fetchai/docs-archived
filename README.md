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

Then run `make new_env`. This creates a new pipenv virtual environments and installs the required dependencies.

Then `pipenv shell` to enter the pipenv virtual environment.

Then run `mkdocs serve` and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

If you run in `--strict` mode, you will receive warnings about any broken links.

## Making changes

- For docs in submodules (i.e. `aea`) open a PR against the relevant repo (`develop` branch) and wait until the changes hit `master`. Then deploy.

- For docs on the `docs` repo, make changes directly and open a PR against `master` branch of the docs repo. Then deploy.

## Previews and Staging

- Any changes made to a PR will generate an ephemeral preview site on firebase, which will disappear after a couple of days.
The URL of this temporary site will be added to the PR's conversation.

- Any changes pushed to the `staging` branch will be deployed to the [preview](https://fetch-docs-preview.web.app/) website, and will not expire.

## Deployment

Request the `deploy.sh` script from a maintainer and run it.
