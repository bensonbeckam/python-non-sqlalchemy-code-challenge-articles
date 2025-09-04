class Article(object):
    all = []
    
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be of type Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be of type Magazine")
        if not isinstance(title, str):
            title = str(title)
        if len(title) < 5 or len(title) > 50:
            title = "Default Title"
        
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        # Silently fail for immutability
        pass

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            return  # Silently fail
        self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            return  # Silently fail
        self._magazine = value
        
class Author(object):
    def __init__(self, name):
        if not isinstance(name, str):
            name = str(name)
        if len(name) == 0:
            name = "Default Author"
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        # Silently fail for immutability
        pass

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set([magazine.category for magazine in self.magazines()]))

class Magazine(object):
    all = []
    
    def __init__(self, name, category):
        if not isinstance(name, str):
            name = str(name)
        if not 2 <= len(name) <= 16:
            name = name[:16] if len(name) > 16 else "Mag"
        if not isinstance(category, str):
            category = str(category)
        if len(category) == 0:
            category = "General"
            
        self._name = name
        self._category = category
        Magazine.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            return  # Silently fail
        if not 2 <= len(value) <= 16:
            return  # Silently fail
        self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            return  # Silently fail
        if len(value) == 0:
            return  # Silently fail
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        articles = self.articles()
        return [article.title for article in articles] if articles else None

    def contributing_authors(self):
        authors = [author for author in self.contributors() 
                  if len([article for article in self.articles() if article.author == author]) > 2]
        return authors if authors else None
    
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))