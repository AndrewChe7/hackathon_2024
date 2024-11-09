FROM node:latest

WORKDIR /usr/src/front
COPY package*.json ./
RUN npm install -r 

COPY . .

EXPOSE 5173