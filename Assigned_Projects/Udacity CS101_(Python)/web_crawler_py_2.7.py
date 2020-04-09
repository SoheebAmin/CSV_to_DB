# NOTE: This will not work in Python 3. It was written for Python 2.7

#Test page. It can be swapped with any page.
page = 'https://bbc.co.uk'

#This extracts source code from given url.
def get_page(url):
	try:
	    import urllib
	    return urllib.urlopen(url).read()
	except:
	    return ""

#This puts two list together without repetiton. 
def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

#This finds the first URL and its end position within a source page.
def get_link(page):
  start_link = page.find("<a href=")
  if start_link == -1:
      return None, 0
  start_quote = page.find('"', start_link)
  end_quote = page.find('"', start_quote +1)
  url = page[start_quote+1:end_quote]
  return url, end_quote

#This takes the source page and extracts its URLs.
def get_all_links(page):
  links = []
  while True:
    url, endpos = get_link(page)
    if url:
      links.append(url)
      page = page[endpos:]
    else:
      break
  return links 

#This adds a keyword and URL to an index.
def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
          if url not in index:
            entry[1].append(url)
          return
    index.append([keyword, [url]])

#This searches keywords and returns their URLs.
def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []


#This adds all the words in a source page into the index, along with their URL.
def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

#This creates the index using the URL finder, adding every word from the seed pages and linked pages to the limit of max_pages.
def crawl_web(seed, max_pages):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
      page = tocrawl.pop()
      if page not in crawled and len(crawled) < max_pages:
        body = get_page(page)
        add_page_to_index(index, page, body)
        union(tocrawl, get_all_links(body))
        crawled.append(page)
    return index   


print (crawl_web(page, 4))
