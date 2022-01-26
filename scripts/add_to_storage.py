from load_save import load, save, file_path

def add_to_storage(category, amount):
    """
    przyjmuje kategorie i ilosc
    pobiera, updatuje i zapisuje storage
    """
    storage = load(file_path.storage) # loaduje storage
    storage[category] = storage.get(category, 0) + amount # updatuje storage
    save(storage, file_path.storage) # savuje storage
