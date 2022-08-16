---
date: 2022-08-17 00:00:00 +1200
title: Connect to Azure SQL Database in a Jupyter Notebook using Python
author: Luke
categories:
- Azure
toc: false
header:
  teaser: "/uploads/juptyer_notebook.png"

---
up an [Jupyter](https://jupyter.org/ "Jupyter") Notebook's, commonly used by Data Scientists and students, allow you to run code, such as Python and PowerShell, inside a Notebook format, and display the output inside the notebook, this is really useful for teaching a subject or displaying up-to-date information.

I am not a python or Jupyter expert, so this article will be brief on how I was able to connect to an Azure SQL Database using Azure Active Directory authentication and run a query.

To run a Jupyther Notebook, you can install [Anaconda](https://www.anaconda.com/products/distribution "Anaconda"), and then use that to download Juypter to run the notebooks from a locally _(or server)_ hosted web-based interface.

However, today I will be using Visual Studio Code with the [Jupyter extension](https://code.visualstudio.com/docs/datascience/jupyter-notebooks " Jupyter Notebooks in VS Code ") on a windows endpoint.

Make sure you install:

* [Python](https://www.python.org/downloads/ "Python")
* [pyodbc](https://pypi.org/project/pyodbc/ "pyodbc ") library
* [Microsoft ODBC Driver for SQL Sever](https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server "Microsoft ODBC Driver for SQL Server") _(has to be v17 or newer to support Azure Active Directory authentication)_.
* [Visual Studio Code](https://code.visualstudio.com/ "Visual Studio Code") + [Jupyter extension](https://code.visualstudio.com/docs/datascience/jupyter-notebooks " Jupyter Notebooks in VS Code ")

_Note: Jupyter notebook extensions end in '*.ipynb'._

Once all the prerequsites are installed, its time to create the Notebook.

1. Open Visual Studio Code
2. Click File, New File
3. Select Jupyter Notebook
4. Press + Code _(to add a Code snippet)_
5. First we need to import the pyodbc library:

    \#Libraries
    import pyodbc

Then we need to add the snippet to connect to the SQL database _(this can be in a seperate Codeblock or the same codeblock, as long as the import is ran before the SQL connection is made)_:

    #Connection to SQL database
    
    
    server = 'tcp:SQLSERVER.database.windows.net' 
    database = 'DBNAME' 
    username = 'user@contoso.com' 
    password = 'password' 
    
    
    connection = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server='+server+',1433;Database='+database+';Uid='+username+';Pwd='+password+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=180;Authentication=ActiveDirectoryInteractive')
    cursor = connection.cursor()