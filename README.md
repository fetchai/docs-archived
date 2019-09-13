## Instructions for building the documentation locally

To compile and build the documentation site locally, run the follwoing steps:

1. Installing dependencies using pip & pipenv:
    >```
    >pip3 install pipenv
    >pipenv install
    >```

2. Build the html documentation:
    >```
    >pipenv run mkdocs build --strict
    >```
    , what will generate the html documentaion in `site` folder.


3. Use the documentation:
    Either Start the Web server with documentation locally:
    >```
    >pipenv run mkdocs serve
    >```
    , or directly open the `site/index.html` file in the browser.

Have fun.
