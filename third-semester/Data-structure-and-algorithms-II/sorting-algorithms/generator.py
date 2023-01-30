from data import *
import random


class Person():
	def __init__(self):
		self.name = giveName()
		self.height = round(random.uniform(1.30, 2.10), 3)
		self.weight = round(random.uniform(40.0, 180.0), 3)
		self.age = round(random.uniform(18, 90), 0)

	def __str__(self):
		return f'Persona:[{self.name}|{self.height} m|{self.weight} kg|{self.age} years old]'


def giveName():
	name = random.choice(names)
	surname1 = random.choice(surnames)
	surname2 = random.choice(surnames)
	return f'{name} {surname1} {surname2}'


def main():
    person1 = Person()
    print(person1)


if __name__ == '__main__':
	main()