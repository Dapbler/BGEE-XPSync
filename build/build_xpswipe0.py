from math import log10, floor

def round_to_3(x):
    return round(x, 2-int(floor(log10(abs(x)))))

# The script we're starting when done with the main XP block
next_xps_script="xpsgrant"

# The limit of banded XP.
# This script only runs through once and exits when hitting the XP band
# so having a higher cap doesn't make it take longer for everyone with
# normal XP levels

xp_band_limit=250000000 # 250 million


lower=50
growth=1.1
give_scaleup=1.05
print('''
IF
\tCheckStatLT(LastSummonerOf(Myself),{0},XP)
THEN
\tRESPONSE #100
\t\tChangeAIScript("{1}",OVERRIDE)
END
'''.format(lower,next_xps_script))
    

while lower<1000:
    top=int(round(lower*growth))
    gt=lower-1
    lt=top+1
    give=int(round(lower*give_scaleup))
    print('''
// NPC XP {0}-{1} => {2}
IF
\tCheckStatLT(LastSummonerOf(Myself),{4},XP)
THEN
\tRESPONSE #100
\t\tIncrementGlobal("XPSYNC_GRANT","LOCALS",-{2})
\t\tChangeAIScript("{6}",OVERRIDE)
END'''.format(lower,top,give,gt,lt,give,next_xps_script))
    lower=top+1

