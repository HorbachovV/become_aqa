FROM python:3.11.3-buster

WORKDIR /test-framework

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "pytest", "." ]