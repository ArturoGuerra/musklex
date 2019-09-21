FROM python:3-buster

WORKDIR /app
RUN apt update && apt install -y ffmpeg libffi-dev

COPY Pipfile* /tmp/
RUN pip install pipenv
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . .

CMD ["python", "./main.py"]
