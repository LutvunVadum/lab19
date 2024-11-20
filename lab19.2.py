import shelve

def save_cars_to_shelve(cars):
    with shelve.open('cars_shelve') as shelf:
        for model, quantity in cars.items():
            shelf[model] = quantity

def read_cars_from_shelve():
    with shelve.open('cars_shelve') as shelf:
        return dict(shelf)

def find_two_models_with_smallest_quantity(data):
    sorted_cars = sorted(data.items(), key=lambda x: x[1])
    return sorted_cars[:2]

if __name__ == "__main__":
    cars_data = {
        'Model A': 10,
        'Model B': 5,
        'Model C': 8,
        'Model D': 2,
        'Model E': 7,
        'Model F': 4,
        'Model G': 6,
        'Model H': 1,
        'Model I': 3,
        'Model J': 9
    }

    save_cars_to_shelve(cars_data)

    cars = read_cars_from_shelve()
    two_models = find_two_models_with_smallest_quantity(cars)
    
    print("Дві моделі автомобілів з найменшою кількістю:")
    for model, quantity in two_models:
        print(f"{model}: {quantity}")