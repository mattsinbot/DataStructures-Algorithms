"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""

import csv
import operator

max_duration = 0
phonedict = {}
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for one_record in calls:
        if one_record[0] in phonedict:
            phonedict[one_record[0]] += int(one_record[3])
        else:
            phonedict[one_record[0]] = int(one_record[3])
            
        if one_record[1] in phonedict:
            phonedict[one_record[1]] += int(one_record[3])
        else:
            phonedict[one_record[1]] = int(one_record[3])
            
# Find the key with maximum value
max_time_phone = max(phonedict.iteritems(), key=operator.itemgetter(1))[0]
print("%s spent the longest time, %2.4f seconds, on the phone during September 2016" % (max_time_phone, phonedict[max_time_phone]))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
"""
O(N) -> for reading the file
O(N^2) -> O(N) computations for "for loop" * O(N) computations for fetching the keys from the dictionary
Total = O(N) + O(N^2) ~ O(N^2)
"""

