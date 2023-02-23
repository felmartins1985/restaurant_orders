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
    inventory = InventoryControl()
    inventory.add_new_order("jorge", "hamburguer", "terça-feira")
    inventory.add_new_order("maria", "pizza", "terça-feira")

    print(
        'Quantidade de ingredientes para comprar:',
        inventory.get_quantities_to_buy(),
    )

    print(
        'Pratos disponíveis no cardápio:',
        inventory.get_available_dishes(),
    )
