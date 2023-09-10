# sudo docker build -t softshell .
# sudo docker run -p 8888:8888 softshell:latest

FROM ubuntu:18.04

RUN useradd -m ctf
WORKDIR /src
RUN apt update
RUN apt install gcc xinetd make cowsay -y

COPY ctf.xinetd /etc/xinetd.d/ctf
COPY Makefile /src
COPY flag.txt /
COPY softshell.c /src
COPY run.sh /src

RUN make

RUN chmod 444 /flag.txt
RUN chmod +x /src/run.sh
RUN sed -i -e 's/\r$//' /src/run.sh
RUN sed -i -e 's/\r$//' /etc/xinetd.d/ctf
RUN rm -rf /var/cache/apt/archives /var/lib/apt/lists/*

CMD ["/bin/bash", "/src/run.sh"]
EXPOSE 8888
