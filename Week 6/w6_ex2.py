#from collections import Counter
#test = "one one one two three four four five"
#test_dict_ez = Counter(test.split())
#print(test_dict_ez)
'''
The above 4 lines I found as a solution to someone else
asking how to do this and they work perfectly,
but I don't think that's the way you expect us to do it.
'''

text = "test test test one two two three three three"

def remove_punc(a):
    newtext = ''
    for i in a.lower():
        if i in 'abcdefghijklmnopqrstuvwxyz ':
            newtext = newtext + i
    return newtext

newtext = remove_punc(text)
textlist = newtext.split()

print(newtext)
print(textlist)

def make_dict(textlist):
    dict_text = {}
    for i in textlist:
        dict_text[i] = dict_text.setdefault(i, 0) + 1

    return dict_text

print(make_dict(text))
