import sphinx_rtd_theme
from sphinx_rtd_theme import __version__ as theme_version
from sphinx_rtd_theme import __version_full__ as theme_version_full
from sphinx.locale import _
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = u'NHSX Data Engineering'
version = '0.0.1'
release = '0.0.1'
copyright = '2021 NHSX, MIT Licence'
author = 'Craig R Shenton, Mattia Ficarelli'
language = 'en'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinxcontrib.httpdomain',
    'sphinx_rtd_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

gettext_compact = False
master_doc = 'index'
pygments_style = 'default'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_favicon = "_static/favicon.png"

html_logo = "_static/logo-wordmark-light.svg"

html_theme_options = {
    "style_external_links": False,
    "style_nav_header_background": "#2980B9",
    "navigation_depth": -1,
    'logo_only': False,
}

html_css_files = [
    "css/theme_overrides.css",  # override wide tables in RTD theme
]
