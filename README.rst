================
python-votesmart
================

Python library for interacting with the Project Vote Smart API.

The Project Vote Smart API provides detailed information on politicians,
including bios, votes, and NPAT responses.
(http://votesmart.org/services_api.php)

python-votesmart is a project of Sunlight Labs (c) 2008.
Written by James Turk <jturk@sunlightfoundation.com>.

All code is under a BSD-style license, see LICENSE for details.

Homepage: http://pypi.python.org/pypi/python-votesmart/

Source: http://github.com/sunlightlabs/python-votesmart/


Requirements
============

python >= 2.4

simplejson >= 1.8 (not required with python 2.6, will use built in json module)


Installation
============
To install run

    ``python setup.py install``

which will install the library into python's site-packages directory.


Usage
=====

To initialize the api, all that is required is for it to be imported and for an
API key to be defined.

(If you do not have an API key visit http://votesmart.org/services_api.php to
register for one.)

Import ``votesmart`` from ``votesmart``:
    
    >>> from votesmart import votesmart
    
And set your API key:

    >>> votesmart.apikey = '496ec1875a7885ec65a4ead99579642c'

---------------
address methods
---------------

Official API documentation at http://api.votesmart.org/docs/Address.html

The methods ``getCampaign(candidateId)``, ``getCampaignByElection(electionId)``,
and ``getOffice(candidateId)`` all return a list of ``Address`` objects based on
the provided election or candidate id.

Example of getting Nancy Pelosi's office:

    >>> addr = votesmart.address.getOffice(26732)[0]
    >>> print addr.street, addr.city, addr.state
    District Office
    450 Golden Gate Avenue
    14th Floor San Francisco CA

``getCampaignWebAddress(candidateId)`` and ``getOfficeWebAddress(candidateId)``
return a list of ``WebAddress`` objects based on the provided election or
candidate id.

Example of getting Nancy Pelosi's web addresses:
    >>> for x in votesmart.address.getOfficeWebAddress(26732):
    ...     print x
    http://speaker.house.gov/
    http://www.house.gov/pelosi/
    http://www.house.gov/pelosi/contact/contact.html
    sf.nancy@mail.house.gov

--------------------
candidatebio methods
--------------------

Official API documentation at http://api.votesmart.org/docs/CandidateBio.html

``getBio(candidateId)`` and ``getAddlBio(candidateId)`` get a Bio object and
a series of AddlBio objects.

Example of getting Nancy Pelosi's bio:

    >>> bio = votesmart.candidatebio.getBio(26732)
    >>> print 'Born', bio.birthDate, 'in', bio.birthPlace
    Born 03/26/1940 in Baltimore, MD
    
    >>> for fact in votesmart.candidatebio.getAddlBio(26732):
    ...     print fact
    Father's Occupation: Congressman for Baltimore, Mayor of Baltimore
    Number of Grandchildren: 5

------------------
candidates methods
------------------

Official API documentation at http://api.votesmart.org/docs/Candidates.html

* ``getByOfficeState(officeId, stateId=None, electionYear=None)``
* ``getByLastname(lastName, electionYear=None)``
* ``getByLevenstein(lastName, electionYear=None)``
* ``getByElection(electionId)``
* ``getByDistrict(districtId, electionYear=None)``

All five methods return a list containing one or more Candidate objects.

Example of fetching all candidates for the MN Senate race:

    >>> for candidate in votesmart.candidates.getByOfficeState(6, 'MN'):
    ...    print candidate
    Norm Coleman
    Al Franken


-----------------
committee methods
-----------------

Official API documentation at http://api.votesmart.org/docs/Committee.html

``getTypes()`` returns a listing of all CommitteeType.

Example:

    >>> for c in votesmart.committee.getTypes():
    ...     print c.committeeTypeId, c.name
    H House
    S Senate
    J Joint

``getCommitteesByTypeState(typeId=None, stateId=None)`` returns a listing of
Committee objects, if either typeId isn't specified all committees for that
state will be returned, if state isn't specified then congressional committees
will be returned.

Example of getting all joint committees:

    >>> for c in votesmart.committee.getCommitteesByTypeState(typeId='J'):
    ...     print c
    Joint Committee on Printing
    Joint Committee on Taxation
    Joint Committee on the Library of Congress
    Joint Economic Committee

``getCommittee(committeeId)`` get extended details on a committee in a
CommitteeDetail object.

Example of getting details on the House Ways & Means committee:

    >>> committee = votesmart.committee.getCommittee(23)
    >>> print committee.jurisdiction
    1. Customs revenue, collection districts, and ports of entry and delivery. 
    2. Reciprocal trade agreements. 
    3. Revenue measures generally. 
    4. Revenue measures relating to insular possessions. 
    5. Bonded debt of the United States, subject to the last sentence of clause 4(f). 
    6. Deposit of public monies. 
    7. Transportation of dutiable goods. 
    8. Tax exempt foundations and charitable trusts. 
    9. National social security (except health care and facilities programs that are supported from general revenues as opposed to payroll deductions and except work incentive programs).

``getCommitteeMembers(committeeId)`` gets a list of CommitteeMember objects
representing members of the given committee.

Example of getting all members of the Subcommittee on the Constitution,
Civil Rights, and Civil Liberties:

    >>> for member in votesmart.committee.getCommitteeMembers(4015):
    ...     print member
    Representative Jerrold Nadler
    Representative Trent Franks
    Representative Stephen Cohen
    Representative John Conyers
    Representative Artur Davis
    Representative Keith Ellison
    Representative Darrell Issa
    Representative James Jordan
    Representative Steve King
    Representative Mike Pence
    Representative Robert Scott
    Representative Debbie Wasserman Schultz
    Representative Melvin Watt

----------------
district methods
----------------

Official API documentation at http://api.votesmart.org/docs/District.html

``getByOfficeState(officeId, stateId, districtName=None)`` gets a list of
District objects matching the specified criteria.

Example of getting all House districts for North Carolina:

    >>> for district in votesmart.district.getByOfficeState(5, 'NC'):
    ...     print district
    District 1
    District 2
    District 3
    District 4
    District 5
    District 6
    District 7
    District 8
    District 9
    District 10
    District 11
    District 12
    District 13

----------------
election methods
----------------

Official API documentation at 

``getElection(electionId)`` fetches a single Election object by electionId.

Example of getting details on NC 2008 Gubernatorial election:

    >>> election = votesmart.election.getElection(684)
    >>> print election.name
    North Carolina Gubernatorial 2008
    >>> for stage in election.stages:
    ...     print stage.name, stage.electionDate
    Primary 2008-05-06
    General 2008-11-04


``getElectionByYearState(year, stateId=None)`` gets all Election objects
matching a given criteria.  If stateId is not specified it defaults to national
elections.

Example of getting details on all elections in North Carolina in 2008:

    >>> for election in votesmart.election.getElectionByYearState(2008, 'NC'):
    ...     print election
    North Carolina Congressional 2008
    North Carolina Gubernatorial 2008
    North Carolina State Legislative 2008
    North Carolina State Judicial 2008


``getStageCandidates(electionId, stageId, party=None, districtId=None, stateId=None)``
gets a list of StageCandidate objects matching the given criteria.

Example of getting all North Carolina 2008 Gubernatorial primary candidates:

    for candidate in votesmart.election.getStageCandidates(684, 'P')

------------------
leadership methods
------------------

Official API documentation at http://api.votesmart.org/docs/Leadership.html

``getPositions(stateId=None, officeId=None)`` gets a list of LeadershipPosition
objects matching the given criteria.

Example of getting all Alaska leadership positions:

    >>> for pos in votesmart.leadership.getPositions('AK'):
    ...     print pos.officeName, pos.name
    State House Speaker
    State Senate President
    State House Majority Leader
    State Senate Majority Leader
    State House Minority Leader
    State Senate Minority Leader

-------------
local methods
-------------

Official API documentation at http://api.votesmart.org/docs/Local.html

``getCounties(stateId)`` and ``getCities(stateId)`` return lists of counties or
cities as Locality objects.

Example of getting all cities in Alaska:

    >>> for city in votesmart.local.getCities('AK'):
    ...     print city.name, city.localId
    Anchorage 1
    Fairbanks 2
    Juneau 4322
    
``getOfficials(localId)`` gets all Officials known for a given locality.

Example of getting all officials from Anchorage, AK:

    >>> for official in votesmart.local.getOfficials(1):
    ...     print official
    Mayor Mark Begich
    Assembly Member Chris Birch
    Assembly Member Matt Claman
    Assembly Member Dan Coffey
    Assembly Member Harriet Drummond
    Assembly Member Patrick Flynn
    Assembly Member Elvi Gray-Jackson
    Assembly Member Mike Gutierrez
    Assembly Member Jennifer Johnston
    Assembly Member Debbie Ossiander
    Assembly Member Sheila Selkregg
    Assembly Member Bill Starr

---------------
measure methods
---------------

Official API documentation at http://api.votesmart.org/docs/Measure.html

``getMeasuresByYearState(year, stateId)`` gets a list of Measure objects for
the provided year and state.

Example of getting all 2008 Maryland Ballot Measures:

    >>> for measure in votesmart.measure.getMeasuresByYearState(2008, 'MD'):
    ...     print measure.measureId, measure.title
    1260 Video Lottery
    1261 Early Voting

``getMeasure(measureId)`` gets a MeasureDetail object providing more details
about a particular measure.

Example of getting more details on Maryland 2008 Early Voting measure:

    >>> measure = votesmart.measure.getMeasure(1260)
    >>> print measure.source       # just print the url -- summary is long
    http://www.elections.state.md.us/elections/2008/questions/index.html

------------
npat methods
------------

Official API documentation at http://api.votesmart.org/docs/Npat.html

NPATs are not converted into objects, the getNpat method is exceptional in that
it returns a python dict representing the NPAT in question.

Example of checking John McCain's NPAT:

    >>> print votesmart.npat.getNpat(53270)['surveyMessage']
    repeatedly refused to provide any responses to citizens on the issues through the 2008 Political Courage Test when asked to do so by national leaders of the political parties, prominent members of the media, Project Vote Smart President Richard Kimball, and Project Vote Smart staff.

--------------
office methods
--------------

Official API documentation at 

-----------------
officials methods
-----------------

Official API documentation at 

--------------
rating methods
--------------

Official API documentation at 

-------------
state methods
-------------

Official API documentation at 

-------------
votes methods
-------------

Official API documentation at 
