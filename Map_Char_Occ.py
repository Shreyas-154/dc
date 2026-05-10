# mapper.py

import sys

for line in sys.stdin:

    line = line.strip()

    for ch in line:

        if ch != " ":

            print(ch + "\t1")



# reducer.py

import sys

current_char = ""
current_count = 0

for line in sys.stdin:

    line = line.strip()

    ch, count = line.split("\t")

    count = int(count)

    if ch == current_char:

        current_count = current_count + count

    else:

        if current_char:

            print(current_char + "\t" + str(current_count))

        current_char = ch
        current_count = count

print(current_char + "\t" + str(current_count))

#----------------------------

#B) WORD COUNT USING MAPREDUCE

# mapper.py

import sys

for line in sys.stdin:

    line = line.strip()

    words = line.split()

    for word in words:

        print(word + "\t1")


# reducer.py

import sys

current_word = ""
current_count = 0

for line in sys.stdin:

    line = line.strip()

    word, count = line.split("\t")

    count = int(count)

    if word == current_word:

        current_count = current_count + count

    else:

        if current_word:

            print(current_word + "\t" + str(current_count))

        current_word = word
        current_count = count

print(current_word + "\t" + str(current_count))
