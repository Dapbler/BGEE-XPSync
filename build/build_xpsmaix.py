from math import log10, floor

def round_to_3(x):
    return round(x, 2-int(floor(log10(abs(x)))))

# The script we're starting when done with the main XP block
next_xps_script="xps_pd"

xp_band_limit=10000 # 250 million


lower=1000
growth=1.01
give_scaleup=1.005
while lower<xp_band_limit:
    top=int(round(lower*growth))
    gt=lower-1
    lt=top+1
    give=int(round(lower*give_scaleup))
    print('''
// Player XP {0}POW-{1}POW => {2}POW
IF
\tCheckStatLT(Player1,{4}POW,XP)
THEN
\tRESPONSE #100
\t\tSetGlobal("XPSYNC_GRANT","LOCALS",{5}POW)
\t\tChangeAIScript("{6}",OVERRIDE)
END'''.format(lower,top,give,gt,lt,give,next_xps_script))
    lower=top+1

print('''
// We've hit the end - player XP is beyond our test range (BUG)
IF
\tTrue()
THEN
\tRESPONSE #100
\t\tChangeAIScript("{1}",OVERRIDE)
END'''.format(give,next_xps_script))



