class Book:
    """Модель книги для нашего проекта."""

    def __init__(
        self,
        title: str,
        description: str,
        list_count: int,
        price: float,
        rate_list: list[int]
    ) -> None:
        self.title = title
        self.description = description
        self.list_count = list_count
        self.price = price 
        self.rate_list = rate_list

    @property
    def rate(self) -> float:
        return sum(self.rate_list) / len(self.rate_list)
    
    def __eq__(self, sec__book: object) -> bool:

        return f"""{self.title == sec__book.title
        and self.description == sec__book.description
        and self.list_count == sec__book.list_count
        and self.price == sec__book.price
        and self.rate_list == sec__book.rate_list}"""
        
    
    def save() -> None:
        pass

    def delete() -> None:
        pass

    def update() -> None:
        pass


book1: Book = Book(
    'amir',
    'amir',
    10,
    10,
    [5,5]
)
book2: Book = Book(
    'rezvan',
    'rezvan',
    10,
    10,
    [5,5]
)
book3: Book = Book(
    'max',
    'max',
    10,
    10,
    [5,5]
)
