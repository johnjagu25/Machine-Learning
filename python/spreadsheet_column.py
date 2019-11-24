# MS Excel column titles have the following pattern:
#  A, B, C, ..., Z, AA, AB, ..., AZ, BA, BB, ..., ZZ, AAA, AAB, ... etc.
#  In other words, column 1 is named "A", column 2 is "B", column 26 is "Z", 
#  column 27 is "AA" and so forth.
#  Given a positive integer, find its corresponding column name.
import math

def spreadsheet_column(value):
    columns =  []
    i = 0
    while value > 0:
        remainder = value % 26
        if remainder == 0:
            columns.append("Z")
            value = ( value // 26 ) - 1
        else :
            columns.append(chr( (remainder - 1) + ord("A")))
            value = value // 26
        
        i += 1
    
    return "".join(columns[::-1])

    

        
print(spreadsheet_column(51))
print(spreadsheet_column(52))
print(spreadsheet_column(53))
print(spreadsheet_column(676))