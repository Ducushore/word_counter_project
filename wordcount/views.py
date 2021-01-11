from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html', {'hithere': 'This is me'})


def aboutpage(request):
    return render(request, 'about.html')


# def eggs(request):
#     return HttpResponse('<h1>EGGS</h1>')


def countpage(request):
    fulltext = request.GET['fulltext']
    # print(fulltext)  # this is printed only in the terminal side

    wordlist = fulltext.split()  # this is gonna split the text by words (actually after each SPACE)

    if not fulltext:  # if no input is made but 'Count' button si pressed, then a INFO is delivered ('emptyinput.html' page)
        return render(request, 'emptyinput.html')

    wordcountdictionary = {}  # declare an empty dictionary where all the words will be counted

    for word in wordlist:  # looping word by word into the newly created 'wordlist'
        if word in wordcountdictionary:
            # when we want to add (count) one unit to the'wordcountdictionary' related to a counted word
            wordcountdictionary[word] += 1
        else:
            # this is when we want to add a new word to the 'wordcountdictionary'
            wordcountdictionary[word] = 1

    # # Variant ONE - returning a DICTIONARY :
    # return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'wordcountdictionary': wordcountdictionary})

    # # Variant TWO - returning a LIST :
    # return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'wordcountdictionary': wordcountdictionary.items()})

    # # Variant THREE - returning an ORDERED/SORTED LIST with a SORTED function:
    # import operator
    # # This use of itemgetter is great because it makes everything clear while also being faster as all operations are kept on the C side.
    # sortedwordcountdictionary = sorted(wordcountdictionary.items(), key=operator.itemgetter(1), reverse=True)

    # # Variant FOUR - returning an ORDERED/SORTED LIST with a LAMBDA function:
    # using lambda instead of itemgetter: is not as clear, it is also slower and it is preferred not to use lambda
    # unless you have to, e.g. list comprehensions are preferred over using map with a lambda
    sortedwordcountdictionary = sorted(wordcountdictionary.items(), key=lambda x: x[1], reverse=True)

    # 'reverse=True' is reversing tho soring of the key, from the biggest to the smallest

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist),
                                          'sortedwordcountdictionary': sortedwordcountdictionary})
