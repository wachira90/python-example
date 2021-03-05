import random
import string

#digit
x = 4

# printing lowercase
letters = string.ascii_lowercase
print ( ''.join(random.choice(letters) for i in range(x)) )

# printing uppercase
letters = string.ascii_uppercase
print ( ''.join(random.choice(letters) for i in range(x)) )

# printing letters
letters = string.ascii_letters
print ( ''.join(random.choice(letters) for i in range(x)) )

# printing digits
letters = string.digits
print ( ''.join(random.choice(letters) for i in range(x)) )

# printing punctuation
letters = string.punctuation
print ( ''.join(random.choice(letters) for i in range(x)) )
