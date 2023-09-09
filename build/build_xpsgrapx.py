from math import log10, floor

def round_to_3(x):
    return round(x, 2-int(floor(log10(abs(x)))))

# The script we're starting when done with the main XP block
next_xps_script="xpscreai"

# The limit of banded XP.
# This script only runs through once and exits when hitting the XP band
# so having a higher cap doesn't make it take longer for everyone with
# normal XP levels

xp_band_limit=10000 # 250 million

lower=1000  
growth=1.01
give_scaleup=1.005

while lower<xp_band_limit:
    top=int(round(lower*growth))
    gt=lower-1
    lt=top+1
    give=int(round_to_3(lower*give_scaleup))
    print('''
// NPC XP {0}POW-{1}POW => {2}POW
IF
\tGlobalLT("XPSYNC_GRANT","LOCALS",{4}POW)
THEN
\tRESPONSE #100
\t\tAddXpObject(LastSummonerOf(Myself),{2}POW)
\t\tDestroySelf()
END'''.format(lower,top,give,gt,lt,give,next_xps_script))
    lower=top+1
