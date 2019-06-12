"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
num_list = []

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    len_text_records = len(texts)
    for i in range(len_text_records):
        sender_ph = texts[i][0]
        received_ph = texts[i][1]
        if sender_ph not in num_list:
            num_list.append(sender_ph)
        if received_ph not in num_list:
            num_list.append(received_ph)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    len_call_records = len(calls)
    for i in range(len_call_records):
        caller_ph = calls[i][0]
        receiver_ph = calls[i][1]
        if caller_ph not in num_list:
            num_list.append(caller_ph)
        if receiver_ph not in num_list:
            num_list.append(receiver_ph)
print("There are %d different telephone numbers in the records" % (len(num_list)))


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

"""
2*O(N) to read two files. O(N^2) for the "for" loop and nested existence checking.
Therefore total computations required O(N) + O(N^2) = O(N^2)  
"""
