def alphabet_position(letter):
  lower_letters = "abcdefghijklmnopqrstuvwxyz"
  upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  if letter.islower():
    return lower_letters.index(letter)
  else:
    return upper_letters.index(letter)

def rotate_character(char, rot):
  if not char.isalpha():
    return char
  else:
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rotated_char_position = (alphabet_position(char)+rot)%26
    if char.islower():
      return lower_letters[rotated_char_position]
    else:
      return upper_letters[rotated_char_position]

def encrypt(text, rot):
  encrypted_string = ""
  for char in text:
    encrypted_string += rotate_character(char,rot)
  return encrypted_string

def main():
  text = input("Please write the statement you wish to encrypt:\n>>> ")
  rot = int(input("Please input the amount of characters to rotate your ciphered message by:\n>>> "))
  print(encrypt(text,rot))
if __name__ == '__main__':
  main()