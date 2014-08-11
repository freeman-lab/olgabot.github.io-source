#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Olga Botvinnik'
SITENAME = u'Science, meet productivity'
SITEURL = ''
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'


TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'http://github.com/olgabot'),
          ('twitter-square', 'http://twitter.com/olgabot'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "pure-single"

COVER_IMG_URL = "content/images/caterpillar.jpg"
PROFILE_IMG_URL = "content/images/olga_icon_square.jpg"
TAGLINE = "Exploring productivity, python, and reproducibility in science"
DISQUS_SITENAME = "sciencemeetproductivity"
