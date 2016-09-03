import random
import string

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
all = vowels + consonants
message = "What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: "

letter_input_1 = raw_input(message)
letter_input_2 = raw_input(message)
letter_input_3 = raw_input(message)

def generator(input_letter):
    if input_letter == 'v':
        out_letter = random.choice(vowels)
    elif input_letter == 'c':
        out_letter = random.choice(consonants)
    elif input_letter:
        out_letter = random.choice(all)
    else:
        out_letter = letter_input_1
    return out_letter

name = generator(letter_input_1) + generator(letter_input_2) + generator(letter_input_3)
print name