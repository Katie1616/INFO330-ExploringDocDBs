import pymongo

mongoClient = pymongo.MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemon']
pokemonColl = pokemonDB['pokemon_data']

# Query 1: query that returns all the Pokemon named "Pikachu". 
print("Pokemon with the name \" Pikachu \"")
pikachu = pokemonColl.find({"name": "Pikachu"})
for p in pikachu:
    print(p)
print()

# Query 2: query that returns all the Pokemon with an attack greater than 150.
print("Pokemon greater than 150")
greaterThan150 = pokemonColl.find({"attack": {"$gt": 150}})
for greater in greaterThan150:
    print(greater)
print()

# Query 3: query that returns all the Pokemon with an ability of "Overgrow"
print("Pokemon with \"Overgrow\" ability")
overgrow = pokemonColl.find({"abilities": {"$regex": "Overgrow"}})
for o in overgrow:
    print(o)
print()
