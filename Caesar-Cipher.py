print ("\nWelcome to the Caesar Cipher Encryption and Decrytpion System")


history=[]
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encryption=""
decryption=""

#"""User Prompt"""

print("1:Encryption")
print("2:Decryption")
print("3:Brute Force")
print("4:History")
print("5:Exit")
choice=input("\nEnter Choice (1-5):")


"""Encryption"""

"""First we start by displaying the message entered by the user , then that message is used in the string alphabet to locate
the position of each letter. A new position is made after the user enters the shift key. That new position , depending on the shift
key, is used the generate new letters. These new letters are located in the string alphabet and used to generate a encrypted text """
""""""
if choice== "1":

  text=input("Enter a message : ")
  key=int(input("Choose a shift key from 0-10 : "))  

  for letter in text:
    print(letter)
    position=alphabet.index(letter)
    new_position=(position +key)
  #"""""print("Current position:",position)"""
  #"""print ("Position after shift key:",new_position,'\n')"""
    new_letter=alphabet[new_position]
    encryption=encryption+new_letter
  
  print(encryption)


  """Decryption """

elif choice == "2":
  text=input("Enter a message : ")
  key=int(input("Choose a shift key from 0-10 : "))


  for letter in text:
    print (letter)
    position=alphabet.index(letter)
    old_position=(position -key)
    old_letters=alphabet[old_position]
    decryption=decryption+old_letters
  
  print(decryption)  




"""User History"""
record={"text":text, "shift value":key,
        "Encrypted text":encryption ,
        "Decrypted text":decryption
        }
