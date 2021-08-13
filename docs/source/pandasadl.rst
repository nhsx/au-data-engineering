************************
Azure DataLake to Pandas
************************

Upload
======

.. code:: python

    path = "/folder/"
    file_name = "file.csv"
    ​
    file_system_client.create_directory(path)
    directory_client = file_system_client.get_directory_client(path)
    file_client = directory_client.create_file(file_name)
    file_contents = io.BytesIO()
    df.to_csv(file_contents)
    file_length = file_contents.tell()
    file_client.upload_data(file_contents.getvalue(), length=file_length, overwrite=True)

