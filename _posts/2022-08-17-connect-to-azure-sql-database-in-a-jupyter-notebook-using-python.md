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
[Jupyter](https://jupyter.org/ "Jupyter"){:target="blank"} Notebooks, commonly used by Data Scientists and Students, allow you to run code, such as Python and PowerShell, inside a Notebook format and display the output inside the notebook; this is useful for teaching a subject or displaying up-to-date information.

I am not a python or Jupyter expert, so this article will be brief on how I was able to connect to an Azure SQL Database using Azure Active Directory authentication and run a query.

To run a Jupyter Notebook, you can install [Anaconda](https://www.anaconda.com/products/distribution "Anaconda"){:target="blank"} and then use that to download Juypter to run the notebooks from a locally _(or server)_ hosted web-based interface.

However, today I will be using Visual Studio Code with the [Jupyter extension](https://code.visualstudio.com/docs/datascience/jupyter-notebooks " Jupyter Notebooks in VS Code "){:target="blank"} on a windows endpoint.

Make sure you install:

* [Python](https://www.python.org/downloads/ "Python"){:target="blank"}
* [pyodbc](https://pypi.org/project/pyodbc/ "pyodbc "){:target="blank"} library
* [Microsoft ODBC Driver for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server "Microsoft ODBC Driver for SQL Server"){:target="blank"} _(has to be v17 or newer to support Azure Active Directory authentication)_.
* [Visual Studio Code](https://code.visualstudio.com/ "Visual Studio Code") + [Jupyter extension](https://code.visualstudio.com/docs/datascience/jupyter-notebooks " Jupyter Notebooks in VS Code"){:target="blank"}

_Note: Jupyter notebook extensions end in '*.ipynb'._

Once all the prerequisites are installed, it's time to create the Notebook.

1. Open **Visual Studio Code**
2. Click **File**, **New File**
3. Select **Jupyter Notebook**
4. Press **+ Code** _(to add a Code snippet)_
5. First, we need to import the pyodbc library:

       #Libraries
       import pyodbc

Then we need to **add the snippet to connect to the SQL database** _(this can be in a separate Codeblock or the same code block, as long as the import is run before the SQL connection is made - **make sure you update the server and database variables,** to match your environment!)_:

    #Connection to SQL database
    
    
    server = 'tcp:SQLSERVER.database.windows.net' 
    database = 'DBNAME' 
    username = 'user@contoso.com' 
    password = 'password' 
    
    
    connection = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server='+server+',1433;Database='+database+';Uid='+username+';Pwd='+password+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=180;Authentication=ActiveDirectoryInteractive')
    cursor = connection.cursor()

The 'Authentication=ActiveDirectoryInteractive' parameter as part of the Connection string will prompt an interactive Azure Active Directory prompt to display and ask for credentials to be logged in; this includes MFA support. Using this method, the username and password variables are simply placeholders.

If you want to hardcode credentials into the Notebook _(not recommended)_, you can remove the '_Authentication=ActiveDirectoryInteractive_' section and enter the credentials into the username and password field.

Now that we have connected to the database, let us **run a test query to obtain the SQL version**:

    #Sample select query
    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()
    while row:
    print(row[0])
    row = cursor.fetchone()

![Jupyter python SQL connection](/uploads/juptyer_notebook_query.png)

Congratulations, you have successfully connected to an Azure SQL database and ran a query against the database.

If the connection to SQL appears to be stalling, check to make sure the Azure authentication window, isn't hidden behind another window.

_A_ [_GIST_](https://gist.github.com/lukemurraynz/6636632309bc2bf2b1b37676ee0881ce "python.sqldb.text"){:target="blank"} _has been created, with the code as well, in case issues are copied from the website._
