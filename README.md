## MySql Database

```
docker run -d \
    --name manos-bondadosas-db \
    -v $(pwd)/db:/var/lib/mysql \
    -p 3306:3306 \
    -e MYSQL_ROOT_PASSWORD="asd.123" \
    -e MYSQL_DATABASE="development" \
    -e MYSQL_USER="admin" \
    -e MYSQL_PASSWORD="asd.123" \
    mysql:latest
```

## Preguntas
1. ¿Deberían los colaboradores en general tener acceso a la información de los beneficiados?