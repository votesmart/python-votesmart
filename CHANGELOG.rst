python-votesmart changelog
==========================

dev
-----
* new votes.getByBillNumber and officials.getStatewide methods
* Fixed __repr__ so that eval(repr(obj)) == obj for all VotesmartApiObjects

0.2.1
-----
* fixes to places where PVS returns single items where lists are expected
* fix allowing fetching of BillDetail amendments (thanks Josh Eastburn)

0.2.0
-----
* first public release (superceded unpythonic internal library)

