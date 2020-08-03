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

import sys
import json

from api import Api
from verify import Clan_tag_verifier
from analysis import Analysis

# ---------------------------  MAIN CODE  ------------------------------------ #

class Main:
    """
    MAIN CLASS
    """

    def main(self, token, timeout):
        """
        this function takes the input token and api request timeout as inputs
        Args:
            token ([str]): [API Token]
            timeout ([int]): [api request timeout]
        """
        _clan_tag = sys.stdin.readline()
        clan_tag = _clan_tag.strip()

        _Clan_tag_verifier = Clan_tag_verifier()

        if _Clan_tag_verifier.clan_tag_verifier(clan_tag) == False:
            print("INVALID CLAN TAG !!")
            
        if _Clan_tag_verifier.clan_tag_verifier(clan_tag) == True:
            cocoapi = Api(token, timeout)
            api_response = cocoapi.clan_tag(clan_tag)
            # print(api_response)  
            for key in api_response:
                if key == 'reason':
                    print("CLAN NOT FOUND !!")
                    return
                if key == 'result':
                    print(api_response)
                    return
            cwl_response = cocoapi.clan_leaguegroup(clan_tag)
            
            for key in cwl_response:
                if key == 'reason':
                    print("CLAN NOT IN CWL CURRENTLY !!")
                    return
                if key == 'result':
                    print(cwl_response)
                    return 
            _analysis = Analysis()
            clan_power = {}
            clan_power = _analysis.analysis(cwl_response, clan_tag, token, timeout)
            current_clan = clan_tag
            
            _analysis.print_cwldata(clan_power, current_clan, token, timeout)
                    
        return     





