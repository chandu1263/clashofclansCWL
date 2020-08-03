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

from api import Api
import operator

# ------------------------------ ANALYSIS ------------------------------------ #

class Analysis:
    """
    Analysing current clan with all seven other clans in the current clan war league
    """
    
    def analysis(self, cwl_response: dict, clan_tag: str, token: str, timeout: int) -> dict:
        """[summary]

        Args:
            cwl_response (dict): [cwl api response from clash of clans CWL api]
            clan_tag (str): [current clan's clan_tag]
            token (str): [api_token]
            timeout (int): [api timeout]
                
        Returns:
            dict: [description]
        """
        
        clans = cwl_response['clans']
        clan_power = {}
        for each_clan in clans:
            c_tag = each_clan['tag']
            clan_power[c_tag] = self.clan_offense(each_clan, token, timeout)
            print(clan_power[c_tag])
        return clan_power

    def clan_offense(self, each_clan: dict, token: str, timeout: int) -> list:
            
        players = each_clan['members']
        th_levels = []
        cocoapi = Api(token, timeout)
        clan_data = []
        for each_player in players:
            player_tag = each_player['tag']
            th_level = each_player['townHallLevel']
            player_details = cocoapi.players(player_tag)
            player_troop_index_num = 0
            player_troop_index_den = 0
            player_troop_index = 0
            for each_troop in player_details['troops']:
                if each_troop['village'] == 'home':
                    player_troop_index_num += each_troop['level']
                    player_troop_index_den += each_troop['maxLevel']
                    player_troop_index += 1
            player_spell_index_num = 0
            player_spell_index_den = 0
            player_spell_index = 0
            for each_spell in player_details['spells']:
                player_spell_index_num += each_spell['level']
                player_spell_index_den += each_spell['maxLevel']
                player_spell_index += 1
            heroes = 0
            heroes_list = []
            for each_hero in player_details['heroes']:
                if each_hero['village'] == 'home':
                    heroes += (each_hero['level']/each_hero['maxLevel']) + 1 
                    heroes_list.append(each_hero['level'])
            experience_level = player_details['expLevel']
            if player_troop_index_den != 0:
                player_troop_index += (player_troop_index_num/player_troop_index_den)*100
            if player_spell_index_den != 0:
                player_spell_index += (player_spell_index_num/player_spell_index_den)*100
                heroes *= 100
            clan_data.append([player_tag, th_level, experience_level, heroes, player_troop_index, player_spell_index, heroes_list, th_level*(experience_level*.5 + heroes*1.5+player_spell_index*0.4+player_troop_index*0.6)])
        return clan_data
    
    def print_cwldata(self, clan_data: dict, current_clantag: str, token: str, timeout: int): 

        clan_data_modified = {}
        for each_clan in clan_data:
            
            sorted_players_list = sorted(clan_data[each_clan], key = lambda x:x[7])
            players_list = sorted_players_list[::-1]
            clan_data_modified[each_clan] = players_list
        
        home_clan = current_clantag
        home_clan_data = clan_data_modified[home_clan]
        cocoapi = Api(token, timeout) 
        home_clan_api_data = cocoapi.clan_tag(home_clan)
        cwl_stars = 0
        for each_clan in clan_data_modified:
            if each_clan != home_clan:
                cur_clan_api_data = cocoapi.clan_tag(each_clan)
                cur_clan_data = clan_data_modified[each_clan]
                print("************************ ---------------------- *****************************")
                print(str(home_clan_api_data['name']) + "     vs      " + str(cur_clan_api_data['name']))
                print("************************ ---------------------- *****************************")
                total_stars = 0
                for i in range(30):
                    str1 = ""
                    clasher = home_clan_data[i]
                    str1 += str(clasher[0])
                    str1 += "  th: " + str(clasher[1]) +"  heroes: "
                    for j in clasher[6]:
                        str1 += str(j) + "/"  
                    str1 += "exp: " + str(clasher[2])
                    print(str1)
                    str1 = ""
                    clasher1 = cur_clan_data[i]
                    str1 += str(clasher1[0])
                    str1 += "  th: " + str(clasher1[1]) +"  heroes: "
                    for j in clasher1[6]:
                        str1 += str(j) + "/"  
                    str1 += "exp: " + str(clasher1[2])
                    print(str1)
                    val = float(clasher[7]) - float(clasher1[7])
                    cur_stars = 0
                    if val < 0:
                        val = val * -1
                        cur_stars = -1 * int(int(val)/500)
                        if cur_stars < -3:
                            cur_stars = -3
                        tmp = -1 * cur_stars
                        print("head to head:" + "deficit by " + str(tmp) + " stars")
                    else:
                        cur_stars = int(int(val)/500)
                        if cur_stars > 3:
                            cur_stars = 3
                        print("head to head: " + "lead by " + str(cur_stars) + " stars")
                    total_stars += cur_stars
                if total_stars < 0:
                    tmp = total_stars * (-1)
                    print("head to head clan fight will give your clan a deficit of " + str(tmp) + " stars")    
                else:
                    print("head to head clan fight will give your clan a lead of " + str(total_stars) + " stars")    