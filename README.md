# Roles

## Admin
- Can change configuration and behavior of the system.
- Can perform CRUD to all kind of projects.
- Can change state of projects.
- Can generate reports.
- Can review beneficiaries progress.

## Director
- Can perform CRUD to local projects.
- Can assign collaborators to projects tasks and beneficiaries tasks.
- Can generate reports.

## Collaborator
- Can register new beneficiaries to the system. 
- Can update his own account information. 
- Can sign in to active projects.
- Can leave old projects.
- Can drop ownership of tasks.
- Can review general information of beneficiaries.

## Beneficiary
- No access at all.

# Technology
- Vuejs
- Vuetify
- Django

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

DtVPSzRaF1IDVNnpcJwq