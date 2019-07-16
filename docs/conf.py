# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import sys

import pkg_resources

# -- Path setup --------------------------------------------------------------

sys.path.insert(0, os.path.abspath('../src/'))
#sys.path.insert(0, os.path.abspath('../src/pudl/'))

# -- Project information -----------------------------------------------------

project = 'PUDL'
copyright = '2019, Catalyst Cooperative'
author = 'Catalyst Cooperative'

# The full version, including alpha/beta/rc tags
release = pkg_resources.get_distribution('pudl').version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
]

# List of packages that should not really be installed, because they are
# written in C or have C extensions. Instead they should be mocked for import
# purposes only to prevent the doc build from failing.
autodoc_mock_imports = ['snappy', 'python-snappy']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

master_doc = 'index'
html_theme = 'sphinx_rtd_theme'
html_logo = '_static/catalyst_logo-200x200.png'
html_icon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
