from flask import Flask
from ansa.ansa import Ansa
from ansa.constant import HOMEPAGE
from flask import request
import json 

app = Flask(__name__)

obj1 = Ansa()

@app.route("/api/news/<string:category>")
def get_all_articles(category):
    data = request.args.get('find', None)
    if data is None:
        articles = obj1.get_articles(category)
        return json.dumps(articles)
    else:
        articles = obj1.get_articles(category)
        listSearch = []
        for article in articles:
            if data.lower() in article['title_detail']['value'].lower():
                listSearch.append(article)
    return json.dumps(listSearch)
            
@app.route("/api/news/<string:category>/get_all_titles")
def get_all_titles_by_category(category):
    articles = obj1.get_articles(category)
    listTitles = []
    for article in articles:
        listTitles.append(article['title'])
    return json.dumps(listTitles)

@app.route("/api/news/<string:category>/<int:value>/get_title")
def get_title_to_category(category,value):
    articles = obj1.get_articles(category)
    return articles[value]['title']

@app.route("/api/news/<string:category>/get_all_descriptions")
def get_all_description_by_category(category):
    articles = obj1.get_articles(category)
    listTitles = []
    for article in articles:
        listTitles.append(article['description'])
    return json.dumps(listTitles)

@app.route("/api/news/<string:category>/<int:value>/get_description")
def get_description_to_category(category,value):
    articles = obj1.get_articles(category)
    return articles[value]['description']

@app.route("/api/news/<string:category>/get_all_date")
def get_all_date_by_category(category):
    articles = obj1.get_articles(category)
    listTitles = []
    for article in articles:
        listTitles.append(article['published'])
    return json.dumps(listTitles)

@app.route("/api/news/<string:category>/<int:value>/get_date")
def get_date_to_category(category,value):
    articles = obj1.get_articles(category)
    site = request.url
    if value in articles:
        return articles[value]['published']
    else:
        return ("errore 500! Valore troppo alto.")
    

@app.route('/')
def index():
    return "Benvenuto nella home"

if __name__ == "__main__":
    app.run()