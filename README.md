# google-py-exercise--removing-outdated-permissions

This piece of code was written as part of the Google Cybersecurity Course circuit.

Most of it ended up pretty similar to the original exercise, though I did:

1. Identify a small slip in the provided example and fixed it;
2. Experiment writing a "while" loop instead of a "for" iterative statement.

Inside the exercise's context, I, as the student, was meant to play the role of a security professional working at a health care company.
My hypothetical task would be of regularly updating a file that identified all employees who could access restricted content.
More specifically, removing IP addresses that no longer should access these confidential files.

Said file's contents were based on who's working with personal patient records. There is meant to be an allowed list for IP addresses that is permitted to sign into the restricted subnetwork, so even allowed employees would also have to fit the IP address requirement or else they'd be restricted; there is also a “remove” list that identifies which employees should have their permission removed.

In short, this is a piece of Python code for reading a .txt file and removing outdated IP permissions.
