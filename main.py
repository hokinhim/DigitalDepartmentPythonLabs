class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Pages must be an integer")
        if value <= 0:
            raise ValueError("Pages must be a positive integer")
        self._pages = value

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Страниц: {self.pages}"

    # __repr__ is inherited


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float):
            raise ValueError("Duration must be a float")
        if value <= 0:
            raise ValueError("Duration must be a positive float")
        self._duration = value

    def __str__(self):
        return f"Аудио книга {self.name}. Автор {self.author}. Продолжительность: {self.duration} часов"

    # __repr__ is inherited, but you can override it if needed


if __name__ == "__main__":
    # Creating instances of PaperBook and AudioBook
    paper_book = PaperBook(name="The Great Gatsby", author="F. Scott Fitzgerald", pages=180)
    audio_book = AudioBook(name="1984", author="George Orwell", duration=10.5)

    # Attempting to modify read-only properties will result in an AttributeError
    # paper_book.name = "New Title"  # Raises AttributeError
    # audio_book.author = "New Author"  # Raises AttributeError

    # Attempting to set invalid values for pages or duration will raise a ValueError
    # paper_book.pages = "invalid"  # Raises ValueError
    # audio_book.duration = -5  # Raises ValueError

    # Displaying the string representation of the objects
    print(paper_book)
    print(audio_book)
