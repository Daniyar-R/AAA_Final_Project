import click
from random import randint
from pizza_classes import Margherita, Pepperoni, Hawaiian


@click.group()
def cli():
    pass


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    print(f"👨‍🍳 Приготовили {pizza} за {randint(0, 60)}с!")
    if delivery:
        print(f"🛵 Доставили {pizza} за {randint(0, 60)}с!")


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
