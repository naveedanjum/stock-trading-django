# Stock Trading Mock Application
This Stock Trading Mock Application is made to demonstrate the DJANGO DRF with Mock Data. Unit test, Integration tests are written and can be executed.
For more information please contact at anjum.farrukh@gmail.com

### For Documentation of API Endpoints
http://localhost:8000/api/docs

### For Standalone
Configure the Database Settings in settings.py
and execute
```
cd investment_site
```
```
pip install -r requirements.txt
```
```
python manage.py runserver
```

# OR

## Run Migrations
### To Run in Docker
```
cd investment_site
```
```
docker-compose up --build
```
#### In Order to run Test Cases (Unit Tests)
```
python manage.py test portfolio.tests.models_tests
```
#### In Order to run Test Cases (Integration API Tests)
```
python manage.py test portfolio.tests.api_tests
```

```
python manage.py makemigrations
```
### Generating the Fake Data For Stocks
```
python manage.py generate_fake_data --companies 40 --days 30
```

### For Documentation of API Endpoints
http://localhost:8000/api/docs

# If you want to use Docker Standalone MySQL
## Docker for MySQL
```
docker run  --detach   --name stock_mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=stock_db -e MYSQL_USER=stock_user -e MYSQL_PASSWORD=stock_pass -d mysql
```

#### Connecting Locally
```
docker run -it --link stock_mysql:mysql --rm mysql sh -c "exec mysql -h\"$MYSQL_PORT_3306_TCP_ADDR\" -P\"$MYSQL_PORT_3306_TCP_PORT\" -uroot -p\"$MYSQL_ENV_MYSQL_ROOT_PASSWORD\""
```