FROM ubuntu:16.04

RUN apt-get update
RUN apt-get upgrade
RUN apt-get -y install python3 build-essential python3-pip python3-wheel libzmq3-dev libgdal-dev
RUN pip3 install --upgrade pip
RUN apt-get install -y python-numpy python-matplotlib python-scipy python-sklearn
RUN apt-get install -y git nano




RUN apt-get update && apt-get install -y \
	nano
  	git
	wget
	bzip2

RUN git clone https://github.com/ccivit/yolo_docker.git

WORKDIR /yolo_docker

#RUN wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
#RUN md5sum Miniconda3-latest-Linux-armv7l.sh
#RUN bash Miniconda3-latest-Linux-armv7l.sh
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O Miniconda.sh && \
	/bin/bash Miniconda.sh -b -p /opt/conda && \
	rm Miniconda.sh

ENV PATH /opt/conda/bin:$PATH

RUN conda create -y -n jupyter_env python=3.6 anaconda && \
        /opt/conda/envs/jupyter_env/bin/pip install tensorflow --upgrade pip opencv-python


RUN echo "source activate jupyter_env" > ~/.bashrc
#RUN ~/.bashrc
