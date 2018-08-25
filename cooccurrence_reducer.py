import sys

topTen=["blockchain","bitcoin","crypto","one","new","puerto","women","people","cryptocurrency","technology"]

co_occur={}

for line in sys.stdin:
    line=line.strip()
    word,co_word=line.split('\t')
    tup = (word,co_word)
    if tup in co_occur.keys():
        co_occur[tup]+=1
    else:
        co_occur[tup]=1
for x in co_occur.keys():
    print('%s\t%s'%(x,co_occur[x]))
