# A look-and-say sequence is defined as the integer sequence beginning with
# a single digit in which the next term is obtained by describing the previous term.
# An example is easier to understand:

# Each consecutive value describes the prior value.


def look_and_say(num_val):
    to_text = str(num_val)
    len_to_text = len(to_text)
    if len_to_text == 1:
        print("")
        return False
    response = ""
    word_dict = num_to_word()
    for index in range(len_to_text):
        value = to_text[index]
        if index % 2 == 0:
            response += word_dict[to_text[index]] 
        else :
            last_index_check = index != len_to_text - 1
            add_s = "'s" if int(value) < 2  and not last_index_check else ""
            punctuator = ", " if last_index_check else "."
            response += " "+to_text[index] + add_s + punctuator
    print(response)




def num_to_word():
    word_dict = {"1": "one", "2": "two", "3": "three", "4": "four",
    "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "Nine" }
    return word_dict


look_and_say(1)
#
look_and_say(11)
# one 1's
look_and_say(21)
# two 1's
look_and_say(1211)
# one 2, and one 1.
look_and_say(111221)
# #one 1, one 2, and two 1's.
