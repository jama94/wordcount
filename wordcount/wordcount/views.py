from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    wordictionary = {}
    for word in set(wordlist):
        wordictionary[word] = wordlist.count(word)
    sortedWords2 = sorted(wordictionary.items(), key = operator.itemgetter(1), reverse = True) #sorted by value (# of the same words)
    sortedWords = sorted(wordictionary.items()) #sorted by key (word)
    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist),'sortedWords':sortedWords2} )

def about(request):
    return render(request, 'about.html')
