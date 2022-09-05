# Etude 9 - Substrings
# Asks the User for the alphabet to be used in the form of input which is taken
# as a string. This alphabet is then used tp create the longest string that 
# contains no repeated sequences (substring).

import sys
import string
import random

# Turn user input into list with all the letters of the chosen alphabet 
# to allow for easier mainupulation in creating the string 
#
def alphabet_strip(user_alphabet: string) -> list:
    alphabet_str = "qwertyuiopasdfghjklzxcvbnm "
    alphabet_list = []
    for i in user_alphabet:
        if i in alphabet_str:
            alphabet_list += i
        else:
            continue
    return(alphabet_list)



# String builder for the specific alphabet requested
#
def alphabet_build(alphabet_list: list) -> string:
    alphabet_list = alphabet_list
    current_substring = []
    build_string = ""
    build_string += alphabet_list[0] + alphabet_list[0]
    finish = False
    position1 = 0
    position2 = 0
    alph_pos = len(alphabet_list)
    substring = ""
    overlap = True
    while finish == False:
        position2 = position1 + 1
        alph_count = 0
        random.shuffle(alphabet_list)
        substring = build_string[position1] + build_string[position2]
        if substring not in current_substring:
            current_substring.append(substring)
        for i in alphabet_list:
            temp_build_str = build_string
            temp_build_str += i
            position1 += 1
            position2 = position1 + 1
            if (temp_build_str[position1] + temp_build_str[position2]) in current_substring:
                if ((temp_build_str[position1] + temp_build_str[position2]) == (temp_build_str[position1 - 1] + temp_build_str[position2 -1])) & overlap == True:
                    build_string = temp_build_str
                    overlap = False
                    break
                else:
                    position1 -= 1
                    temp_build_str = build_string
                    alph_count += 1
                    if alph_count >= alph_pos:
                        finish = True
                        break
            elif (temp_build_str[position1] + temp_build_str[position2]) not in current_substring:
                build_string = temp_build_str
                overlap = True
                break
    return(build_string)

        


longest_string = ""

# Enter the desired alphabet 
print("Please enter the desired alphabet: ")
for line in sys.stdin:
    user_alphabet = line
    user_alphabet = user_alphabet.rstrip('\n')
    longest_string = ""
    alphabet_list = alphabet_strip(user_alphabet)
    for i in range(100): 
        built_string = alphabet_build(alphabet_list)
        if len(built_string) > len(longest_string):
            longest_string = built_string
    print(longest_string)


