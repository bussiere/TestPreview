
# coding: utf-8

# In[6]:

from webpreview import web_preview
import bs4 as BeautifulSoup


# In[8]:
url = "http://www.streetpress.com/sujet/1488190869-tribunal-de-l-armee"
title, description, image = web_preview(url)


# In[7]:
template = """<html><head><meta name="twitter:card" content="" />
<meta name="twitter:site" content="" />
<meta name="twitter:title" content="%s" />
<meta name="twitter:description" content="%s" />
<meta name="twitter:image" content="%s" />
<meta property="og:type" content="website">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="%s">
<meta property="og:image" content="%s">
</head><body></body></html>"""%(title,description,image,title,description,url,image)
f = open('index.html', 'w')
f.write(template)
f.close()


