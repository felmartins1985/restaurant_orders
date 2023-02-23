class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self.stock = {
            "pao": 0,
            "carne": 0,
            "queijo": 0,
            "molho": 0,
            "presunto": 0,
            "massa": 0,
            "frango": 0,
        }

    def add_new_order(self, customer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if self.stock[ingredient] < self.MINIMUM_INVENTORY[ingredient]:
                self.stock[ingredient] += 1
            else:
                return False

    def get_quantities_to_buy(self):
        return self.stock

    def get_available_dishes(self):
        available_dishes = set()
        for dish, ingredients in self.INGREDIENTS.items():
            count_ingredient = 0
            for ingredient in ingredients:
                if self.stock[ingredient] < self.MINIMUM_INVENTORY[ingredient]:
                    count_ingredient += 1
            if count_ingredient == len(ingredients):
                available_dishes.add(dish)
        return available_dishes
    
    
if __name__ == "__main__":
    track_orders = TrackOrders()

    orders = [
        ["jorge", "frango", "domingo"],
        ["maria", "frango", "segunda-feira"],
        ["arnaldo", "peixe", "sábado"],
        ["maria", "carne", "terça-feira"],
        ["joao", "salada", "segunda-feira"],
    ]

    for name, dish, day in orders:
        print(f'Adicionando pedido: {name, dish, day}')
        track_orders.add_new_order(name, dish, day)

    print(
        'Prato mais pedido por Maria:',
        track_orders.get_most_ordered_dish_per_customer("maria"),
    )
    print(
        'Prato nunca pedido por João:',
        track_orders.get_never_ordered_per_customer("joao"),
    )
    print(
        'Dia(s) que João nunca visitou:',
        track_orders.get_days_never_visited_per_customer("joao"),
    )
    print(
        'Dia de maior movimento:',
        track_orders.get_busiest_day(),
    )
    print(
        'Dia de menor movimento:',
        track_orders.get_least_busy_day(),
    )
