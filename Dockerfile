FROM ubuntu:18.04

RUN sudo apt-get update

RUN apt-get install --upgrade -y \
    python3 \
    python3-dev \
    python-pip \
    graphviz \
    libgraphviz-dev \
    pkg-config \
    libpq-dev

RUN pip install -r config/requirements.txt

COPY ./src/bookofmagnus .

CMD gunicorn bookofmagnus.wsgi --log-file -
