FROM python:3.6.3

pip install --upgrade pip setuptools

ADD . /app
WORKDIR /app
RUN pip install -e .

CMD ['pserve', 'ini/development.ini', '--reload']