#!/usr/bin/env/python3

import feedparser
NewsFeed = feedparser.parse('https://www.alcf.anl.gov/training/rss.xml')

def write_header(file):
    file.write('---\n')
    file.write('layout: page\n')
    file.write('title: RSS\n')
    file.write('---\n')
    file.write('\n')
    

with open('rss.markdown', 'w') as file:
    write_header(file)
    for entry in NewsFeed.entries:
        file.write(' - [' + entry["title"] + '](' + entry["link"] + ')\n')

    file.close()
