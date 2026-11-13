import random

vow = ["b","c","d","f","g","h","j","k","l","m","n","p","q",
      "r","s","t","v","w","x","z"]
con = ["a","e","i","o","y","u"]

def string_id(n=10):

  string_id = ""

  for i in range(0,n): # Looping n times
    if i % 2 == 0:
      string_id += random.choice(vow) # When eaven
    else:
      string_id += random.choice(con) # When uneaven
      
  n = random.randrange(0,99) # Random number between 0 and 99
  return f"{str(n).zfill(2)}{string_id}" # Returns final string id
  