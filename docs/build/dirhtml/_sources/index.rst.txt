Welcome to documentation!
=========================

*Precise, fast, and personality analysis*

|python| |jupyter| |sphinx|

Overview
--------
A project that **automatically gathers, processes, and analyzes investment fund data**.

The objective is to create a solid foundation for historical analysis, data visualization, and investment simulations.

Pre-requisits
-------------

1.  Required software: 

- `Python <https://www.python.org/downloads/>`_

.. note::
    It is recommended to use `Visual Studio Code <https://code.visualstudio.com/>`_, as it provides excellent support for Jupyter Notebooks.

2.  Access to the project

Clone the repository:

.. code-block:: console
    
    # Command to clone the project
    git clone https://github.com/NicolasChirazawa/automacao-cotas-investimento.git

Or download the `.zip` repository from 'GitHub'.

3.  Install all the dependencies

The project includes a ``requirements.txt`` file in the root directory containing all required dependencies.

.. code-block:: console

    pip install -r requirements.txt

Next steps
----------
* **How to Start**

  * :doc:`JSON Configuration <JSON_configuration>`

   * Learn how to configure the project;
   * 'CONFIG' key;
   * 'DIR' key;
   * 'INVESTMENTS' key;
   * 'CHARTS' key;
   * 'REDEEM' key;

  * :doc:`Project Flow <project_flow>`

   * Learn how to configure the project;
   * 'CONFIG' key;
   * 'DIR' key;
   * 'INVESTMENTS' key;
   * 'CHARTS' key;
   * 'REDEEM' key;

   * Understand how the project is organized;

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

Next: :doc:`JSON_configuration`


.. toctree::
   :titlesonly:
   :maxdepth: 2
   :caption: How to start:
   :includehidden:

   JSON_configuration
   project_flow