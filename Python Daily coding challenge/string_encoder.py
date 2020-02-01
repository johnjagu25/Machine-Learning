# Run-length encoding is a fast and simple method of encoding strings. 
# The basic idea is to represent repeated successive characters as a single count and character. 
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".


def encoder(text):
    
    t_dict = {}
    lastChar = text[0]
    final_res = ""
    for c in text+" ":
        if lastChar != c:
            final_res += str(t_dict[lastChar])+lastChar
            t_dict[lastChar] = 0
            lastChar = c
        if c in t_dict:
            t_dict[c] += 1
        else:
            t_dict[c] = 1
        
    print(final_res)


encoder("AAAABBBCCDAA")


