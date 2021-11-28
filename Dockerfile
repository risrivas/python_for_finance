FROM ubuntu:latest

MAINTAINER rishi

ADD install.sh /

RUN chmod u+x /install.sh

RUN /install.sh

ENV PATH /root/miniconda3/bin:$PATH

CMD ["ipython"]

