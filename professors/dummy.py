from faker import Faker
import random
from .models import School, Professor, Course

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

def generateProf(n):
    departments = ['CPSC', 'MATH', 'ENGL', 'CHIN', 'PHYS', 'SCIE', 'BIOL', 'CHEM']
    fake = Faker()
    for i in range(n):
        index = random.randint(0, len(departments) - 1)
        school = School.objects.first()
        department = departments[index]
        Professor.objects.create(name=fake.name(), school=school, department=department)


