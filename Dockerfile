FROM python:3.7
RUN pip3 install pipenv

WORKDIR /app
ADD Pipfile Pipfile.lock /app/
RUN pipenv install --system --deploy
RUN pipenv install importlib_metadata
RUN mkdir /app/site

ENTRYPOINT [ "mkdocs" ]
CMD ["build"]
