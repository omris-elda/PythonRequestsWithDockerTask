from app import db
from app.models import Animals

db.drop_all()
db.create_all()

ape = Animals(animal_name = "Apes", animal_noise = "Gibber")
bat = Animals(animal_name = "Bats", animal_noise = "Screech")
bear = Animals(animal_name = "Bears", animal_noise = "Growl")
bee = Animals(animal_name = "Bees", animal_noise = "Buzz")
bird = Animals(animal_name = "Birds", animal_noise = "Chirp")
camel = Animals(animal_name = "Camels", animal_noise = "Grunt")
cat = Animals(animal_name = "Cats", animal_noise = "Meow")
cow = Animals(animal_name = "Cows", animal_noise = "Moo")
chick = Animals(animal_name = "Chicks", animal_noise = "Cheep")
chicken = Animals(animal_name = "Chickens", animal_noise = "Cluck")

db.session.add(ape)
db.session.add(bat)
db.session.add(bear)
db.session.add(bee)
db.session.add(bird)
db.session.add(camel)
db.session.add(cat)
db.session.add(cow)
db.session.add(chick)
db.session.add(chicken)

db.session.commit()
