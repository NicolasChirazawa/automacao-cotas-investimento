Project Structure
=================

Features Relation
-----------------

.. image:: _static/images/image.png
   :alt: Project Structure
   :align: center
   :width: 700px


.. grid:: 1
   :gutter: 3

   .. grid-item-card:: 
        :doc:`🌐 Spreedsheets<spreedsheets>`

      Author in reStructuredText or MyST Markdown to create highly structured technical documents.

   .. grid-item-card::
        :doc:`📊 Charts<charts>`

      Create cross-references within your project and across different projects.

   .. grid-item-card:: 🤖 Redeem
        :doc:`🤖 Redeem<redeem>`

      Generate documentation in HTML, LaTeX, ePub, and more.

---

`app/ <https://github.com/NicolasChirazawa/automacao-cotas-investimento/tree/main/app>`_
    Main project directory.

    - ``options_template.json``: Template configuration file for project execution.

`app/data/`
    Stores all generated, processed, and consumed data.

`app/src/ <https://github.com/NicolasChirazawa/automacao-cotas-investimento/tree/main/app/src>`_
    Contains all project modules.

    - ``charts``: Generates charts for quota price evolution and percentage variation compared to economic indicators.
    - ``redeem``: Investment simulations based on processed data.
    - ``spreadsheets``: Generates spreadsheets based on the ``options_template.json`` file.
    - ``utils``: Classes and functions to standardize project development.

`docs/ <https://github.com/NicolasChirazawa/automacao-cotas-investimento/tree/main/docs/>`_
    Sphinx documentation files. All ``*.rst`` files compose sections of the documentation.


.. toctree::
   :titlesonly:
   :maxdepth: 2
   :caption: spreedsheet
   :includehidden:

   spreedsheets

.. toctree::
   :titlesonly:
   :maxdepth: 2
   :caption: spreedsheet
   :includehidden:

   redeem

.. toctree::
   :titlesonly:
   :maxdepth: 2
   :caption: spreedsheet
   :includehidden:
   
   charts
