from faker import Faker
import random

def generateProfList(numOfProf):
    profs = []
    fake = Faker()
    for i in range(numOfProf):
        prof = {
            'name': fake.name(),
            'email': fake.email(),
            'avgRate': round(random.random() * 5, 2)
        }
        profs.append(prof)
    return profs