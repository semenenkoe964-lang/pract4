from abc import ABC, abstractmethod
class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass
class Book():
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def info(self):
        return f"{self.title} ${self.author} ${self.year}"

    def print_info(self) :
        print(self.info())
    def __str__(self):
        return self.info()
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    @property
    def age(self):
        return self.CURRENT_YEAR - self.year

    @classmethod
    def from_string(cls, book_string: str):
        title, author, year_str = book_string.split(';')
        year = int(year_str.strip())
        return cls(title.strip(), author.strip(), year)
class EBook(Book):
    def __init__(self,title,author,year,format):
        super().__init__(title,author,year)
        self.format=format
    def info(self):
        return f"{self.title} ${self.author} ${self.year} ${self.format}"
