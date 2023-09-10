FROM python:3-alpine

RUN mkdir -p /app

WORKDIR /app
COPY chall .
RUN mv flag.txt /flag.txt
RUN pip install -r requirements.txt

EXPOSE 80
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "80"]
