FROM idealista/jdk:8u212-stretch-openjdk-headless
LABEL maintainer="idealista <labs@idealista.com>"

RUN rm -rf /var/lib/apt/lists/* && apt-get update \
    && apt-get install -y sudo systemd systemd-sysv \
    && apt-get autoremove -y && apt-get clean

EXPOSE 2181 2888 3888

CMD ["/sbin/init"]