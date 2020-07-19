FROM ubuntu:latest
MAINTAINER alfred.kim

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y python3.8
RUN mkdir /src
COPY hanoi_tower.py /src/hanoi_tower.py
ENV NUM_DISK 3
WORKDIR /src
CMD python3.8 hanoi_tower.py ${NUM_DISK}
