import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def filterFunc(x):
    if "#" in x or "@" in x or re.match("a|the|an|the|to|in|for|of|or|by|with|is|on|that|be|from|https|\\n|//t|me|we|you|my|this|it", x):
        return False
    else:
        return True

def split_words(text):
    result = re.split("\.|\?|\,|\-|\'|\"|\!|\:|\;|\ ", text)
    return list(filter(filterFunc, result))

f = open("running.txt", encoding="ascii", errors='ignore')
linelist = f.readlines()

word_frequencies = {}

for line in linelist:
    for word in split_words(line):
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1

# print(word_frequencies)

wc = WordCloud(background_color="white", min_word_length=3, width=1600, height=900)
wc.generate_from_frequencies(word_frequencies)

plt.axis("off")
plt.imshow(wc, interpolation="bilinear")
plt.show()
    
