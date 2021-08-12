***********************
Open Analytics Template
***********************

.. contents:: Table of Contents

The `Open Analytics <https://github.com/nhsx/open-analytics-template>`__ project has been developed using an end-to-end open source analytics pipeline consisting four key components:

#. **GitHub API** (https://docs.github.com/en/rest/reference/orgs): We use the open API to pull data from open health repositoiries as ``json`` files that are flattened into ``pandas`` dataframes for analysis.
#. **Plotly.py** (https://plotly.com/graphing-libraries/): An open source python graphing library is used to plot the repository data as tables and interactive charts.
#. **GitHub Actions** (https://github.com/features/actions): Used to orchestrate and automate the first two components on a schedule and commit those changes back to the project's repository.
#. **GitHub.io Pages** (https://pages.github.com/): We host and publish the results of our analysis to a static website that is re-built on every new commit.

The four components come together to create a very light and reusable pipeline for open analytics.

GitHub API
==========

An API (Application Program Interface) allows us to access web tools or data in the cloud. The Github API's are designed so that we can create and manage our repositories, branches, issues, pull requests programmatically. Typically you would need to sign into your own account to access these features, but some information is publicly available. In this project we are using the API to access publicly available information on open source repositories published by NHS and health related organisations.

We use the ``urllib.request`` python library to access the API as follows:

.. code-block:: python
   :linenos:
   :caption: GitHub API url.

   url = (
         "https://api.github.com/orgs/"  # github REST call
         + org_id                        # organisation github name
         + "/repos?page="                # list of open repos
         + str(page)                     # page count
         + "&per_page=100"               # no of results per page
         )

Note: you can only make 60 calls per hour to the publich GitHub API, so we need to bear this in mind when looping through the API calls.

The outputs of the API call returns a ``json`` file from which we can flatten to a ``panads`` dataframe.

.. code-block:: python
   :linenos:
   :caption: Flatten JSON to a panads dataframe.

   flat_data = pd.json_normalize(data)


We can then do some basic calculations to summerise these data. For example, count the number of repositores by each organisation.

.. code-block:: python
   :linenos:
   :caption: Group repositories by organisation and date.

   aggregate = (
      df.groupby(["org", "date"])
      .sum()
      .reset_index()
   )


