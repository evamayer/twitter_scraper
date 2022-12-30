# Project 1: Can we learn from Twitter Data?

The twitter_scraper.py script allows us to automatically scrape Twitter for conversations on three topics: running, Hungary and Amsterdam. 

Three text files are created with 10 000 tweets each (running.txt, hungary.txt and amsterdam.txt).

The reader.py script reads these text files and splits the tweets into lines, then words and then filters out certain words and characters. 

The remaining words are then visualised by frequency of occurrance in a word cloud.

The word clouds are presented in matching image outlines (runner, Hungary and tulip silhouettes). 

The repository also contains the resulting images (running_wordcloud.png, hungary_wordcloud.png and amsterdam_wordcloud.png).
