
import sys


curr_word = None
curr_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t')
    count = int(count)
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_word = word
if current_word == word:
    print('%s\t%s' % (current_word, current_count))
