.. _charts_quota_evolution:

Quota price Evolution
=====================

* :ref:`extract_json_cvm_download_sec`
* :ref:`download_archives_cvm_download_sec`
* :ref:`extracting_archives_cvm_download_sec`

.. _extract_json_cvm_download_sec:

Extract options.json data
-------------------------

CVM data is downloaded using the ``START_DATE`` and ``END_DATE`` parameters defined in ``options.json``.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Name
     - Description
   * - ``START_DATE``
     - Required parameter (YYYY-MM-DD).
   * - ``END_DATE``
     - Optional parameter (YYYY-MM-DD). If provided, data is downloaded up to this date; otherwise, the current date is used.

.. note::
   If ``END_DATE`` is not present in ``options.json`` during execution, the program automatically updates the file by setting ``END_DATE`` to the current date.

Using this information, the program iterates through all months between ``START_DATE`` and ``END_DATE``.

.. _download_archives_cvm_download_sec:

Download Status
---------------

After downloading archives from CVM in a month-year schema, the program stores the ``.zip`` files in their respective directories on ``/data``.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Status
     - Description
   * - 200
     - A ``.zip`` archive is successfully returned for the requested month.
   * - 404
     - Link not found. The program logs the corresponding month/year with issues.

.. _extracting_archives_cvm_download_sec:

Extraction Status
-----------------

After extracting the archives from the ``.zip`` directory, the program creates a new directory containing all monthly ``.csv`` data on ``/data``.

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Status
     - Description
   * - Success
     - Archives were successfully extracted.
   * - Failed
     - No archives were found in the ``CVM/ZIP`` directory.

.. warning::
   This section does not describe low-level implementation details. It focuses only on the main components and on aspects that may cause confusion.