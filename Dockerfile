FROM python:3.9

RUN useradd --create-home userapi
WORKDIR /smartMeter

RUN pip install -U pipenv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --system
COPY ./ .
RUN chown -R userapi:userapi ./
USER userapi

EXPOSE 8080
CMD gunicorn --bind 0.0.0.0:8080 wsgi:app