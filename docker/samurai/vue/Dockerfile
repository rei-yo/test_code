FROM node:18

RUN mkdir app
COPY ./vue_pj ./app
WORKDIR /app/vue_pj
RUN npm install -g npm

EXPOSE 3000
ENV HOST 0.0.0.0