FROM python:3-slim

WORKDIR /usr/src/app

ENV DB_PASSWORD=root

COPY ./requirements.txt ./

RUN pip install -r ./requirements.txt

COPY ./app ./

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]