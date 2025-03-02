import pickle
seznam = [1,2,3,4,5]

pickle_data = pickle.dumps(seznam)

print("serializovaný Pickle:" , pickle_data)

nacteny_seznam = pickle.loads(pickle_data)
print("Načteny seznam:", nacteny_seznam)