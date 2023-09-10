# sudo docker build -t flagfinder .
# sudo docker run -d -p 4757:4757 flagfinder:latest

FROM ubuntu:18.04

RUN useradd -m ctf
WORKDIR /src
RUN apt update
RUN apt install gcc xinetd make -y

COPY ctf.xinetd /etc/xinetd.d/ctf
COPY Makefile /src
COPY flagfinder.c /src
COPY run.sh /src

RUN make

RUN chmod +x /src/run.sh
RUN sed -i -e 's/\r$//' /src/run.sh
RUN sed -i -e 's/\r$//' /etc/xinetd.d/ctf
RUN rm -rf /var/cache/apt/archives /var/lib/apt/lists/*

CMD ["/bin/bash", "/src/run.sh"]
EXPOSE 4757
