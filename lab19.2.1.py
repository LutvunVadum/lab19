import pickle

def save_cars_to_binary_file(data):
    with open('cars.bin', 'wb') as file:
        pickle.dump(data, file)

if __name__ == "__main__":
    cars = {
        'Toyota Camry': 5,
        'Honda Accord': 3,
        'Ford Focus': 8,
        'Nissan Altima': 9,
        'Chevrolet Malibu': 4,
        'Kia Optima': 6,
        'Hyundai Sonata': 7,
        'Subaru Impreza': 1,
        'Volkswagen Jetta': 3,
        'Mazda 6': 2,
    }

    save_cars_to_binary_file(cars)
    print("Автомобільний словник збережено в cars.bin.")