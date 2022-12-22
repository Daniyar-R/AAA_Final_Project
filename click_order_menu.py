import click
from pizza_classes import Margherita, Pepperoni, Hawaiian
from log_utils import log_bonus


@click.group()
def cli():
    pass


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""

    @log_bonus("👨‍🍳 Приготовили за {}с!")
    def cook():
        print(f"Готовим {pizza}...")

    @log_bonus("🛵 Доставили за {}с!")
    def deliver():
        print(f"Доставляем {pizza}...")

    pizza_list = list(
        map(
            lambda x: x.lower(),
            [Margherita("L").name, Pepperoni("L").name, Hawaiian("L").name],
        )
    )

    if pizza.lower() not in pizza_list:
        raise TypeError("There is no such pizza")

    cook()

    if delivery:
        deliver()


@cli.command()
def menu():
    """Выводит меню"""
    print(f'– Margherita 🧀: {Margherita("L").ingredients}')
    print(f'– Pepperoni 🍕: {Pepperoni("L").ingredients}')
    print(f'– Hawaiian 🍍: {Hawaiian("L").ingredients}')


cli.add_command(order)
cli.add_command(menu)

if __name__ == "__main__":
    cli()
