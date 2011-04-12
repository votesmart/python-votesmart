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

    >>> votesmart.apikey = '<YOUR KEY>'

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
    235 Cannon House Office Building Washington DC

``getCampaignWebAddress(candidateId)`` and ``getOfficeWebAddress(candidateId)``
return a list of ``WebAddress`` objects based on the provided election or
candidate id.

Example of getting Nancy Pelosi's web addresses:
    >>> for x in votesmart.address.getOfficeWebAddress(26732):
    ...     print x
    https://pelosi.house.gov/contact/email-me.shtml
    http://www.house.gov/pelosi/
    AmericanVoices@mail.house.gov

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
* ``getByZip(zip5, zip4=None)``

All six methods return a list containing one or more Candidate objects.

Example of fetching all candidates for the NJ Gubernatorial race:

    >>> for candidate in votesmart.candidates.getByOfficeState(3, 'NJ'):
    ...    print candidate
    Christopher Christie
    Christopher Christie
    Jon Corzine
    Jon Corzine
    Jason Cullen
    Christopher Daggett
    Kenneth Kaplan
    Joshua Leinsdorf
    Brian Levine
    Alvin Lindsay
    David Meiswinkle
    Richard Merkt
    Gregory Pason
    Kostas Petris
    Gary Steele
    Gary Stein

You will notice that several candidates appear twice, this is due to an
unfortunate issue with the Vote Smart API where candidates with multiple
parties, or election statuses are duplicated.  Be careful when consuming
candidate data to dedupe using the fields you find useful.

