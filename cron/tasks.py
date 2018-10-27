from huey import crontab
from .config import huey

from ansa.ansa import Ansa
from ansa.constant import HOMEPAGE
from ansa.constant import CATEGORIES

@huey.periodic_task(crontab(minute='*'))
def every_minute():

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
        print(listArticles)
        return listArticles

    def fetchNews():
        obj = Ansa()
        listArticles = []
        for n in CATEGORIES:
            listArticles.append(obj.get_articles(n)) 
        return self.flatten(listArticles)
    
    def putInDb():
        pass

    def delateOld():
        pass

    print(fetchNews())

    