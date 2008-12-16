""" Python library for interacting with Project Vote Smart API.

    Project Vote Smart's API (http://www.votesmart.org/services_api.php)
    provides rich biographical data, including data on votes, committee
    assignments, and much more.
"""

__author__ = "James Turk (jturk@sunlightfoundation.com)"
__version__ = "0.2.0"
__copyright__ = "Copyright (c) 2008 Sunlight Labs"
__license__ = "BSD"

import urllib, urllib2
try:
    import json
except ImportError:
    import simplejson as json

class VotesmartApiError(Exception):
    """ Exception for Sunlight API errors """

class votesmart(object):
    
    apikey = None
    
    @staticmethod
    def _apicall(func, params):
        if votesmart._apikey is None:
            raise VotesmartApiError('Missing Project Vote Smart apikey')
    
        url = 'http://api.votesmart.org/%s?o=JSON&key=%s&%s' % (func,
            votesmart._apikey, urllib.urlencode(params))
        try:
            response = urllib2.urlopen(url).read()
            return json.loads(response)
        except urllib2.HTTPError, e:
            raise VotesmartApiError(e.read())
        except ValueError, e:
            raise VotesmartApiError('Invalid Response')
    
    class address(object):
        @staticmethod
        def getCampaign(candidateId):
            params = {'candidateId': candidateId}
            result = votesmart._apicall('getCampaign', params)['address']['office']
    
        @staticmethod
        def getCampaignWebAddress(candidateId):
            params = {'candidateId': candidateId}
            result = votesmart._apicall('getCampaignWebAddress', params)['webaddress']['address']
                
        @staticmethod
        def getCampaignByElection(electionId):
            params = {'electionId': electionId}
            result = votesmart._apicall('getCampaignByElection', params)['address']['office']
                
        @staticmethod
        def getOffice(candidateId):
            params = {'candidateId': candidateId}
            result = votesmart._apicall('getOffice', params)['address']['office']
                
        @staticmethod
        def getOfficeWebAddress(candidateId):
            params = {'candidateId': candidateId}
            result = votesmart._apicall('getOfficeWebAddress', params)['webaddress']['address']
                
        @staticmethod
        def getOfficeByOfficeState(officeId, stateId=None):
            params = {'officeId': officeId, 'stateId': stateId}
            result = votesmart._apicall('getOfficeByOfficeState', params)['address']['office']
            
    class candidatebio(object):
        @staticmethod
        def getBio(candidateId):
            params = {'candidateId': candidateId}
            result = votesmart._apicall('getBio', params)['bio']['candidate']
            
        @staticmethod
        def getAddlBio(candidateId):
            params = {'candidateId': candidateId}
            result = votesmart._apicall('getAddlBio', params)['addlbio']['additional']['item']
            
    class candidates(object):
        @staticmethod
        def getByOfficeState(officeId, stateId=None, electionYear=None):
            params = {'officeId': officeId, 'stateId':stateId, 'electionYear': electionYear}
            result = votesmart._apicall('getByOfficeState', params)['candidateList']['candidate']
                
        @staticmethod
        def getByLastname(lastName, electionYear=None):
            params = {'lastName': lastName, 'electionYear':electionYear}
            result = votesmart._apicall('getByLastname', params)['candidateList']['candidate']
                
        @staticmethod
        def getByLevenstein(lastName, electionYear=None):
            params = {'lastName': lastName, 'electionYear':electionYear}
            result = votesmart._apicall('getByLevenstein', params)['candidateList']['candidate']
                
        @staticmethod
        def getByElection(electionId):
            params = {'electionId': electionId}
            result = votesmart._apicall('getByElection', params)['candidateList']['candidate']
                
        @staticmethod
        def getByDistrict(districtId, electionYear=None):
            params = {'districtId': districtId, 'electionYear':electionYear}
            result = votesmart._apicall('getByDistrict', params)['candidateList']['candidate']
        
    class committee(object):
        @staticmethod
        def getTypes(self):
            result = votesmart._apicall('getTypes', {})['committeeTypes']['type']
            
        @staticmethod
        def getCommitteesByTypeState(typeId=None, stateId=None):
            params = {'typeId':typeId, 'stateId':stateId}
            result = votesmart._apicall('getCommitteesByTypeState', params)['committees']['committee']
            
        @staticmethod
        def getCommittee(committeeId):
            params = {'committeeId' : committeeId}
            result = votesmart._apicall('getCommittee', params)['committee']
        
        @staticmethod
        def getCommitteeMembers(committeeId):
            params = {'committeeId' : committeeId}
            result = votesmart._apicall('getCommitteeMembers', params)['committeeMembers']['member']
    
    class district(object):
        @staticmethod
        def getByOfficeState(officeId, stateId, districtName=None):
            params = {'officeId':officeId, 'stateId': stateId}
            if districtName:
                params['districtName'] = districtName
            result = votesmart._apicall('getByOfficeState', params)['districtList']['district']
    
    class election(object):
        @staticmethod
        def getElection(electionId):
            params = {'electionId':electionId}
            result = votesmart._apicall('getElection', params)['elections']['election']
            
        @staticmethod
        def getElectionByYearState(year, stateId=None):
            params = {'year':year}
            if stateId:
                params['stateId'] = stateId
            result = votesmart._apicall('getElectionByYearState', params)['elections']['election']
            
        @staticmethod
        def getStageCandidates(electionId, stageId,
                               party=None, districtId=None, stateId=None):
            params = {'electionId':electionId, 'stageId':stageId, 'party':party,
                      'districtId':districtId, 'stateId':stateId}
            result = votesmart._apicall('getElectionByYearState', params)['stageCandidates']['candidate']
        
    class leadership(object):
        @staticmethod
        def getPositions(stateId=None, officeId=None):
            params = {'stateId':stateId, 'officeId':officeId}
            result = votesmart._apicall('getPositions', params)['leadership']['position']
                
        @staticmethod
        def getCandidates(leadershipId, stateId=None):
            params = {'leadershipId':leadershipId, 'stateId':stateId}
            result = votesmart._apicall('getCandidates', params)['leaders']['leader']
            
    class local(object):
        @staticmethod
        def getCounties(stateId):
            params = {'stateId': stateId}
            result = votesmart._apicall('getCounties', params)['counties']['county']
            
        @staticmethod
        def getCities(stateId):
            params = {'stateId': stateId}
            result = votesmart._apicall('getCities', params)['cities']['city']
            
        @staticmethod
        def getOfficials(localId):
            params = {'localId': localId}
            result = votesmart._apicall('getOfficials', params)['candidateList']['candidate']
        
    class measure(object):
        @staticmethod
        def getMeasuresByYearState(year, stateId):
            params = {'year':year, 'stateId':stateId}
            result = votesmart._apicall('getMeasuresByYearState', params)['measures']['measure']
            
        @staticmethod
        def getMeasure(measureId):
            params = {'measureId':measureId}
            result = votesmart._apicall('getMeasure', params)['measure']
        
    class npat(object):
        @staticmethod
        def getNpat(candidateId):
            params = {'candidateId':candidateId}
            result = votesmart._apicall('getNpat', params)['npat']
    
    class office(object):
        @staticmethod
        def getTypes(self):
            result = votesmart._apicall('getTypes', {})['officeTypes']['type']
        
        @staticmethod
        def getBranches(self):
            result = votesmart._apicall('getBranches', {})['branches']['branch']
    
        @staticmethod
        def getLevels(self):
            result = votesmart._apicall('getLevels', {})['levels']['level']
    
        @staticmethod
        def getOfficesByType(typeId):
            params = {'typeId':typeId}
            result = votesmart._apicall('getOfficesByType', params)['offices']['office']
            
        @staticmethod
        def getOfficesByLevel(levelId):
            params = {'levelId':levelId}
            result = votesmart._apicall('getOfficesByLevel', params)['offices']['office']
            
        @staticmethod
        def getOfficesByTypeLevel(typeId, levelId):
            params = {'typeId':typeId, 'levelId':levelId}
            result = votesmart._apicall('getOfficesByTypeLevel', params)['offices']['office']
            
        @staticmethod
        def getOfficesByBranchLevel(branchId, levelId):
            params = {'branchId':branchId, 'levelId':levelId}
            result = votesmart._apicall('getOfficesByBranchLevel', params)['offices']['office']
                
    class officials(object):
        @staticmethod
        def getByOfficeState(officeId, stateId=None):
            params = {'officeId':officeId}
            result = votesmart._apicall('getByOfficeState', params)['candidateList']['candidate']
                
        @staticmethod
        def getByLastname(lastName):
            params = {'lastName':lastName}
            result = votesmart._apicall('getByLastname', params)['candidateList']['candidate']
       
        @staticmethod
        def getByLevenstein(lastName):
            params = {'lastName':lastName}
            result = votesmart._apicall('getByLevenstein', params)['candidateList']['candidate']
       
        @staticmethod
        def getByElection(electionId):
            params = {'electionId':electionId}
            result = votesmart._apicall('getByElection', params)['candidateList']['candidate']
        
        @staticmethod
        def getByDistrict(districtId):
            params = {'districtId':districtId}
            result = votesmart._apicall('getByDistrict', params)['candidateList']['candidate']
    
    class rating(object):
        @staticmethod
        def getCategories(stateId=None):
            params = {'stateId':stateId}
            result = votesmart._apicall('getCategories', params)['categories']['category']
    
        @staticmethod
        def getSigList(categoryId, stateId=None):
            params = {'categoryId':categoryId, 'stateId':stateId}
            result = votesmart._apicall('getSigList', params)['sigs']['sig']
    
        @staticmethod
        def getSig(sigId):
            params = {'sigId':sigId}
            result = votesmart._apicall('getSig', params)['sig']
    
        @staticmethod
        def getCandidateRating(candidateId, sigId):
            params = {'candidateId':candidateId, 'sigId':sigId}
            result = votesmart._apicall('getCandidateRating', params)['candidateRating']['rating']
    
    class state(object):
        @staticmethod
        def getStateIDs(self):
            result = votesmart._apicall('getStateIDs', {})['stateList']['list']['state']
    
        @staticmethod
        def getState(stateId):
            params = {'stateId':stateId}
            result = votesmart._apicall('getState', params)['state']['details']
                
    class votes(object):
        @staticmethod
        def getCategories(year, stateId=None):
            params = {'year':year, 'stateId':stateId}
            result = votesmart._apicall('getCategories', params)['categories']['category']
            
        @staticmethod
        def getBill(billId):
            params = {'billId':billId}
            result = votesmart._apicall('getBill', params)['bill']
        
        @staticmethod
        def getBillAction(actionId):
            params = {'actionId':actionId}
            result = votesmart._apicall('getBillAction', params)['action']
        
        @staticmethod
        def getBillActionVotes(actionId):
            params = {'actionId':actionId}
            result = votesmart._apicall('getBillActionVotes', params)['votes']['vote']
        
        @staticmethod
        def getBillActionVoteByOfficial(actionId, candidateId):
            params = {'actionId':actionId, 'candidateId':candidateId}
            result = votesmart._apicall('getBillActionVoteByOfficial', params)['bills']['bill']
            
        @staticmethod
        def getBillsByCategoryYearState(categoryId, year, stateId=None):
            params = {'categoryId':categoryId, 'year':year, 'stateId':stateId}
            result = votesmart._apicall('getBillsByCategoryYearState', params)['bills']['bill']
            
        @staticmethod
        def getBillsByYearState(year, stateId=None):
            params = {'year':year, 'stateId':stateId}
            result = votesmart._apicall('getBillsByYearState', params)['bills']['bill']
            
        @staticmethod
        def getBillsByOfficialYearOffice(candidateId, year, officeId=None):
            params = {'candidateId':candidateId, 'year':year, 'officeId':officeId}
            result = votesmart._apicall('getBillsByOfficialYearOffice', params)['bills']['bill']
            
        @staticmethod
        def getBillsByCandidateCategoryOffice(candidateId, categoryId, officeId=None):
            params = {'candidateId':candidateId, 'categoryId':categoryId, 'officeId':officeId}
            result = votesmart._apicall('getBillsByCandidateCategoryOffice', params)['bills']['bill']
            
        @staticmethod
        def getBillsBySponsorYear(candidateId, year):
            params = {'candidateId':candidateId, 'year':year}
            result = votesmart._apicall('getBillsBySponsorYear', params)['bills']['bill']
            
        @staticmethod
        def getBillsBySponsorCategory(candidateId, categoryId):
            params = {'candidateId':candidateId, 'categoryId':categoryId}
            result = votesmart._apicall('getBillsBySponsorCategory', params)['bills']['bill']
        
        @staticmethod    
        def getBillsByStateRecent(stateId=None, amount=None):
            params = {'stateId':stateId, 'amount':amount}
            result = votesmart._apicall('getBillsByStateRecent', params)['bills']['bill']
                
        @staticmethod
        def getVetoes(candidateId):
            params = {'candidateId': candidateId}
            result = votesmart._apicall('getVetoes', params)['vetoes']['veto']
