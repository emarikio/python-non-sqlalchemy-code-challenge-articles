class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        self._article = []

    def name(self):
        return self._name

    def articles(self):
        return self._articles
        pass

    def magazines(self):
        return list(set(article.magazine for article in self._articles))
        pass

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article
        pass

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))
        pass
        
class Magazine:
    def __init__(self, name, category):
        if not isinstance(category, str) or not 2 <= len(name) <= 16:
            raise ValueError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._name = name
        self._category = category
        self._articles = []

    def name(self):
        return self._name
    
    def name(self, value):
        if not isinstance(value, str) or not 2 <= len(value) <= 16:
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    def category(self):
        return self._category
    
    def category(self, value):
        if not isinstance(value, str) or not 2 <= len(value) <= 16:
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._category = value


    def articles(self):
        return self._articles
        pass

    def contributors(self):
        return list(set(article.author for article in self._articles))
        pass

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

        pass

    def contributing_authors(self):
        if not self._articles:
            return None
        author_count = {}
        for article in self._articles:
            if article.author in author_count:
                author_count[article.author] += 1
            else:
                author_count[article.author] = 1
        return [author for author, count in author_count.items() if count > 2]
        pass

