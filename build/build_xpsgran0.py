from math import log10, floor

def round_to_2(x):
    return round(x, 1-int(floor(log10(abs(x)))))

# The script we're starting when done with the main XP block
next_xps_script="xpsgrazz"

# The limit of banded XP.
# This script only runs through once and exits when hitting the XP band
# so having a higher cap doesn't make it take longer for everyone with
# normal XP levels

xp_band_limit=-1000 # 250 million

lower=-100   
growth=1.1
give_scaleup=1.05

while lower>xp_band_limit:
    top=int(round(lower*growth))
    gt=top-1
    lt=lower+1
    give=int(round_to_2(lower*give_scaleup))
    print('''
// NPC XP {0}-{1} => {2}
IF
\tGlobalGT("XPSYNC_GRANT","LOCALS",{3})
\tCheckStatGT(LastSummonerOf(Myself),{4},XP)
THEN
\tRESPONSE #100
\t\tAddXpObject(LastSummonerOf(Myself),{2})
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