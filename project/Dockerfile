FROM python:3.9

RUN apt update
RUN pip3 install --upgrade pip

RUN mkdir -p /home/project

WORKDIR /home/project

COPY ./project/requirements.txt /home/project/
RUN pip3 install -r requirements.txt

COPY ./project /home/project
