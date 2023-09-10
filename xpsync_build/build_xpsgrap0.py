from math import log10, floor

def round_to_2(x):
    return round(x, 1-int(floor(log10(abs(x)))))

# The script we're starting when done with the main XP block
next_xps_script="xpscreai"

# The limit of banded XP.
# This script only runs through once and exits when hitting the XP band
# so having a higher cap doesn't make it take longer for everyone with
# normal XP levels

xp_band_limit=1000 # 250 million

lower=100  
growth=1.1
give_scaleup=1.05

while lower<1000:
    top=int(round(lower*growth))
    gt=lower-1
    lt=top+1
    give=int(round_to_2(lower*give_scaleup))
    print('''
// NPC XP {0}-{1} => {2}
IF
\tGlobalLT("XPSYNC_GRANT","LOCALS",{4})
THEN
\tRESPONSE #100
\t\tAddXpObject(LastSummonerOf(Myself),{2})
\t\tDestroySelf()
END'''.format(lower,top,give,gt,lt,give,next_xps_script))
    lower=top+1
