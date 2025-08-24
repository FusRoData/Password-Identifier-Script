# Password-Identifier-Script
This script will allow the user to load password files of usernames and corresponding hashed passwords as well as a list of commonly used passwords to determine if the user has a common password

Password files are generally stored in a pairing of usernames and a cryptographic hash of the password. The Password Identifier Script is used to cross check the hashed passwords against a common password list.
Note: Users are assumed to have a basic understanding of command line interface (CLI), using file directories and json files.

1.	Saving the program and files
  a.	Save the script in a location on your machine
  b.	Save the hashed passwords file and the common password file to the same location as the script

2.	Launching the program
  a.	Open the script as you would any other application (double click or right click and open –this example will use terminal)
  b.	Alternatively open the file directory through the CLI and start the program
  Please note the program name through this document is “passwdidentityrx” and may be different on your version
 <img width="384" height="78" alt="image" src="https://github.com/user-attachments/assets/fff209a4-5b78-46a0-8e6f-e42ab8ffeb27" />
  c.	If this does not work, you may need to install Python on your machine. You may need to seek support or permission from your IT department

3.	Using the script
a.	If the program has launched correctly, you should see “Welcome” and then a prompt to enter the path to the json file, “Enter your JSON path or [E] to exit:”
<img width="489" height="58" alt="image" src="https://github.com/user-attachments/assets/480165b4-3430-4a60-98d4-c6f97e056249" />
b.	You should then enter the file path to where the users and hashed password file is stored, eg: using the file jsondata.json, type “/home/kali/Desktop/jsondata.json” and then press the Enter/Return key
<img width="888" height="30" alt="image" src="https://github.com/user-attachments/assets/d1bb1b49-1e56-4c62-8416-20ee5081dfde" />
c.	You should then see the next prompt “Enter the path to your password file:” where you can input the password list file eg. using the file rockyou.txt, type /home/kali/Desktop/rockyou.txt
<img width="870" height="30" alt="image" src="https://github.com/user-attachments/assets/044c9fcd-0582-413e-9bc7-546a0b644f28" />
d.	Once loaded, you will see output of the users in the json file and if their password was found. 
<img width="352" height="109" alt="image" src="https://github.com/user-attachments/assets/ddbacb8c-3a8c-43c3-b4d3-98ef122acbec" />

If you have entered any file path incorrectly, output will display “Error loading file” and ask again for the file path
<img width="614" height="83" alt="image" src="https://github.com/user-attachments/assets/cb500636-7631-4fec-a891-0bf7e93010b0" />
e.	This script will continue to loop until command is given to exit
<img width="505" height="56" alt="image" src="https://github.com/user-attachments/assets/aa5d395a-4cca-438b-8bb6-c5b109fdeae5" />

A separate file will automatically be created with the users plain text passwords in the same location as the Password Identifier Script, called ‘password_finder.json’ that will output similar to the following image
<img width="511" height="609" alt="image" src="https://github.com/user-attachments/assets/f88da5fa-fe5b-4ad2-b9c0-5aa714eeab98" />
 
