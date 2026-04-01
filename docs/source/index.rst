Welcome to the Documentation!
=============================

*Precise, fast, and reliable data analysis*

|python| |jupyter| |sphinx|

Overview
--------
A project that **automatically gathers, processes, and analyzes investment fund data**.

The objective is to provide a solid foundation for historical analysis, data visualization, and investment simulations.


Prerequisites
-------------

- **Required software:**

  - `Python <https://www.python.org/downloads/>`_

  .. note::
     It is recommended to use `Visual Studio Code <https://code.visualstudio.com/>`_, as it provides excellent support for Jupyter Notebooks.

- **Access to the project**

  Clone the repository:

  .. code-block:: console

     git clone https://github.com/NicolasChirazawa/automacao-cotas-investimento.git

ㅤ Or download the ``.zip`` file from GitHub.

- **Install dependencies**

  The project includes a ``requirements.txt`` file in the root directory containing all required dependencies.

  .. code-block:: console

     pip install -r requirements.txt


Next Steps
----------

**Getting Started**

- :ref:`JSON Configuration <json_configuration>`

  - Learn how to configure the project
  - Understand the ``CONFIG`` key
  - Understand the ``DIR`` key
  - Understand the ``INVESTMENTS`` key
  - Understand the ``CHARTS`` key
  - Understand the ``REDEEM`` key

- :ref:`Project Flow <project_flow>`

  - Understand the project features
  - Learn how features communicate with each other
  - Comprehend the overall project structure

- :ref:`Spreadsheet <spreadsheet>`

  - Learn how to use the ``spreadsheet`` feature;
  - Download and process only the data relevant to you;
  -  Available ``CVM`` and ``CDI`` data;

- :ref:`Charts <charts>`

  - Learn how to use the ``charts`` feature;
  - Make various graphs that help the readability of data;

- :ref:`Redeem <redeem>`

  - Learn how to **simulate** investments;

Questions / Comments
--------------------
If you have questions about this project, feel free to open an issue on GitHub  
`here <https://github.com/NicolasChirazawa/automacao-cotas-investimento/issues>`_.


.. |python| image:: https://img.shields.io/static/v1?label=%20&labelColor=9cccf4&message=Python&color=grey&style=for-the-badge&logo=python&logoColor=black
   :class: inline

.. |jupyter| image:: https://img.shields.io/static/v1?label=%20&labelColor=fcbe96&message=Jupyter&color=grey&style=for-the-badge&logo=jupyter&logoColor=black
   :class: inline

.. |sphinx| image:: https://img.shields.io/static/v1?label=%20&labelColor=ffffff&message=Sphinx&color=grey&style=for-the-badge&logo=sphinx&logoColor=black
   :class: inline

.. toctree::
   :maxdepth: 4
   :hidden:
   :caption: Getting Started

   getting_started/JSON_configuration
   getting_started/project_flow

.. toctree::
   :maxdepth: 4
   :hidden:
   :caption: Modules

   modules/spreadsheets/index
   modules/charts/index
   modules/redeem/redeem