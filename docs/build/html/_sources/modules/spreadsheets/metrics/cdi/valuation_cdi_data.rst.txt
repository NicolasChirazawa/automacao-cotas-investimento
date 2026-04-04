.. _valuation_cdi:

CDI Valuation Data
==================

* :ref:`extract_json_cdi_valuation_sec`
* :ref:`create_dataframe_personalized_cdi_valuation_sec`
* :ref:`create_new_archive_cdi_valuation_sec`

.. _extract_json_cdi_valuation_sec:

Extract Data from options.json
------------------------------

Using the ``METRICS/CDI`` key in ``options.json``, two parameters are retrieved.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Name
     - Description
   * - ``START_DATE``
     - Optional parameter (YYYY-MM-DD).
   * - ``END_DATE``
     - Optional parameter (YYYY-MM-DD).

.. _create_dataframe_personalized_cdi_valuation_sec:

Create and Adjust a Pandas DataFrame for CDI
--------------------------------------------

The ``START_DATE`` and ``END_DATE`` parameters are used to control how CDI data is processed.

.. tip::
   If ``START_DATE`` or ``END_DATE`` is not present in ``options.json`` during execution, the program automatically updates the file by:

   - Setting ``START_DATE`` to the earliest available date;
   - Setting ``END_DATE`` to the latest available date.

The ``CDI_TAX`` column is removed, and a new column, ``VALUATION_PERCENT``, is added to calculate the cumulative return. This calculation follows specific rules:

- The first valid date (row date greater than or equal to ``START_DATE``) is set to 0.00% and used as the baseline for future calculations.

.. _create_new_archive_cdi_valuation_sec:

Create a New File with CDI Valuation
------------------------------------

The program generates a new file named ``cdi_valuation.csv`` in the ``/data`` directory.

.. warning::
   This section does not describe low-level implementation details. It focuses only on the main components and on aspects that may cause confusion.