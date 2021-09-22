*************************************
Azure Data Factory Pipeline Templates 
*************************************

Open access and reusable design documentation of pipelines used in the NHSX Analytics Unit Azure Data Factory (ADF) environment.

SQL Database Ingestion Pipeline
===============================

**Developed by:** Craig Shenton and Mattia Ficarelli 

Template name: ``ingestion_sql``

Here we develop a template solution in Azure Data Factory. The Azure Data Factory json configuration file is `available below <#json-configuration>`_.

.. image:: _static/img/latest_folder/overview.png
  :width: 600
  :alt: Overview of the latest folder lookup ADF utility
*Figure 1: Overview of the latest folder lookup ADF utility*

Description
-----------

Pipeline to ingest raw data in a time-stamped folder to Azure Datalake blob storage from a SQL database.

 *. Lookups the JSON configuration file for this pipeline.
    *. Sets the source database owner (dbo).
    *. Sets the SQL query.
    *. Sets the source table.
    *. Sets the file system.
    *. Sets the sink path.
    *. Sets the sink file.
 *. Copy activity copies the data returned from the SQL query as either a .csv file or a .parquet file. 
 *. If the copy activity fails, fails, the error notification logic app API will notify the specified email address of the error.

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

:download:`latestFolder.json <https://raw.githubusercontent.com/nhsx/au-data-engineering/main/config-files/adf-utilities/latestFolder.json>`

