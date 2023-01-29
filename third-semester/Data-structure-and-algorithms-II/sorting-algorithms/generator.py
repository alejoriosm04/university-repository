from data import *
import random


class Person():
	def __init__(self):
		self.name = giveName()
		self.height = random.uniform(1.30, 2.10)


def giveReal(bottomLimit, topLimit):
	pass


def giveName():
	name = random.choice(names)
	surname1 = random.choice(surnames)
	surname2 = random.choice(surnames)
	return f'{name} {surname1} {surname2}'


def main():
    person1 = Person()
    print(person1.name)
    print(person1.height)


if __name__ == '__main__':
	main()