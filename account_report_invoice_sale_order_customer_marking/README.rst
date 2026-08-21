.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===================================================
Account Report Invoice: Sale Order Customer Marking
===================================================

Adds a ``customer_marking`` field to invoices, computed from the customer
marking(s) of the related sale order(s) (``account.move.sale_order_ids``,
from ``account_invoice_related_sale_order``). If an invoice originates from
several sale orders with different markings, all distinct values are shown,
comma-separated.

Shows the value on the invoice PDF, in the same "informations" row as
**Source** and **Customer Code**, right after **Customer Code**.

Configuration
=============
\-

Usage
=====
Install this module from Apps. The field appears on the invoice form, next
to **Order Reference**, and on the printed invoice next to **Customer
Code**, whenever a related sale order has a customer marking set.

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Valtteri Lattu <valtteri.lattu@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
