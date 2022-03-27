FROM alpine:latest

RUN apk add --update py3-pip
RUN apk add --update npm

RUN mkdir -p /app

ADD $pwd /app

RUN cd /app; pip install pipenv && \
    pipenv install --system && \
    cd /app/frontend; npm install; npm run build

WORKDIR /app

EXPOSE 5000
ENV PORT 5000
#ENV CLOUD_STORAGE ""

RUN rm -rf /app/frontend/node_modules

CMD ["honcho", "start"]
