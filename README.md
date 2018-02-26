# BeerReviews
BeerReviews is a website that let you make beer reviews, and see the best beers from around the world !

Check the specifications here !
https://docs.google.com/document/d/1cmlz5GmnrAaOqnjyCHOZkS_mgMEQBeXUotX54O-hQQM/edit#

### Deployment : 

```shell
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Loading placeholders : 
```
python manage.py loaddata path/to/fixtures.json
```
