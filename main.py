# This piece of code was written as part of the Google Cybersecurity Course circuit.
# Most of it ended up pretty similar to the original exercise, though I did:
#
# 1. Identify a small slip in the provided example and fixed it;
# 2. Experiment writing a "while" loop instead of a "for" iterative statement.
#
# Inside the exercise's context, I, as the student, was meant to play the role of a security professional working at a health care company.
# My hypothetical task would be of regularly updating a file that identified all employees who could access restricted content.
# More specifically, removing IP addresses that no longer should access these confidential files.
# 
# Said file's contents were based on who's working with personal patient records. There is meant to be an allowed list for IP addresses that
# is permitted to sign into the restricted subnetwork, so even allowed employees would also have to fit the IP address requirement or else
# they'd be restricted; there is also a “remove” list that identifies which employees should have their permission removed.
#
# In short, this is a piece of Python code for reading a .txt file and removing outdated IP permissions.

implist = "allow_list.txt"


# The IP addresses below were provided by the Google Course. I kept them as they were.

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]


with open (implist, "r") as file:
	ip_list = file.read()
ip_list = ip_list.split()


# The "for" iterative statement below was partially provided by the Google Course.
# I detected a potential logic slip in the original, and switched:
#
# 1. "for element in ip_list" to "for element in remove_list"
# 2. "if element in remove_list" to "if element in ip_list"
#
# This because, in the original code as provided by Google, the for loop would skip
# over the next item every time an IP was removed.

# for element in remove_list:
# 	if element in ip_list:
# 		ip_list.remove(element)

# I like using "while", so I tried making the same code with it just for the sake of experimenting.

elem_counter = 0
while elem_counter < len(remove_list):
	if remove_list[elem_counter] in ip_list:
		ip_list.remove(remove_list[elem_counter])
	elem_counter += 1
		

ip_list = "\n".join(ip_list)

with open (implist, "w") as file:
	file.write(ip_list)
