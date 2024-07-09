# Checky
Checky can be used to get the checksum of a file, and then compare it with the checksum given by the creators. Open Checky, enter the file path, the type of checksum and the checksum given by the creators. Checky will compare the checksums and output whether the file has been damaged or not. It will save the result to a file along with the date of use, file path and other details.

# design behind the app
Checky has been written in Python 3. It is completely free and open-source. it runs on the user's computer.
 
# options
1. Compare checksums
2. Access history
3. Delete history
4. Exit

# Using Checky from the terminal
Checky can be used from the terminal as well.
USAGE: checky [file path] [checksum type] [checksum provided by creators] OR check

# license
Checky is distributed under a license named after itself- Checky license...

# additional information
- to make installer: pyinstaller checky.py --onefile --icon [icon path]
