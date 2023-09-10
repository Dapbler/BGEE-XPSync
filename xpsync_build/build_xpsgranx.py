from math import log10, floor

def round_to_3(x):
    return round(x, 2-int(floor(log10(abs(x)))))

# The script jump to if we can't subtract XP
next_xps_script="xpsgrazz"

# The limit of banded XP.
# This script only runs through once and exits when hitting the XP band
# so having a higher cap doesn't make it take longer for everyone with
# normal XP levels

xp_band_limit=-10000 # 250 million

lower=-1000   
growth=1.01
give_scaleup=1.005

while lower>xp_band_limit:
    top=int(round(lower*growth))
    gt=top-1
    lt=lower+1
    give=int(round_to_3(lower*give_scaleup))
    print('''
// NPC XP {0}POW-{1}POW => {2}POW
IF
\tGlobalGT("XPSYNC_GRANT","LOCALS",{3}POW)
\tCheckStatGT(LastSummonerOf(Myself),{4}POW,XP)
THEN
\tRESPONSE #100
\t\tAddXpObject(LastSummonerOf(Myself),{2}POW)
\t\tDestroySelf()
END'''.format(lower,top,give,gt,-give))
    lower=top+1

print('''
// Reached end - can happen if we have enough XP to remove
// Jump to a fallback zeroing script
IF
\tTrue()
THEN
\tRESPONSE #100
\t\tChangeAIScript("{0}",OVERRIDE)
END'''.format(next_xps_script))