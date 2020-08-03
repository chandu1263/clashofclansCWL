###########################################################################
###########################################################################
##############                                                #############
##############      *************************************     #############
##############                                                #############
##############              AUTHOR : CHANDU BOBBILI           #############
##############                                                #############
##############      *************************************     #############
##############                                                #############
###########################################################################
###########################################################################

# ----------------------- LIBRARIES & CLASSES -------------------------------- #

import urllib
import json
from typing import Dict, Tuple
import httpx

# -------------------------- api functions ----------------------------------- #
 
class Api:
    def __init__(self, token: str, timeout: int = 20):
        """
        Initializing requisites
        Args:
            token (str): [clan tag]
            timeout (int, optional): [api timeout]. Defaults to 20.
        """
        self.token = token
        self.ENDPOINT = "https://api.clashofclans.com/v1"
        self.timeout = timeout
        self.headers = {
            "authorization": "Bearer %s" % token,
            "Accept": "application/json",
        }
        self.DEFAULT_PARAMS = ("limit", "after", "before")
        self.ERROR_INVALID_PARAM = {
            "result": "error",
            "message": "Invalid params for method",
        }
        
    def check_if_dict_invalid(self, params: Dict, valid_items: Tuple = ()) -> bool:
        if not valid_items:
            valid_items = self.DEFAULT_PARAMS
        return set(params.keys()).issubset(valid_items)
    
    def clan_tag(self, tag: str) -> Dict:
        """
        Function to Get information about a single clan by clan tag.
        Clan tags can be found using clan search operation.
        """
        uri = "/clans/%23" + tag[1:]
        return self.api_response(uri=uri)
    
    def clan_members(self, tag: str, params: Dict = {}) -> Dict:
        """
        Function to List clan members
        """
        if not self.check_if_dict_invalid(params=params):
            return self.ERROR_INVALID_PARAM
        uri = "/clans/%23" + tag[1:] + "/members"
        return self.api_response(uri=uri, params=params)

    def clan_war_log(self, tag: str, params: Dict = {}) -> Dict:
        """
        Function to Retrieve clan's clan war log
        """
        if not self.check_if_dict_invalid(params=params):
            return self.ERROR_INVALID_PARAM
        uri = "/clans/%23" + tag[1:] + "/warlog"
        return self.api_response(uri=uri, params=params)
    
    def clan_leaguegroup(self, tag: str) -> Dict:
        """
        Function to Retrieve information about clan's current clan war league group
        """
        uri = "/clans/%23" + tag[1:] + "/currentwar/leaguegroup"
        return self.api_response(uri=uri)
    
    def players(self, tag: str) -> Dict:
        """
        Function to Get information about a single player by player tag. Player tags can be found either in game or by from clan member lists.
        """
        uri = "/players/%23" + tag[1:]
        return self.api_response(uri=uri)
    
    def api_response(self, uri: str, params: Dict = {}) -> Dict:
        """
        Function to handle requests,it is possible to use this handler on it's
        own to make request to the api on in case of a new or unsupported api
        Args:
            uri      -> The endpoint uri that needs to be called for the specific function
            params   -> Dictionary of supported params to be filtered
                        with Refer https://developer.clashofclans.com/#/documentation
        Return:
            The json response from the api as is or returns error if broken
        """
        
        url = self.ENDPOINT + uri + "?" + urllib.parse.urlencode(params)  # type: ignore
        try:
            response = httpx.get(url=url, headers=self.headers, timeout=self.timeout)
            json_str = response.json()
            res = dict(json_str)
            return res
        except:
            res = {}
            res['result'] = 'error'
            res['message'] = 'something broke'
            return res
        
    def clan_members(self, tag: str, params: Dict = {}) -> Dict:
        """
        Function to List clan members
        """
        if not self.check_if_dict_invalid(params=params):
            return self.ERROR_INVALID_PARAM
        uri = "/clans/%23" + tag[1:] + "/members"
        return self.api_response(uri=uri, params=params)

    def clan_war_log(self, tag: str, params: Dict = {}) -> Dict:
        """
        Function to Retrieve clan's clan war log
        """
        if not self.check_if_dict_invalid(params=params):
            return self.ERROR_INVALID_PARAM
        uri = "/clans/%23" + tag[1:] + "/warlog"
        return self.api_response(uri=uri, params=params)    