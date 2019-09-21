FROM python:3-buster

WORKDIR /app
RUN apt install -y cffi libffi-dev

COPY Pipfile* /tmp
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . .

CMD ["python", "./main.py"]
