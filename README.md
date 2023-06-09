# Backend Rest

## Requisitos

El proyecto está configurado para correr en un entorno de desarrollo con Docker Engine. Para fácil instalación, se recomienda utilizar un OS Linux.

- [Pasos de instalación de Docker Engine en Linux](https://docs.docker.com/engine/install/)

**No se recomienda utilizar Docker Desktop sino Docker Engine.**

## Instrucciones de ejecución

1. Clonar el repositorio

```bash
git clone https://github.com/SmartCode2023/user-service.git
```

2. Crear el archivo .env con las variables de entorno (Modificar según sea necesario)

```bash
cp .env.example .env
```

3. Construir la imagen de Docker

```bash
docker compose build
```

4. Ejecutar los contenedores

```bash
docker compose up -d
```

El proyecto está configurado para correr en 
http://localhost:8100.

Para ver los logs de los contenedores

```bash
docker compose logs -f
```

Para detener los contenedores

```bash
docker compose down
```

Para detener los contenedores y eliminar los volúmenes **ATENCIÓN: Esto eliminará la base de datos**

```bash
docker compose down --volumes
```
