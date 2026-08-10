.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=========================================================
Account Report - Journal Items Pivot by Partner VAT
=========================================================

* Adds the partner's VAT number (``res.partner.vat``) as a field on
  Journal Items (``account.move.line``), and as a one-click "Group By"
  option on the Journal Items pivot/list report.

Configuration
=============
\-

Usage
=====
* Accounting -> Reporting -> Journal Items (or the Journal Items pivot
  view) -> Filters -> Group By -> "Partner VAT".
* The field is also available through the pivot view's own "Add Custom
  Group" option, and through the search bar for filtering.

Known issues / Roadmap
======================
* Journal items whose partner has no VAT number set are grouped under an
  empty/"None" group, same as any other empty group-by value in Odoo.

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
