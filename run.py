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

from main import Main

# ---------------------- MOTHER CODE ---------------------------- #

MAIN = Main()
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjcxNjExYmM2LTZiMGMtNGI4Ny05ODc5LWRmNGExNzU5NzgwYiIsImlhdCI6MTU5NjM1ODU3Miwic3ViIjoiZGV2ZWxvcGVyLzZhY2Y0ODljLWIzOTMtNTViMC1mNjEyLWNiN2IyZGY3YThhZiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEwMy4xMDYuMTgxLjExIl0sInR5cGUiOiJjbGllbnQifV19.13c03vNM4IiNlR1fSSJ7UuGCxMHwkNZJKCiSkplMTltJbO90mSbIVqaoqrntgS8-bSGn22HERWWWyc9t9EEUQg'
"""
API TOKEN (You need to create your api token after creating your Clash of Clans developer account )
"""
timeout = 15
"""
api request timeout (You can set timeout according to your convenience)    
"""

MAIN.main(token, timeout)