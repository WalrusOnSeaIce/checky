##Checky##
Checky can be used to get the checksum of a file, and then compare it with the checksum given by the creators. Open Checky, enter the file path, the type of checksum and the checksum given by the creators. Checky will compare the checksums and output if the file has been damaged or not. It will save the result to a database along with the date of use, file path and other details.

Checky has been written in Python 3 and uses sqlite3. It is completely free and open-source.
 
#Options
1. Compare checksums
2. Access history
3. Delete history
4. Exit

#Using Checky from the terminal
Checky can be used from the terminal as well.
USAGE: checky [file path] [checksum type] [checksum provided by creators] OR checky

#Source Code
Can be found on Github: https://github.com/WalrusOnSeaIce/checky

- to make installer: pyinstaller checky.py --onefile --icon [icon path]
- to make table: CREATE TABLE checksums (id INTEGER PRIMARY KEY AUTOINCREMENT, date DATE, file VARCHAR(255), hash VARCHAR(12), original_checksum VARCHAR(60), file_checksum VARCHAR(60), result VARCHAR(30));
