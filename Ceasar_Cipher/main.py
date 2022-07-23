alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your secret word:\n").lower()
shift = int(input("How many character you want to shift?:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    new_text = ""
    for i in text:
        cipher_text_index = alphabet.index(i) + shift
        cipher_text = alphabet[cipher_text_index]
        new_text += cipher_text
    print(f"The encoded text is : {new_text}")

    

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 


# -----------------------------Decryption --------------------------------
#TODO-1: Create a function  'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
    old_text = ""
    for j in text:
        old_index = alphabet.index(j) - shift
        old_text += alphabet[old_index]
  #print output: "The decoded text is hello"
    print(f"After decode your text is {old_text}")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction == "encode".lower():
    encrypt(text, shift)
elif direction == "decode".lower():
    decrypt(text, shift)

