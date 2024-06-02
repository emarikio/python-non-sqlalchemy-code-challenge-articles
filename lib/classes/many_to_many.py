class Author:
    def _init_(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self.__name = name
        self.__articles = []

    
    def name(self):
        return self.__name

    def articles(self):
        return self.__articles

    def magazines(self):
        return list(set(article.magazine for article in self.__articles))

    def add_article(self, article):
        self.__articles.append(article)


class Magazine:
    def _init_(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        self.__name = name
        self.category = category
        self.__articles = []

    
    def name(self):
        return self.__name

   
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be of type str")
        if not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        self.__name = new_name

    def articles(self):
        return self.__articles

    def contributors(self):
        return list(set(article.author for article in self.__articles))

    def add_article(self, article):
        self.__articles.append(article)


class Article:
    def _init_(self, author, magazine):
        self.author = author
        self.magazine = magazine
        author.add_article(self)
        magazine.add_article(self)


author1 = Author()
author2 = Author()

magazine1 = Magazine()
magazine2 = Magazine()

article1 = Article()
article2 = Article()
article3 = Article()

print(f"Author: {author1.name}")
print(f"Author's Articles: {[article.magazine.name for article in author1.articles()]}")
print(f"Author's Magazines: {[mag.name for mag in author1.magazines()]}")

print(f"Magazine: {magazine1.name}")
print(f"Magazine's Articles: {[article.author.name for article in magazine1.articles()]}")
print(f"Magazine's Contributors: {[author.name for author in magazine1.contributors()]}")

magazine1.name = "Tech Innovations"
print(f"New Magazine Name: {magazine1.name}")
