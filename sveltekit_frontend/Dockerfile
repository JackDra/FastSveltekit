FROM node:latest

WORKDIR /svelte_frontend

COPY ./src src
COPY ./static static
COPY ./package-lock.json .
COPY ./package.json .
COPY ./svelte.config.js .
COPY ./playwright.config.ts .
COPY ./tsconfig.json .

RUN npm ci

RUN npm run build

CMD ["npm", "run", "preview"]