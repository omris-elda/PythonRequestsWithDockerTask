import random
from app import app
from flask import request

animals = [
    "Apes",
    "Bats",
    "Bears",
    "Bees",
    "Birds",
    "Camels",
    "Cats",
    "Cows",
    "Chicks",
    "Chickens"
]

sounds = [
    "Gibber",
    "Screech",
    "Growl",
    "Buzz",
    "Chirp",
    "Grunt",
    "Meow",
    "Moo",
    "Cheep",
    "Cluck",
]

@app.route("/api/animal", methods=["GET"])
def get_animal():
    randomno = random.randint(0, len(animals)-1)
    animal = animals[randomno]
    return animal

@app.route("/api/animal/noise", methods=["GET", "POST"])
def get_noise():
    x = 0
    response = request.data.decode("utf-8")
    for i in animals:
        if i == response:
            noise = sounds[x]
            break
        else:
            x += 1
    return noise
