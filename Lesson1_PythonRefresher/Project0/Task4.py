"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

unique_text_in = list()
unique_text_out = list()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for i in texts:
        if i[0] not in unique_text_out:
            unique_text_out.append(i[0])
        if i[1] not in unique_text_in:
            unique_text_in.append(i[1])

unique_calls_in = list()
unique_calls_out = list()
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for j in calls:
        if j[0] not in unique_calls_out:
            unique_calls_out.append(j[0])
        if j[1] not in unique_calls_in:
            unique_calls_in.append(j[1])

# Check for probable tele marketers
probable_telemarketers = list()
for k in unique_calls_out:
    if k not in unique_calls_in:
        if k not in unique_text_in:
            if k not in unique_text_out:
                probable_telemarketers.append(k)
print("These numbers could be telemarketers: ")

# Print
probable_telemarketers.sort()
for probable_tele in probable_telemarketers:
    print(probable_tele)




"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

"""
O(N^2) -> to get unique numbers in the calls record
O(N^2) -> to get unique numbers in the texts record
O(N^2) -> O(N) (if all numbers are unique) * O(N) (if all numbers are telemarketers)
O(N^2) -> for sorting
Total = O(N^2) + O(N^2) + O(N^2) + O(N^2) ~ O(N^2)
"""
