print ("Welcome to the Caesar Cipher Encryption and Decrytpion System")
text=input("Enter a message")
key=int(input("Choose a shift key from 0-10"))
alphabet=ABCDEFGHIJKLMNOPQRSTUVWXYZ

for letter in text:
  print(letter)
  position=alphabet.index(letter)
  new_position=position +key
