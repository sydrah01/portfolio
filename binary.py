import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

length = len(countries)
print(countries[1])
print(countries)

#input a country
# look for the index of that country
F = 0
L =len(countries)
index = int((F+L))//2

user_input=input()
while(True):

	if user_input == countries[index]:
		print("index")

	elif user_input> countries[index]:
		F=index

	elif user_input< countries[index]:
		L=index