"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

#=================================
#           Part: A
#=================================
fixed_line_code = list()
# telemarketer_code = list()
mobile_code = list()
count = 0
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for one_call in calls:
        if one_call[0][:5] == "(080)":
            if one_call[1][0] == "(":
                curr = one_call[1][1] 
                code = curr
                i = 1
                while curr != ")":
                    i += 1
                    curr = one_call[1][i]
                    if curr != ")":
                        code += curr
                if code not in fixed_line_code:
                    fixed_line_code.append(code)
            # elif one_call[1][0] == "1":
                # print(one_call[1][0])
                # telemarketer_code.append(one_call[1])
            else:
                if one_call[1][:4] not in mobile_code:
                    mobile_code.append(one_call[1][:4])

# Print Area Code 
no_repeat_area_code = fixed_line_code + mobile_code
no_repeat_area_code.sort()
for single_code in no_repeat_area_code:
    print(single_code)
    
"""
O(N) -> reading the file and converting in to the list
O(N^2) -> O(N)(for loop) * O(N)(checking uniqueness)
O(N^2) -> for sorting
O(N) -> print
Total = O(N) + O(N^2) + O(N^2) + O(N) ~ O(N^2)
"""


#=================================
#           Part: B
#=================================
bangalore_to_other = 0
bangalore_to_bangalore = 0
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for one_call in calls:
        if one_call[0][:5] == "(080)":
            bangalore_to_other += 1
            if one_call[1][:5] == "(080)":
                bangalore_to_bangalore += 1
print("\n%2.2f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore\n"%(bangalore_to_bangalore*100/bangalore_to_other))

"""
O(N) -> reading the file and converting into list
O(N) -> for the "for" loop
O(1) -> percentage computation
Total = O(N) + O(N) + O(1) ~ O(N)
"""

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
