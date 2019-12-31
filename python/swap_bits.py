# Hi, here's your problem today. This problem was recently asked by Twitter:

# Given a 32-bit integer, swap the 1st and 2nd bit, 3rd and 4th bit, up til the 31st 
# and 32nd bit.

# Here's some starting code and an example:


def swap_bits(num):
    return "".join([ num[i+1]+num[i] for i in range(0,len(num),2)])

print(swap_bits("0b10101010101010101010101010101010"))
# b001010101010101010101010101010101
