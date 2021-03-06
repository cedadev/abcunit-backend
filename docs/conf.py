
import sys, os

project = 'ABCUnit Backend'
copyright = '2020, Jonathan Haigh'
author = 'Jonathan Haigh'

version = '1.2.0'
release = 'v1.2.0'

highlight_language = 'python'
pygments_style = 'sphinx'


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.coverage',
    'sphinx.ext.todo',
    'sphinx.ext.autosectionlabel',
    'm2r2'
]

source_suffix = ['.rst', '.md']

master_doc = 'index'

exclude_patterns = ['_build', 'sphinx-enki-info.txt']

keep_warnings = True


html_theme = 'default'
