# Dockerfile para el frontend React/Vite
FROM node:20-alpine

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias
COPY package.json yarn.lock ./

# Instalar dependencias
RUN yarn install --frozen-lockfile

# Copiar el código de la aplicación
COPY . .

# Exponer el puerto
EXPOSE 5173

# Comando para ejecutar la aplicación en modo desarrollo
CMD ["yarn", "dev", "--host", "0.0.0.0"]

