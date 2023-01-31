# Jenkylll with RSS feed example

This example demonstrates how to use a python script to fetch from an RSS feed and populate a markdown file.
If you add the python script to a cron job, it will get automatically updated.

## Running
First fetch the RSS feed and create the markdown file
```
cd site
python3 ../scripts/fetch.py
```

Now run jenkyll:
```
bundle exec jekyll serve
```

Browse to [http://localhost:4000](http://localhost:4000)

