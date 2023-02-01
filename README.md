# url-shortener-on-steroids
 попытка написать очень мало бизнес-логики на гибкой архитектуре

# Run
### In terminal:
```
pip install poetry
poetry install
```
### In .env file:
```
DB_DSN=postgresql://user:password@localhost:5432/url_shortener
```
### Finallly: 
```
make db
make migrate head
make run
```
