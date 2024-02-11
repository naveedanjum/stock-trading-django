# Run Migrations

```
python manage.py makemigrations
```

## Dockere for MySQL
```
docker run  --detach   --name stock_mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=stock_db -e MYSQL_USER=stock_user -e MYSQL_PASSWORD=stock_pass -d mysql
```
#### Connecting Locally
```
docker run -it --link stock_mysql:mysql --rm mysql sh -c "exec mysql -h\"$MYSQL_PORT_3306_TCP_ADDR\" -P\"$MYSQL_PORT_3306_TCP_PORT\" -uroot -p\"$MYSQL_ENV_MYSQL_ROOT_PASSWORD\""
```