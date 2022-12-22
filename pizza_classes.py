class Pizza:
    """Base class of pizza

    size - L or XL
    kwargs - ingredients of pizza
    """

    def __init__(self, size, **kwargs):
        if size not in ("L", "XL"):
            raise TypeError("Only L and XL sizes are available")
        self.name = "Pizza"
        self.size = size
        self.sauce = kwargs["sauce"]
        self.cheese = kwargs["cheese"]
        self.ingredients = list(kwargs.values())

    def dict(self) -> dict:
        return {"Recipe": self.ingredients}

    def __eq__(self, other) -> bool:
        return (
            set(self.ingredients) == set(other.ingredients)
            and self.size == other.size
        )


class Margherita(Pizza):
    """Margherita pizza inherited from Pizza class"""

    def __init__(self, size):
        super().__init__(
            size,
            sauce="tomato sauce",
            cheese="mozzarella",
            toppings="tomatoes"
        )
        self.name = "Margherita"


class Pepperoni(Pizza):
    """Pepperoni pizza inherited from Pizza class"""

    def __init__(self, size):
        super().__init__(
            size,
            sauce="tomato sauce",
            cheese="mozzarella",
            toppings="pepperoni"
        )
        self.name = "Pepperoni"


class Hawaiian(Pizza):
    """Hawaiian pizza inherited from Pizza class"""

    def __init__(self, size):
        super().__init__(
            size,
            sauce="tomato sauce",
            cheese="mozzarella",
            toppings_1="chicken",
            toppings_2="pineapples",
        )
        self.name = "Hawaiian"


if __name__ == "__main__":
    m_l = Margherita("L")
    m_xl = Margherita("XL")

    print(m_l == m_xl)
    print(m_l.dict())
