import pickle

def read_list_from_binary_file():
    with open('ukrainian_chars.bin', 'rb') as f:
        return pickle.load(f)

if __name__ == "__main__":
    random_chars = read_list_from_binary_file()
    print("Вміст списку з файлу ukrainian_chars.bin:")
    print(' '.join(random_chars))