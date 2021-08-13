************************
Azure DataLake to Pandas
************************

Azure function app to pull/push Azure Datalake files to ``pandas`` dataframe in memory. To avoid the 500mb limit of the ``tmp/`` folder.

Metadata
========

.. code:: python

    #!/usr/bin python3

    # -------------------------------------------------------------------------
    # Copyright (c) 2021 NHS England and NHS Improvement. All rights reserved.
    # Licensed under the MIT License. See license.txt in the project root for
    # license information.
    # -------------------------------------------------------------------------

    """
    FILE:           pandas2adl.py
    DESCRIPTION:
                    pandas2adl func app
    USAGE:
                    ...
    CONTRIBUTORS:   Craig Shenton, Mattia Ficarelli
    CONTACT:        data@nhsx.nhs.uk
    CREATED:        09 Aug 2021
    VERSION:        0.0.1
    """

Imports
=======

.. code:: python

    # Imports
    # -------------------------------------------------------------------------

    # Python:
    import os
    import io

    # 3rd party:
    import pandas as pd
    from azure.storage.filedatalake import DataLakeServiceClient

    # Internal:
    import azure.functions as func

Download
========

.. code:: python

    # Download from Azure datalake to pandas dataframe
    # -------------------------------------------------------------------------
    FILE_PATH = "folder/"
    FILE_NAME = "file.csv"
    FS = "adl_file_system"
    # !env from func application settings
    CONNECTION_STRING = os.getenv("CONNECTION_STRING")

    service_client = DataLakeServiceClient.from_connection_string(CONNECTION_STRING)
    file_system_client = service_client.get_file_system_client(file_system=FS)
    directory_client = file_system_client.get_directory_client(FILE_PATH)
    file_client = directory_client.get_file_client(FILE_NAME)
    download = file_client.download_file()
    downloaded_bytes = download.readall()
    df = pd.read_csv(io.BytesIO(downloaded_bytes))

Upload
======

.. code:: python

    # Upload pandas dataframe to Azure datalake
    # -------------------------------------------------------------------------
    FILE_PATH = "folder/"
    FILE_NAME = "file.csv"
    FS = "adl_file_system"
    # !env from func application settings
    CONNECTION_STRING = os.getenv("CONNECTION_STRING")

    service_client = DataLakeServiceClient.from_connection_string(CONNECTION_STRING)
    file_system_client = service_client.get_file_system_client(file_system=FS)
    directory_client = file_system_client.get_directory_client(FILE_PATH)
    file_client = directory_client.create_file(FILE_NAME)

    file_contents = io.BytesIO()
    df.to_csv(file_contents)
    file_length = file_contents.tell()
    file_client.upload_data(
      file_contents.getvalue(),
      length=file_length,
      overwrite=True)