(See http://github.com/sunlightlabs/python-votesmart/issues/closed/#issue/1)

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
    Joint Committee on the Library
    Joint Economic Committee

``getCommittee(committeeId)`` get extended details on a committee in a
CommitteeDetail object.

Example of getting details on the House Ways & Means committee:

    >>> committee = votesmart.committee.getCommittee(23)
    >>> print committee
    Ways and Means

``getCommitteeMembers(committeeId)`` gets a list of CommitteeMember objects
representing members of the given committee.

Example of getting all members of the Subcommittee on the Constitution,
Civil Rights, and Civil Liberties:

    >>> for member in votesmart.committee.getCommitteeMembers(4015):
    ...     print member
    Representative Trent Franks
    Representative Mike Pence
    Representative Steven Chabot
    Representative John Conyers
    Representative James Randy Forbes
    Representative James Jordan
    Representative Steve King
    Representative Jerrold Nadler
    Representative Mike Quigley
    Representative Robert Scott


----------------
district methods
----------------

Official API documentation at http://api.votesmart.org/docs/District.html

``getByOfficeState(officeId, stateId, districtName=None)`` and ``getByZip(zip5, zip4=None)`` return a list of
District objects matching the specified criteria.

Example of getting all House districts for North Carolina:

    >>> for district in votesmart.district.getByOfficeState(5, 'NC'):
    ...     print district
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13

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


``getElectionByYearState(year, stateId=None)`` and ``getElectionByZip(zip5, zip4=None, year=None)`` get all Election objects
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
    State Senate Majority Leader
    State House Majority Leader
    State Senate Minority Leader
    State House Minority Leader

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

    >>> for official in votesmart.local.getOfficials(1)[0:1]:
    ...     print official
    Mayor Mark Begich

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
    refused  to tell citizens where he/she stands on any of the issues addressed in the 2010 Political Courage Test, despite repeated requests from Vote Smart, national media, and prominent political leaders.


--e-----------
office methods
--------------

Official API documentation at http://api.votesmart.org/docs/Office.html

``getTypes()`` gets a list of OfficeType objects representing all office types
that the PVS API tracks.

Example call:

    >>> for type in votesmart.office.getTypes():
    ...     print type
    P: Presidential and Cabinet
    C: Congressional
    J: Supreme Court
    G: Governor and Cabinet
    K: State Judicial
    L: State Legislature
    S: State Wide
    H: Local Judicial
    N: Local Legislative
    M: Local Executive

``getBranches()`` gets a list of OfficeBranch objects representing all branches
that the PVS API tracks.

Example call:

    >>> for branch in votesmart.office.getBranches():
    ...     print branch
    E: Executive
    L: Legislative
    J: Judicial

``getLevels()`` gets a list of all OfficeLevel objects representing all office
levels that the PVS API tracks.

Example call:

    >>> for level in votesmart.office.getLevels():
    ...     print level
    F: Federal
    S: State
    L: Local

``getOfficesByType(typeId)``, ``getOfficesByLevel(levelId)``,
``getOfficesByTypeLevel(typeId, levelId)``, and 
``getOfficesByBranchLevel(branchId, levelId)`` return a list of Office objects
based on the provided parameters.

Example of getting all Executive titles for the Local level:

    >>> for office in votesmart.office.getOfficesByBranchLevel('E', 'L'):
    ...     print office
    Freeholder
    Mayor
    Public Advocate
    Council
    Comptroller
    Village Manager

-----------------
officials methods
-----------------

Official API documentation at http://api.votesmart.org/docs/Officials.html

* ``getStatewide(stateId=None)``
* ``getByOfficeState(officeId, stateId=None)``
* ``getByLastname(lastName)``
* ``getByLevenstein(lastName)``
* ``getByElection(electionId)``
* ``getByDistrict(districtId)``
* ``getByZip(zip5, zip4=None)``

All officials methods return a list containing one or more Candidate objects.

Example of fetching all senators from California.

    >>> for official in votesmart.officials.getByOfficeState(6, 'CA'):
    ...    print official
    Senator Barbara Boxer
    Senator Dianne Feinstein

--------------
rating methods
--------------

Official API documentation at http://api.votesmart.org/docs/Rating.html

``getCategories(stateId=None)`` gets a list of Category objects for a given
state (national if no state provided).

Example of getting a few of the issue categories for New York:

    >>> for category in votesmart.rating.getCategories('NY')[0:5]:
    ...     print category
    2: Abortion Issues
    5: Animal Rights and Wildlife Issues
    11: Business and Consumers
    13: Civil Liberties and Civil Rights
    17: Conservative

``getSigList(categoryId, stateId=None)`` gets a list of Sig objects representing
all special interest groups associated with a particular category.  Optionally
a state can be provided to restrict results to a SIG operating within a
particular state.

Example of getting a few groups concerned with Environmental Issues:

    >>> for sig in votesmart.rating.getSigList(30)[0:5]:
    ...     print sig
    934: American Lands Alliance
    1081: American Wilderness Coalition
    1702: American Wind Energy Association
    1107: California Park & Recreation Society
    292: Citizens for Health - Food, Water & Ecological Health Rating


``getSig(sigId)`` gets all details available for a special interest group.

Example getting all details for Sierra Club:

    >>> sig = votesmart.rating.getSig(657)
    >>> print sig.address, sig.city, sig.state
    408 C Street, Northeast Washington DC
    
``getCandidateRating(candidateId, sigId)`` gets a Rating object representing
a candidate's rating by a particular special interest group.

Example checking how Sierra Club rated Nancy Pelosi:

    >>> for rating in votesmart.rating.getCandidateRating(26732, 657):
    ...     print rating

-------------
state methods
-------------

Official API documentation at http://api.votesmart.org/docs/State.html

``getStateIDs()`` returns State objects for all states (and state-like entities)

Example of printing a few of the states returned from getStateIds:

    >>> for state in votesmart.state.getStateIDs()[0:5]:
    ...     print state
    NA National
    AS American Samoa
    FL Florida
    MI Michigan
    MO Missouri

``getState(stateId)`` returns a StateDetail object with all known details on
a given state.

Example of getting several details about the state of Virginia:

    >>> va = votesmart.state.getState('VA')
    >>> print va.population, va.motto
    7,882,590 (2009) Sic Semper Tyrannis [Thus Always to Tyrants]

-------------
votes methods
-------------

Official API documentation at http://api.votesmart.org/docs/Votes.html

``getCategories(year, stateId=None)`` gets a list of Category objects for a
given year and optionally a state (national if no state provided).

Example of getting a few of the national bill categories for 2008:

    >>> for category in votesmart.votes.getCategories(2008)[0:5]:
    ...     print category
    2: Abortion Issues
    4: Agriculture Issues
    5: Animal Rights and Wildlife Issues
    10: Budget, Spending and Taxes
    11: Business and Consumers

``getBill(billId)`` returns a BillDetail object providing details on a particular
bill.

Example of getting details on HR 7321 Auto Industry Financing bill:

    >>> bill = votesmart.votes.getBill(8528)
    >>> print bill.officialTitle
    HR 7321:  To authorize financial assistance to eligible automobile manufacturers, and for other purposes.
    >>> for sponsor in bill.sponsors:
    ...     print sponsor
    Barney  Frank
    >>> for action in bill.actions:
    ...     print action
    2008-12-10 - Introduced
    2008-12-10 - Passage
    

``getBillAction(actionId)`` returns a BillAction object providing details on
a particular action taken on a bill.

Example of getting details on an action for HR 5576:

    >>> print votesmart.votes.getBillAction(8272)
    HR 5576: Making appropriations for the Departments of Transportation, Treasury, and Housing and Urban Development, the Judiciary, District of Columbia, and independent agencies for the fiscal year ending September 30, 2007, and for other purposes.

``getBillActionVotes(actionId)`` and
``getBillActionVoteByOfficial(actionId, candidateId)`` retrieve lists of Vote
objects for a given action (and official).

Example of getting Nancy Pelosi's vote on passage of HR 7321:

    >>> print votesmart.votes.getBillActionVoteByOfficial(23069, 26732)
    Pelosi, Nancy: Yea


There are 8 methods that return Bill objects based on various parameters:

* ``getByBillNumber(billNumber)``
* ``getBillsByCategoryYearState(categoryId, year, stateId=None)``
* ``getBillsByYearState(year, stateId=None)``
* ``getBillsByOfficialYearOffice(candidateId, year, officeId=None)``
* ``getBillsByCandidateCategoryOffice(candidateId, categoryId, officeId=None)``
* ``getBillsBySponsorYear(candidateId, year)``
* ``getBillsBySponsorCategory(candidateId, categoryId)``
* ``getBillsByStateRecent(stateId=None, amount=None)``

Example of getting a few recently tracked bills for 2008:

    >>> for bill in votesmart.votes.getBillsByYearState(2008)[-5:]:
    ...     print bill
    HR 3997 Financial Asset Purchase Authority
    HR 7321 Automotive Industry Financing
    H Res 982 Contempt Charges
    HR 5501 Funding to Combat AIDS, Malaria, and Tuberculosis
    HR 415 Adding Parts of the Taunton River to the National Wild and Scenic Rivers System


``getVetoes(candidateId)`` returns all vetoes for a particular executive.

Example of getting all of George W. Bush's vetoes:

    >>> for veto in votesmart.votes.getVetoes(22369):
    ...     print veto
    HR 6331 Medicare Bill
    HR 6124 Second Farm, Nutrition, and Bioenergy Act of 2007 (Farm Bill)
    HR 2419 Farm, Nutrition, and Bioenergy Act of 2007 (Farm Bill)
    HR 1585 
    HR 3963 Children's Health Insurance Program Reauthorization Act of 2007 (CHIP)
    HR 976 State Children's Health Insurance Program (CHIP) Reauthorization
    S 5 Stem Cell Research Act of 2007
    HR 1591 Emergency Supplemental Appropriations Bill of 2007 with Iraq Withdrawal Timeline
