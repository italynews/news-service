from flask import Flask
from ansa.ansa import Ansa
from ansa.constant import HOMEPAGE
from flask import request
import json
from flask import jsonify
app = Flask(__name__)
base_url = "http://127.0.0.1:5000/api/news/"
ansa = Ansa()

@app.route("/api/news/<string:category>")
def get_all_articles(category):
    search_title = request.args.get('search', None)
    if search_title is None:
        articles = ansa.get_articles_by_category(category)
        return jsonify(articles)
    else:
        articles = ansa.get_articles_by_category(category)
        filtered_list = []
        for article in articles:
            if search_title.lower() in article['title_detail']['value'].lower():
                filtered_list.append(article)
    return jsonify(filtered_list)


@app.route("/api/news/<string:category>/<path:article>")
def read_article(category, article):
    print('article is')
    print(article)
    print('-------------')
    return jsonify(ansa.read_article(article))


@app.route('/')
def index():
    categories_list = []
    for category in ansa.get_categories_list():
        categories_list.append(base_url+category)
    return jsonify(categories_list)


if __name__ == "__main__":
    app.run()
