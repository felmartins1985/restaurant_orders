from src.analyze_log import (
    find_number_first_food,
    find_foods_set,
    find_days_never_go,
)


def set_dict_days(data):
    order_name_days = {}
    for _, _, day in data:
        if day not in order_name_days:
            order_name_days[day] = 1
        else:
            order_name_days[day] += 1
    return order_name_days


class TrackOrders:
    def __init__(self):
        self.tracks = []

    def __len__(self):
        return len(self.tracks)

    def add_new_order(self, customer, order, day):
        self.tracks.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        return find_number_first_food(self.tracks, customer)

    def get_never_ordered_per_customer(self, customer):
        return find_foods_set(self.tracks, customer)

    def get_days_never_visited_per_customer(self, customer):
        return find_days_never_go(self.tracks, customer)

    def get_busiest_day(self):
        days = set_dict_days(self.tracks)
        most_days_amount = 0
        most_days_name = str()
        for key, value in days.items():
            if value > most_days_amount:
                most_days_amount = value
                most_days_name = key
        return most_days_name

    def get_least_busy_day(self):
        days = set_dict_days(self.tracks)
        worst_days_amount = 1000
        worst_days_name = str()
        for key, value in days.items():
            if value < worst_days_amount:
                worst_days_amount = value
                worst_days_name = key
        return worst_days_name
