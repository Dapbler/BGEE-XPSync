Primarily runs as an Override AI script inside our 
Wise Squirrel CREature, and state is mainly based on whichever script 
is currently set to run.

# Scripts

xps_conf - The ex configuration script for the pre EE dual class modifification
    Now triggers the subject to cast a spell summoning the Wise Squirrel that guides
    through the mentoring/XP process

xpscreai - entry script, run by the Wise Squirrel. Checks the subject is sane

xps_main - adds simple (not dual class) XP from main to NPC (branching to a 
    script for the rough band)

xps_mai3 to xps_mai7 - Adds XP to the tally, each script for a higher power of 10

xps_pd - detects a previous PC dual class and branches to class specific scripts

xps_pXXX - scripts for each PC dual class - add the XP to the tally

xps_nd - detects a previous NPC dual class and branches to class specific scripts

xps_nXXX - scripts for each NPC dual class - subtracts XP from the tally
    NOTE: We do the original NPC XP wipe late.
    If another script is doing XP modification at join (or the main program)
    it will have a few seconds to do its thing before we get here.

xps_wipe - removes XP from NPC in up to five steps

xps_wip0 xps_wip7

xpsgrant - grant XP

xpsgran1 - xpsgran7 - negative grants

xpsgrap1 - xpsgrap7 - positive grants

xpsgrazz - This is a short noisy script to wipe XP from the NPC.
    It's used in edge cases where the NPC cannot be brought down to the experience
    it should have, probably because of a high level original class

# Spells

xpsmntr - the Training (aka mentoring) spell run by the subject (eg NPC party member)
    Calls the Wise Squirrel to run through the scripts above
xpsteam - starts the training across the whole party. Calls the Elder Squirrel

# Creatures

xpsquirl.cre - Wise Squirrel (does XP tallying and setting)
xpsquir2.cre - Elder Squirrel (calls wise squirrels)