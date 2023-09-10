#docker build -t scavengerhunt .
#docker run -dit -p 5999:80 scavengerhunt:latest
FROM nginx:alpine3.18-slim

WORKDIR /usr/share/nginx/html
COPY chall/ .

EXPOSE 80