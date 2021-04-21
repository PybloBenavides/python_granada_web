#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Python Granada Org'
SITENAME = 'Python Granada'
SITEURL = ''

PATH = 'content'

THEME = "themes/buruma"
TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["i18n_subsites", "assets"]

JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n"],
}


# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Theme config
MENUITEMS_NAVBAR = (("Docs", "/p/docs.html"), ("Info", "/p/info.html"))
MENUITEMS_NAVBAR_FEATURED = (("Docs", "/p/docs.html", "is-link"), ("Info", "/p/info", "is-info"))
NAVBAR_STYLE = "is-warning"


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True