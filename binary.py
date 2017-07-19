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

SearchInput= input('What country are you looking for?:')
index = int((F+L))//2
SearchInput=input()
while (True):
	
	if SearchInput <= countries[index]:
		index = int((F+L))//2
		print("index")

	elif SearchInput> countries[index]:
		index = int((F+L))//2
		F=index

	elif SearchInput< countries[index]:
		index = int((F+L))//2
		L=index