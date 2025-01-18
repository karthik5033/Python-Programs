str ='''New delhi is the capital of India
    Banglore is a capital of Karnataka, Karnataka is India,
    India is the worlds largest democratic country'''
    #print the string /paragraph
print("entered paragraph \n",str)
wordCount =len(str.split())
print("Totsl number of words : ",wordCount)
counts =dict()
words=str.split()
for word in words:
    if word in counts:
        counts[word]=counts[word]+1
    else:
        counts[word]=1
    print(word,counts[word])
searchword =input(" \n Enter the word in search : ")
result =str.find(searchword)

if(result!= -1):
    print(searchword,"word found in paragraph")
else:
    print(searchword,"!!!! word not found in paragraph")





     
     
