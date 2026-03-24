.. _json_configuration:

JSON Configuration
==================

At the root of the project, there is a file named ``options_template.json``.
Make a copy of this file and remove the ``_template`` suffix from its name.

This file is divided into five main sections:

* :ref:`config_section`
* :ref:`dir_section`
* :ref:`investments_section`
* :ref:`charts_section`
* :ref:`redeem_section`

.. _config_section:

CONFIG
------

Defines the date range for data extraction.

**Parameters**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Name
     - Description
   * - ``START_DATE``
     - Start date (YYYY-MM-DD)
   * - ``END_DATE``
     - End date (YYYY-MM-DD)

**Example**

.. code-block:: json

    {
        "CONFIG": {
            "START_DATE": "2023-01-01",
            "END_DATE": "2023-12-31"
        }
    }

.. _dir_section:

DIR
---

Defines the directory structure used in the project.


**Structure**


* ``CVM``: Data from the *Comissão de Valores Mobiliários*

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Name
     - Description
   * - ``CSV_NAME``
     - Directory containing ``.csv`` files
   * - ``DATA_NAME``
     - Directory containing processed data

* ``METRICS``: Data from economic indicators

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Name
     - Description
   * - ``CDI``
     - Directory containing processed CDI (Certificado de Depósito Interbancário) data

**Example**

.. code-block:: json

    {
        "DIR": {
            "CVM": {
                "CSV_NAME": "csv",
                "ZIP_NAME": "zip",
                "DATA_NAME": "processed"
            },
            "METRICS": {
                "CDI": "cdi"
            }
        }
    }

.. _investments_section:

INVESTMENTS
-----------

Defines the list of investments selected by the user.

Each investment is identified by its **CNPJ**, using the format:
``XX.XXX.XXX/XXXX-XX``.

**Parameters**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Description
   * - ``INVESTMENT_FUND``
     - Name of the investment fund
   * - ``PURCHASE_DATE``
     - Purchase date (YYYY-MM-DD)
   * - ``SOLD_DATE``
     - Sell date (YYYY-MM-DD)
   * - ``QUOTAS``
     - Number of shares (quotas)
   * - ``INVESTMENT_QUOTA``
     - Application settlement (D0, D1, D2)
   * - ``REDEEM_QUOTA``
     - Redemption settlement (D0, D1, D2)

**Example**

.. code-block:: json

    {
        "INVESTMENTS": {
            "12.345.678/0001-99": {
                "INVESTMENT_FUND": "Example Fund",
                "PURCHASE_DATE": "2023-01-01",
                "SOLD_DATE": "2023-12-31",
                "QUOTAS": 200,
                "INVESTMENT_QUOTA": 0,
                "REDEEM_QUOTA": 0
            }
        }
    }

.. _charts_section:

CHARTS
------

Defines the data used to generate charts.

**Parameters**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Description
   * - ``INVESTMENT_LIST``
     - List of selected investments
   * - ``METRICS``
     - Selected metrics for the valuation chart

**Example**

.. code-block:: json

    "CHARTS": {
        "INVESTMENT_LIST": ["52.324.414/0001-70", "36.966.636/0001-30"],
        "METRICS": {
            "CDI": true,
            "Inflacao": false
        }
    }

.. _redeem_section:

REDEEM
------

Defines the data used for investment simulation.

**Parameters**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Description
   * - ``INVESTMENT``
     - Investment used for the simulation
   * - ``DAYS_OFFSET``
     - Number of days applied to the ``PURCHASE_DATE``

**Example**

.. code-block:: json

    "REDEEM": {
        "INVESTMENT": "52.324.414/0001-70",
        "DAYS_OFFSET": 5
    }

Prev: :doc:`index`

Next: :doc:`project_flow`