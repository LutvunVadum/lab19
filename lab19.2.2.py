import pickle

def read_cars_from_binary_file():
    with open('cars.bin', 'rb') as file:
        return pickle.load(file)

def find_two_models_with_smallest_quantity(data):
    sorted_cars = sorted(data.items(), key=lambda x: x[1])
    return sorted_cars[:2]

if __name__ == "__main__":
    cars = read_cars_from_binary_file()
    two_models = find_two_models_with_smallest_quantity(cars)
    
    print("Дві моделі автомобілів з найменшою кількістю:")
    for model, quantity in two_models:
        print(f"{model}: {quantity}")