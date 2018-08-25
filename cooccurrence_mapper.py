import sys
import io
import re
import string

topTen=["blockchain","bitcoin","crypto","one","new","puerto","women","people","cryptocurrency","technology"]

stop_words = ["a","about","above","after","again","against","all","am","an","and","any","are","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","ours","ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","said","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too","under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves"]

for line in sys.stdin:
    line=line.strip()
    words=line.split()
	 for i in range(len(words)):
            words[i] = words[i].lower()
            words[i] = re.sub(r'[^\x00-\x7F]+',"", words[i])
            words[i] = words[i].translate(str.maketrans({key: None for key in string.punctuation}))
    for word in words[5:len(words)-5]:
            if len(word) > 0:
                if word in topTen:
                    i = words.index(word)
                    for co_occurword in words[i+1:i+6] + words[i-5:i]:
                        if co_occurword not in stop_words:
                            print('%s\t%s\t%s ' % (word, co_occurword))
                           