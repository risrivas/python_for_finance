FROM ubuntu:latest

MAINTAINER rishi

ADD install_adv.sh /

RUN chmod u+x /install_adv.sh

RUN /install_adv.sh

ENV PATH /root/miniconda3/bin:$PATH

CMD ["ipython"]

