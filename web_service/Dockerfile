FROM node:23-slim as build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# Этап продакшн-сервера
FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html

# Опционально: замени конфиг nginx, если нужно
# COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]