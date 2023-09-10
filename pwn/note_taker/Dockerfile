FROM ubuntu AS app
RUN apt update && \
    apt -y install qemu-user qemu-user-binfmt libc6-armel-cross gcc-aarch64-linux-gnu && \
    rm -rf /var/lib/apt/lists/*

COPY note_keeper.c /
RUN /usr/bin/aarch64-linux-gnu-gcc /note_keeper.c -o /note_keeper_arm
FROM pwn.red/jail
COPY --from=app / /srv

ENV JAIL_TIME=60
ENV JAIL_CONNS_PER_IP=10
ENV JAIL_PORT=5001

COPY note_keeper.c /srv/app/
COPY run_challenge.sh /srv/app/run
COPY flag.txt /srv/app
RUN mv /srv/note_keeper_arm /srv/app/note_keeper_arm