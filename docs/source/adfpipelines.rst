*************************************
Azure Data Factory Pipeline Templates 
*************************************

Open access and reusable design documentation of pipelines used in the NHSX Analytics Unit Azure Data Factory (ADF) environment.

SQL Database Ingestion Pipeline
===============================

**Developed by:** Craig Shenton and Mattia Ficarelli 

Headder
-------

.. code:: bash

    root/
    ├── directory/
    │   ├── 2021-06-01/
    │   ├── 2021-06-02/
    │   ├── 2021-06-03/
    │   └── 2021-06-04/

Here we develop a template solution in Azure Data Factory. The Azure Data Factory json configuration file is `available below <#json-configuration>`_.

.. image:: _static/img/latest_folder/overview.png
  :width: 600
  :alt: Overview of the latest folder lookup ADF utility
*Figure 1: Overview of the latest folder lookup ADF utility*

**Step 1.** Create two pipeline variables: ``latestFolder`` and ``prevFolder`` (see Figure 2).
  
  * The ``latestFolder`` variable is an empty string to save the latest folder name.
  * The ``prevFolder`` variable is set to a historical date before you started collecting data for example, ‘1970-01-01’


JSON Configuration
------------------

Download the Azure Data Factory json configuration file to use this template in your own data pipelines.

:download:`latestFolder.json <https://raw.githubusercontent.com/nhsx/au-data-engineering/main/config-files/adf-utilities/latestFolder.json>`

