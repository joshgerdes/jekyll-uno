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
[Jupyter](https://jupyter.org/ "Jupyter") Notebook's, commonly used by Data Scientists and students, allow you to run code, such as Python and PowerShell, inside a Notebook format, and display the output inside the notebook, this is really useful for teaching a subject or displaying up-to-date information.

I am not a python or Jupyter expert, so this article will be brief on how I was able to connect to an Azure SQL Database and run a query. 

To run a Jupyther Notebook, you can install [Anaconda](https://www.anaconda.com/products/distribution "Anaconda"), and then use that to download Juypter to run the notebooks from a locally _(or server)_ hosted web-based interface.

However, today I will be using Visual Studio Code with the [Jupyter extension](https://code.visualstudio.com/docs/datascience/jupyter-notebooks " Jupyter Notebooks in VS Code ") on a windows endpoint.

Make sure you install:

* [Python](https://www.python.org/downloads/ "Python")
* pyodbc libraries _(pip install pyodbc)_

_Note: Jupyter notebook extensions end in '*.ipynb'._