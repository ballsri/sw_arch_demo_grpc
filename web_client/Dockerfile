FROM node:16.13.0-slim


ARG REACT_APP_BACKEND_API

ENV REACT_APP_BACKEND_API=$REACT_APP_BACKEND_API

ADD . /home/web

WORKDIR /home/web

ENV TZ=Asia/Bangkok
ENV PORT=80

RUN apt-get update && apt-get install -y curl

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ >/etc/timezone

RUN yarn install

RUN yarn run build

RUN yarn global add serve

EXPOSE 80

CMD serve -s build
