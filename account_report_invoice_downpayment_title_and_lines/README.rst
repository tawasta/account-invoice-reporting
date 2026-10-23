.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

======================================================
Account Invoice Report - Down Payment Title and Lines
======================================================

Intended for customers who invoice down payments from sales orders and need the
resulting PDF to say so.

* Titles a down payment invoice "Down payment" in the document title and in the
  PDF page header. Core titles it "Invoice", because a down payment invoice is a
  normal customer invoice for core.

* Lists the ordered products of the sales order below the invoice totals. Core
  only prints the down payment line itself, so the customer cannot see what the
  payment is for.

The invoice is recognised as a down payment invoice with core's own
``_is_downpayment()``, i.e. every sales order line behind the invoice lines is a
down payment line. A final invoice that deducts an earlier down payment keeps its
normal title.

Configuration
=============
\-

Usage
=====
* Create a down payment invoice from a sales order and print it. The title reads
  "Down payment" and the ordered products are listed under the totals.

Known issues / Roadmap
======================
* The order lines table has no totals row, since the invoice itself already
  prints the totals of the amount due.

Credits
=======

Contributors
------------

* Joonas Lahtinen <joonas.lahtinen@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/web/image/website/1/logo/Futural
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
