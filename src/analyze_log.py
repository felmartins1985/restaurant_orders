import csv


def set_dict(data, name_person):
    order_name = {}
    for name, food, day in data:
        if name == name_person:
            if food not in order_name:
                order_name[food] = 1
            else:
                order_name[food] += 1
    return order_name


def find_number_first_food(data, name_person):
    order_name = set_dict(data, name_person)
    # print(order_name)
    most_order_name_amount = 0
    most_order_name_food = str()
    for key, value in order_name.items():
        if value > most_order_name_amount:
            most_order_name_amount = value
            most_order_name_food = key
    print(most_order_name_food)
    return most_order_name_food


def find_foods_set(data, name_person):
    all_foods = set()
    all_foods_person = set()
    for name, food, _ in data:
        all_foods.add(food)
        if name == name_person:
            all_foods_person.add(food)
    return all_foods.difference(all_foods_person)


def find_days_never_go(data, name_person):
    all_days = set()
    all_days_person = set()
    for name, _, day in data:
        all_days.add(day)
        if name == name_person:
            all_days_person.add(day)
    return all_days.difference(all_days_person)


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file, encoding="utf-8") as file:
            inventory = list(csv.reader(file, delimiter=",", quotechar='"'))
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
    else:
        maria_eats = find_number_first_food(inventory, "maria")
        arnaldo_hamburger = set_dict(inventory, "arnaldo")["hamburguer"]
        joao_never_ordered = find_foods_set(inventory, "joao")
        joao_never_restaurant = find_days_never_go(inventory, "joao")
        with open("data/mkt_campaign.txt", mode="w") as file:
            file.write(
                "".join(
                    [
                        f"{maria_eats}\n{arnaldo_hamburger}\n",
                        f"{joao_never_ordered}\n{joao_never_restaurant}\n",
                    ]
                )
            )


if __name__ == "__main__":
    analyze_log("data/orders_1.csv")
