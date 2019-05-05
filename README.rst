~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Swedbank xls plugin for ofxstatement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a plug-in for `ofxstatement`_. It converts a bank statement downloaded
from the older version of the Swedbank website in XLS (Excel) format to an OFX file suitable for
importing into GnuCash.

.. _ofxstatement: https://github.com/kedder/ofxstatement

Usage::

    ofxstatement convert -t swedbankxls filename.xls filename.ofx
