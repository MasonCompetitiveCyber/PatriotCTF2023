FROM python

LABEL maintainer="sauman"

LABEL name="sauman"

RUN apt update -y \
    && pip3 install flask  \
    && apt install supervisor -y

# Setup app
RUN mkdir -p /app

# Switch working environment
WORKDIR /app

# COPY challenge
COPY challenge .

# Setup supervisor
COPY config/supervisord.conf /etc/supervisord.conf

# Changing Ownership
RUN chown -R www-data: /app

# Expose port the server is reachable on
EXPOSE 9099

# Disable pycache
ENV PYTHONDONTWRITEBYTECODE=1

# Run supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
