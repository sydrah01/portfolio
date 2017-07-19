class User:
    # Define the fields and methods for your object here.
	def __init__(self, user_name, password):
		self.user_name = user_name
		self.password = password
		self.connections = []

	def getUsername (self):
		return self.user_name

	def getConnections(self):
		return self.connections

	def addConnections(self, connection_id):
		self.connections.append(connection_id)

class Network:
	def __init__ (self):
		self.user = []
	def addUser(self, username, password):
		# creat new user with given username
		# and password
		#append that user in the list
		myUser = User(username, password)
		self.user.append(myUser)
		print("user " +  str(username) + " added!")

    # Define the fields and methods for your object here.
def main():
	myNetwork = Network()
	username = input("Enter a username")
	password = input("Enter a password")
	myNetwork.addUser("Liz Gentile", "im_ur_m0m")
	myNetwork.addUser("Sydrah", "heyo rico")
	
    # Define the program flow for your user interface here.


# Runs your program.
if __name__ == '__main__':
	main()