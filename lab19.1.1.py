import random
import pickle

def generate_random_ukrainian_chars(N):

    ukrainian_alphabet = [
        'А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 
        'И', 'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 
        'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 
        'Ь', 'Ю', 'Я'
    ]
    return [random.choice(ukrainian_alphabet) for _ in range(N)]

def write_list_to_binary_file(data):
    with open('ukrainian_chars.bin', 'wb',) as f:
        pickle.dump(data, f)

if __name__ == "__main__":
    N = int(input("Введіть кількість випадкових символів (N): "))
    random_chars = generate_random_ukrainian_chars(N)
    write_list_to_binary_file(random_chars)
    print("Список випадкових символів записано у файл ukrainian_chars.bin.")