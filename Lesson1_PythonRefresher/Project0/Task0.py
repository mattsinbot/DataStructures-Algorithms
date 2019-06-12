"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    print("First record of texts, " + texts[0][0] + " texts " + texts[0][1] + " at time " + texts[0][2])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    num_data = len(calls)
    print("Last record of calls, " + calls[num_data-1][0] + " calls " + calls[num_data-1][1] + " at time " + calls[num_data-1][2] + ", lasting " + calls[num_data-1][3] + " seconds")

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
"""
Task 0:
Assuming the file has N lines in it and each line has comparable lengths and readin a line takes a constant computaations. Then rading a file of N lines, takes O(N) computations. Also assuming constant computations to convert one line into list, total computation to convert into list is again O(N). Fetching the element of a list is O(1). Hence total computation for task0 is:
O(N) + O(N) + O(1) ~ O(N).

Same argument for getting last call record hold true. Hence for this task also, O(N) computations are required.
"""
