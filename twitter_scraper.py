import snscrape.modules.twitter as twitter

def scrape_twitter(topic, filename):
    f = open(filename, "w", encoding="utf-8")
    maxTweets = 10000
    keyword = topic
    for i, tweet in enumerate(twitter.TwitterSearchScraper(keyword + ' since:2022-01-01 until:2023-01-01 lang:"en" ').get_items()):
        f.write(tweet.rawContent)  
        if i > maxTweets:
            break
        print(i)
    f.close()

scrape_twitter("#running", "running.txt")
scrape_twitter("#Hungary", "hungary.txt")
scrape_twitter("#Amsterdam", "amsterdam.txt")