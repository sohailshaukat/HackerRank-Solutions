'''
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
import statistics
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        avg = statistics.mean(self.scores)
        if avg >= 90:
            return 'O'
        elif 80<=avg<90:
            return 'E'
        elif 70<=avg<80:
            return 'A'
        elif 55<=avg<70:
            return 'P'
        elif 40<=avg<55:
            return 'D'
        else:
            return 'T'
line = input().split()
