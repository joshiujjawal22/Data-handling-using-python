"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('CSV/texts.csv', 'r') as f:
    texts = list(csv.reader(f))
   

with open('CSV/calls.csv', 'r') as f:
    calls = list(csv.reader(f))
   


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"


"""


if __name__ == '__main__':
    print("First record of texts, {} texts {} at time {}".format(texts[0][0], texts[0][1], texts[0][2]))
    print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(
        calls[len(calls)-1][0], calls[len(calls)-1][1],
        calls[len(calls)-1][2], calls[len(calls)-1][3]))


