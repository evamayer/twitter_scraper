import re
import numpy
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def filterFunc(x):
    if "#" in x or "@" in x or re.match("a|the|an|the|to|in|for|of|or|by|with|is|on|that|be|from|https|\\n|//t|me|we|you|my|this|it|s|I|&amp|not|The|was|what|what|but", x):
        return False
    else:
        return True

def split_words(text):
    result = re.split("\.|\?|\,|\-|\'|\"|\!|\:|\;|\ ", text)
    return list(filter(filterFunc, result))

def visualize_words(textfile, imagefile):

    f = open(textfile, encoding="ascii", errors='ignore')
    linelist = f.readlines()

    word_frequencies = {}

    for line in linelist:
        for word in split_words(line):
            word_lower = word.lower()
            if word_lower in word_frequencies:
                word_frequencies[word_lower] += 1
            else:
                word_frequencies[word_lower] = 1

    mask = numpy.array(Image.open(imagefile))
    wc = WordCloud(background_color="white", min_word_length=3, width=1600, height=900, max_words = 120, mask=mask)
    wc.generate_from_frequencies(word_frequencies)

    plt.axis("off")
    plt.imshow(wc, interpolation="bilinear")
    plt.show()
    

visualize_words("running.txt", "runner.jpg")
