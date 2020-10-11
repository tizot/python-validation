class String:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner=None):
        print(f"Getting field {self.name}")
        if instance is None:
            return self
        else:
            # raise ValueError()
            return instance.__dict__["__" + self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"Attribute '{self.name}' must be a string")
        instance.__dict__["__" + self.name] = value


class Book:
    title = String('title')

    def __init__(self, title):
        self.title = title


book = Book(title="Python Essential Reference")
print(book.title)  # implicitly calls Book.title.__get__(book)
book.title = "Python Cookbook"  # implicitly calls Book.title.__set__(book, "Python Cookbook")
print(book.title)
