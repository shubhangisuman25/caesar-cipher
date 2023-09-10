alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,direction):
  alpha =''
  for i in range(0,len(text)):
    if(text[i] in alphabet):
      index = alphabet.index(text[i])
      if(direction == "encode"):
        shifted_index = index + shift
        if(shifted_index > 25):
          shifted_index = shifted_index-26*(int(shifted_index/26)+1)
        alpha += alphabet[shifted_index]
        

      elif (direction == "decode"):
        deshift_index = index - shift
        if(deshift_index < 0):
          deshift_index= abs(26*(int(abs(deshift_index)/26)+1)+deshift_index)
        alpha += alphabet[deshift_index]
      
    else:
      alpha = alpha+ text[i]

  print(f"The {direction}d text is: {alpha}")

  
import art
print(art.logo)


user_response= "yes"
while(user_response == "yes"):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(text=text,shift=shift,direction=direction)
  user_response= input("Do you want to restart? Yes/No")

if(user_response == "no"):
  print("Goodbye")
