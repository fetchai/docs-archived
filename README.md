## Instructions for building the documentation locally

To compile and build the documentation site locally, download and install mkdocs. Instructions are <a href="https://www.mkdocs.org/#installation" target=_blank>here</a>.

You will need the material theme. You can install that with `pip install mkdocs-material`. For more information on the material theme, check out <a href="https://squidfunk.github.io/mkdocs-material/" target=_blank>their website</a>.

You will also need the PymDown extensions. Install with `pip install pymdown-extensions`. For more information on the PymDown extensions, go <a href="https://squidfunk.github.io/mkdocs-material/extensions/pymdown/" target=_blank>here</a>.

Then, clone the version of the docs you are interested in, `cd` to the `docs` root, and run `mkdocs build`, then `mkdocs serve`. 

If you run in `--strict` mode, you will receive warnings about any broken links.

Have fun.


##Building CSS

`python3 setup.py install`

`python3 setup.py build_sass`
