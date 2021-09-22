****************************
Azure Data Factory Templates 
****************************

Open access and reusable design documentation of pipelines used in the NHSX Analytics Unit Azure Data Factory (ADF) environment.

SQL Database Ingestion Pipeline
===============================

**Developed by:** Craig Shenton and Mattia Ficarelli 

Template name: ``ingestion_sql``

Here we develop a template solution in Azure Data Factory. The Azure Data Factory json configuration file is `available below <#json-configuration>`_.

.. image:: _static/img/pipeline_temps/sql-ingest.png
  :width: 600
  :alt: Data ingestion from a SQL database
*Figure 1: Data ingestion from a SQL database*

Description
-----------

Pipeline to ingest raw data in a time-stamped folder to Azure Datalake blob storage from a SQL database.

 1. Lookups the JSON configuration file for this pipeline
 2. Source:

    a. Sets the source database owner (dbo)
    b. Sets the source table
    c. Sets the SQL query

 3. Sink:

    a. Sets the file system
    b. Sets the sink path
    c. Sets the sink file

 4. Copy activity copies the data returned from the SQL query as either a .csv file or a .parquet file.
 5. If the copy activity fails, the error notification logic app API will notify the specified email address of the error

Pipeline Configuration
----------------------

.. code:: json

    {
      "pipeline": {
        "name": "ingestion_sql",
        "folder": "templates/ingestion/sql",
        "adl_file_system": "file_system",
        "raw": {
          "source_dbo": "dbo",
          "source_table": "table_1",
          "source_query": "SELECT * FROM dbo.table_1 ORDER BY Date DESC",
          "sink_path": "raw/path/to/data",
          "sink_file": "table_1.parquet"
        }
    }

JSON Configuration
------------------

Download the Azure Data Factory json configuration file to use this template in your own data pipelines.

:download:`sql-ingestion.json <https://raw.githubusercontent.com/nhsx/au-data-engineering/main/config-files/adf-templates/sql-ingestion.json>`

