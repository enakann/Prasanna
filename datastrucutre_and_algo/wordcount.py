
def get_word_count(filename):
    d={}
    w=[]    ##this is the ds which are going to use
    f=open(filename)
    lines=f.readlines()
    for line in lines:
        words=line.split()
        for word in words:
            if ',' in word:
                w.extend(word.split(','))
            else:
                w.append(word)
    for wor in w:
        if wor in d:
            d[wor]+=1
        else:
            d[wor]=1
    print(d)



get_word_count("wordcount")







