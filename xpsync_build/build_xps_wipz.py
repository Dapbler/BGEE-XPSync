from math import log10, floor

def round_to_3(x):
    return round(x, 2-int(floor(log10(abs(x)))))

# The script we're starting when done with the main XP block
next_xps_script="xps_wipe"

print('''
// We're here because the NPC has XP above our range but the
// PC has less than 100M

// Progressively wipe XP down until
// we're back in the band we expect and it's in the ballpark
// of our grant

IF
\tGlobal("XPSYNC_HIGHXP_WIPE","LOCALS",0)
\tGlobal("XPSYNC_DEBUG","GLOBAL",1)
THEN
\tRESPONSE #100
\t\tSetGlobal("XPSYNC_HIGHXP_WIPE","LOCALS",1)
\t\tDisplayString(LastSummonerOf(Myself),540022)
\t\tContinue()
END
''')

xp_check_limit=10000
XP=1024000000 # About 1 x 10^9

while XP>xp_check_limit:
    print('''
IF
\tOR(2)
\t\tCheckStatGT(LastSummonerOf(Myself),90000000,XP)
\t\tGlobalLT("XPSYNC_GRANT","LOCALS",{0})
\tCheckStatGT(LastSummonerOf(Myself),{0},XP)
THEN
\tRESPONSE #100
\t\tAddXpObject(LastSummonerOf(Myself),-{0})
END'''.format(XP))
    XP=int(round_to_3(XP/2))

print('''
// XP now down to the ballpark of the grant
// Retry regular band based wipe
IF
\tTrue()
THEN
\tRESPONSE #100
\t\tChangeAIScript("{0}",OVERRIDE)
\t\tSetGlobal("XPSYNC_HIGHXP_WIPE","LOCALS",0)
END
'''.format(next_xps_script))
