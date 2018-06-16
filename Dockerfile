FROM alpine

RUN mkdir -p /opt/resources && \
  apk add --no-cache python3 && \
  pip3 install stashy

ADD check.py /opt/resource/check
ADD in.py /opt/resource/in
ADD out.py /opt/resource/out
