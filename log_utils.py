from random import randint


def log(function):
    """A decorator that outputs the function name and execution time"""

    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
        print(f"{function.__name__} – {randint(0, 60)}c!")

    return wrapper


def log_bonus(pattern):
    """A decorator accepts a template that the time is substituted into."""

    def decorator(function):
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            print(pattern.format(randint(0, 60)))

        return wrapper

    return decorator


if __name__ == "__main__":

    @log_bonus("🛵 Доставили за {}с!")
    def bake():
        print("baking...")

    bake()
