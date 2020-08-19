import random
from app import app
from flask import request
from app.models import Animals
# animals = [
#     "Apes",
#     "Bats",
#     "Bears",
#     "Bees",
#     "Birds",
#     "Camels",
#     "Cats",
#     "Cows",
#     "Chicks",
#     "Chickens"
# ]

# sounds = [
#     "Gibber",
#     "Screech",
#     "Growl",
#     "Buzz",
#     "Chirp",
#     "Grunt",
#     "Meow",
#     "Moo",
#     "Cheep",
#     "Cluck",
# ]

@app.route("/api/animal", methods=["GET"])
def get_animal():
    number = Animals.query.filter_by().all()
    randomno = random.randint(0, len(number)-1)
    overall = Animals.query.filter_by(id=randomno).first()
    animal = overall.animal_name
    return str(animal)

@app.route("/api/animal/noise", methods=["GET", "POST"])
def get_noise():
    # x = 0
    response = request.data.decode("utf-8")

    overall = Animals.query.filter_by(animal_name = response).first()
    noise = overall.animal_noise
    # for i in animals:
    #     if i == response:
    #         noise = sounds[x]
    #         break
    #     else:
    #         x += 1
    return str(noise)
