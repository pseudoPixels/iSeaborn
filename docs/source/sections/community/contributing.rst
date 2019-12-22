Contributing
============
If you are planning to contribute to iSeaborn, you will first need to set up a local development
environment.

Environment Setup and Dev Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Install Python. Python 3.6 or above recommended, but our CI/CD pipeline currently tests against
   up-to-date patch versions of Python 2.7, 3.5, 3.6, and 3.7.

2. Create and activate a virtualenv, using the tool of your choice:

.. code-block:: console

    $ conda create -n iSeabornEnv python=3.6
    $ conda activate iSeabornEnv


3. Clone the dagster repository to the destination of your choice:

.. code-block:: console

    $ git clone https://github.com/pseudoPixels/iSeaborn.git


4. Install from the setup.py in development mode:

.. code-block:: console

    $ cd iSeaborn
    $ pip install -e .



Developing Docs
~~~~~~~~~~~~~~~
The documentation of the project is created using sphinx. Our documentation employs a combination of Markdown and reStructuredText.
To build your updated docs:

.. code-block:: console

    $ cd docs
    $ make html

