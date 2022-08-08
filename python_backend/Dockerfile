FROM python:3.10

WORKDIR /fastapi_backend

ADD . /fastapi_backend

RUN pip install pipenv

RUN rm Pipfile.lock

RUN pipenv install --skip-lock

RUN pipenv install gunicorn --skip-lock

WORKDIR /fastapi_backend

CMD ["pipenv", "run", "gunicorn", "run:app", "--bind", "0.0.0.0:8000", "--worker-class", "uvicorn.workers.UvicornWorker"]