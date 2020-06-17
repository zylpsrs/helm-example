FROM registry.cn-hangzhou.aliyuncs.com/zylpsrs/example/python-builder

USER root
COPY app.py /tmp/src/
COPY requirements.txt /tmp/src/
RUN chown -R 1001:0 /tmp/src

USER 1001
ENV PORT 9080
RUN /usr/libexec/s2i/assemble
CMD /usr/libexec/s2i/run
