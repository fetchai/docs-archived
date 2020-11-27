![GitHub contributors](https://img.shields.io/github/contributors-anon/fetchai/docs)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/fetchai/docs)
<a href="https://github.com/fetchai/docs/workflows/Docs%20sanity%20checks%20and%20tests">
<img alt="Docs sanity checks and tests" src="https://github.com/fetchai/docs/workflows/Docs%20sanity%20checks%20and%20tests/badge.svg?branch=master">

## Instructions for building the documentation locally

To compile and build the documentation site locally, download and install mkdocs. Instructions are <a href="https://www.mkdocs.org/#installation" target=_blank>here</a>.

You will need the PymDown extensions. Install with `pip install pymdown-extensions`. For more information on the PymDown extensions, go <a href="https://squidfunk.github.io/mkdocs-material/extensions/pymdown/" target=_blank>here</a>.

Then, clone the version of the docs you are interested in, `cd` to the `docs` root, and run `mkdocs build`, then `mkdocs serve`. 

If you run in `--strict` mode, you will receive warnings about any broken links.

Have fun.