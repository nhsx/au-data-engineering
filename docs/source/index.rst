**************************
Read the Docs Sphinx Theme
**************************

This Sphinx_ theme was designed to provide a great reader experience for
documentation users on both desktop and mobile devices. This theme is used
primarily on `Read the Docs`_ but can work with any Sphinx project. You can find
a working demo of the theme in the `theme documentation`_

.. _Sphinx: http://www.sphinx-doc.org
.. _Read the Docs: http://www.readthedocs.org
.. _theme documentation: https://sphinx-rtd-theme.readthedocs.io/en/latest/

Installation
============

This theme is distributed on PyPI_ and can be installed with ``pip``:

.. code:: console

   $ pip install sphinx-rtd-theme

To use the theme in your Sphinx project, you will need to add the following to
your ``conf.py`` file:

.. code:: python

    import sphinx_rtd_theme

    extensions = [
        ...
        "sphinx_rtd_theme",
    ]

    html_theme = "sphinx_rtd_theme"

For more information read the full documentation on `installing the theme`_

.. _PyPI: https://pypi.python.org/pypi/sphinx_rtd_theme
.. _installing the theme: https://sphinx-rtd-theme.readthedocs.io/en/latest/installing.html


.. toctree::
   :caption: Data Engineering

   designprinciples

.. toctree::
   :caption: Open Analytics

   openanalyticstemplate

.. toctree::
   :caption: Appendix

   changelog