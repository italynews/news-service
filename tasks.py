from ansa.ansa import Ansa
from ansa.constant import HOMEPAGE
from ansa.constant import CATEGORIES

class Tasks():

    def flatten(self,list):
        for i in list:
            for j in i:
                yield j

    def fetch_and_store_news(self):
        obj = Ansa()
        listArticles = []
        for n in CATEGORIES:
            listArticles.append(obj.get_articles(n)) 
        listArticles = self.flatten(listArticles)
        return listArticles

    