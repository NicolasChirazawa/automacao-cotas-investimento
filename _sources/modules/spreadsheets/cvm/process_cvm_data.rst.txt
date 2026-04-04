.. _process_cvm:

Process CVM Data
================

* :ref:`extract_json_cvm_processed_sec`
* :ref:`create_dataframe_personalized_cvm_process_sec`
* :ref:`create_processed_csv_cvm_process_sec`

.. _extract_json_cvm_processed_sec:

Extract data from options.json
------------------------------

Using the ``INVESTMENTS`` key in ``options.json``, a list is created containing all selected investments.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Name
     - Description
   * - ``INVESTMENTS``
     - Required parameter. A list of investment fund CNPJs extracted from ``json_data``.
   * - ``PURCHASE_DATE``
     - Optional parameter (YYYY-MM-DD).
   * - ``SOLD_DATE``
     - Optional parameter (YYYY-MM-DD).

.. _create_dataframe_personalized_cvm_process_sec:

Create and Adjust a Pandas DataFrame for Investment Data
--------------------------------------------------------

The ``PURCHASE_DATE`` and ``SOLD_DATE`` parameters are used to control how data is processed individually for each investment.

Filtering is limited to the available data range (i.e., the ``START_DATE`` and ``END_DATE`` defined earlier), since this range represents the data processed by the system.

.. tip::
    If ``PURCHASE_DATE`` or ``SOLD_DATE`` is not present in ``options.json`` during execution, the program automatically updates the file by:
    
    - Setting ``PURCHASE_DATE`` to the earliest available date;
    - Setting ``SOLD_DATE`` to the latest available date.

The resulting DataFrame is sorted by CNPJ and date.

A new column is added containing the investment fund name defined by the user in the ``INVESTMENT_FUND`` key.

Another column is added to calculate the investment valuation. This calculation follows specific rules:

- If the row date is earlier than ``PURCHASE_DATE``, the valuation is set to 0.00%;
- The first valid date (row date greater than or equal to ``PURCHASE_DATE``) is set to 0.00% and used as the baseline for future calculations;

.. _create_processed_csv_cvm_process_sec:

Create Processed CSV Files
--------------------------

Using the processed DataFrame, the program generates individual ``.csv`` files for each investment fund.

.. warning::
   This section does not describe low-level implementation details. It focuses only on the main components and aspects that may cause confusion.