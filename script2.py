#input sentence
sentence=input("enter a sentence please : ")

#extracting words
words=sentence.split()

word_count={}
#if word exists, increment. if word doesn't exist, initiate.
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

print(word_count)