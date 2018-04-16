# BeerReviews
BeerReviews is a website that let you make beer reviews, and see the best beers from around the world !

Specifications available in the wiki !

PowerPoint available in documents !

### Deployment : 

```shell
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Loading placeholders : 
```
python manage.py loaddata maker
python manage.py loaddata style
python manage.py loaddata user
python manage.py loaddata beer
python manage.py loaddata review
```
