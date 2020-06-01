# Start project

1. Build docker image and run:
First run:
```
docker-compose up --build
```
After builded:
```
docker-compose up
```
2. Visit:
[localhost:5000](localhost:5000)


# DB migrations
```
docker-compose exec app sh
flask db init
flask db migrate -m "add table"
flask db upgrade
```

# Screenshots
![Alt text](docs/1.png?raw=true "Start")
![Alt text](docs/todo.png?raw=true "Todo")

