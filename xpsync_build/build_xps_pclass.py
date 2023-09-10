print('''// Player1 is a dual class, with original class CLASSNAME
// Go through levels and adjust XP''')


for lvl in range(2,41):
    print('''IF
\tClassLevel(Player1,CLSCAT,{0})
THEN
\tRESPONSE #100
\t\tIncrementGlobal("XPSYNC_GRANT","LOCALS",%CLASSNAME_{0}_XP%)
\t\tChangeAIScript("xps_nd",OVERRIDE)
END
'''.format(lvl))
    
print(''' // No matches so weirdness or have a dual class greater than our range
IF
\tTrue()
THEN
\tRESPONSE #100
\t\tChangeAIScript("xps_nd",OVERRIDE)
END
''')