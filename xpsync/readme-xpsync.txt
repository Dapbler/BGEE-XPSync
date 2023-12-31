eXPerience SYNC
=================================================================

This mod helps synchronize the experience of NPCs with the PC, removing the
penalty for switching between companions during the game to see their companion quests.

It's a modest quality of life cheat.

The XP matching has a few modes of operation:

1) Using the "Train Party" special ability granted to the PC lets them 
   synchronise all NPCs once a day

2) The XPSync AI script (selectable under the character Record scripts) will
   syncronise either an individual NPC (if they run it) or the whole party 
   (if run by the PC). Also can toggle animations during "Training".

3) [EXPERIMENTAL] With the second dialogue component NPCs should synchronise
   automatically when joining and rejoining the party.

======================================
* Features
======================================

A Training Montage! (NEW!)

Accurate XP matching - typical error of a half percent.

Quiet addition of XP in one lump. ^

Dual Class character aware.

Uses in game experience tables - XP table mod aware if installed after the
table changes.

50,000 lines of code - when other XP matching scripts only give you hundreds!

( ^ Couple of exceptions - NPCs with XP > 100M or who are dual classed with a
high original class level may get a noisy XP flattening. )

======================================
* Compatibility
======================================

This uses some new BG(2)EE triggers that make finding dual class XP much simpler
so won't work in the original games.

So far I've tried it on BGEE, and BG2EE. If it seems appropriate for ther IE EE
games I'll look to add support if/when I play them.

XPSync only handles dual class costing for stock classes. If characters have
mod classes as their original class the XP for that is (probably) not used for
counting XP.

=======================================
* Components
=======================================
1) The core component adds
	a) The PC Train Party power
	b) The XPSYNC AI script

2) XPSync on joining the party (Experimental)
	This component searches all dialogues (1900ish in my BGEE) and hooks
	training into all joining party events.
	This should work with third party NPCs without special work.

=======================================
* Installation order
=======================================

Must be installed after any mods that modify dialogues if you want them
to be updated by the dialog component.

This (and other WeiDU based installers, such as Level1NPCs) should be 
installed after non-WeiDU mods that replace BG2 files.

I'd put this mod as late as possible in your install order just in case
you suspect it's broken dialogues and want to remove it to test.

=======================================
* Installation
=======================================
0. Prelare your BG(2)EE for modding
   
   BGEE: If you have BGEE with Siege of Dragonspear you will need
   to unpack the files with a tool like modmerge.

   LINUX: Depending on filesystem and if you're running the native version 
   or windows via wine you'll need to do some fiddling to handle mixed case. 
   I run via wine and have to prepare the install with Weidu's included 
   tolower utility before installing mods.
   All the files in xpsync are already in lower case.

1. Virus scan the XPSYNC zip (really, you should be in this habit)

2. Unzip the XPSync zip
   Put the xpsync folder from the zip into your game folder (same level as
   the "override" folder)

   (If on Windows: Virus scan and then put the setup-xpsync.exe in your 
   game folder as well. ALWAYS virus scan random things downloaded from
   the internet.)

3a. Windows: run setup-xpsync.exe (ie. <your game path>\setup-xpsync.exe
3b Linux: Install weidu for linux (from weidu.org)
	cd <game directory>
	weinstall xpsync

Note - if this mod is years old you may want to replace setup-xpsync.exe with
a newer version of weidu. Pick one up from weidu.org

=======================================
* Questions, Bugs and Workarounds
=======================================

Q: Do I need to start a new game to use XPSync?
A: No, it should work fine on ongoing games - you may want to Train Party 
   after installing to sync up the existing party members.
   When loading a game after installation the main PC will receive
   the Train Party ability. Individual members of the party can
   use the XPSync AI script to trigger a sync if you like.

Q: If I uninstall the mod can I continue with the save.
A: If you use weidu to uninstall the mod it will remove the dialogue hooks,
   but even if left in the game should continue to work okay and saves
   made before or after removal are usable.
   EE Keeper will automatically warn about, and clean up, the Train Party
   innate ability (XPSTEAM) if you use it to load a save after you've
   uninstalled the XPSync mod.

Q: How EXPERIMENTAL is the second dialogue component?
A: It works and I'd be surprised if it causes any trouble.
   There could be mod added dialogue that has weird content that I hadn't 
   considered - if you come across anything odd that's fixed by uninstalling 
   XPSync please let me know.

Q: What is the accuracy of the sync?
A: For the range of 1,000 to 100,000,000 XP the scripts will usually be 
   accurate to about half a percent.

   To avoid having a bunch of long scripts dealing with very small or large 
   XP totals:
   1) All NPCs have a minimum of about 1000 XP,
   2) Khalid and Jaheira, as seasoned adventurers, have a minimum of about 
      4000 XP (WOW!),
   3) The sync won't do any adjustment of less than 100 XP and
      adjustments of less than 1000 XP are relatively coarse
      (up to 5% error, could be +/- 50 XP!)
   4) NPCs will be boosted up to a maximum of about 100 million XP
   
   On the low end once the main PC is above 1000 (or 4000 for Khalid and 
   Jaheira) using the Train Party ability will bring party XP in line with
   the PC.

Q: Where is my training montage!
A: The "Training montage" (okay... it's an animation and a screen fade...)
   only triggers when using the Train Party ability or AI script.
   Having it run as part of the regular join party conversations looked
   like the NPC went berserk and attacked for no reason.

Q: Dialogue install can take a while, what's up?
A: The dialogue patching tries to copy, decompile, search, patch and 
   recompile every dialogue file in the game. For a combined EET install
   I'm guessing this is about 5000 dialogues. This is "fine" on
   relatively modern computers, but if you're playing on a classic system
   I'm guessing it may take a while.
   The alternative is curating short lists of files to patch for each potential
   game/mod install - which I'm not confident I'd maintain long term.

== ISSUES / BUGS ==

* XP Sync can die during XP matching (killing our squirrel mascot!)

Sometimes (maybe 2% of runs) the sync process dies part way through
and the invisble squirrel guiding the process vanishes.
As far as I can tell it's not a script issue but may be some sort of culling
of memory hog or summoned creatures.

If it happens either use the Train Party power to resync everyone or apply
the XPSync AI script to the affected character and press S to retry.

* If the XP Cap is in place XPSync won't correct NPCs with very high XP

The game keeps track of XP above the XP cap but only reports higher XP as
being the same as the XP cap. For example, if you set XP of an NPC as 2 billion
with the debug console the game will report the XP stat as being 8 million in
BG2EE, but subtracting 7 million XP still leaves them as having 1993 million.

If you've imported a save with a very high XP NPC to sync you can either
disable the XP Cap with Tweaks Anthology or use the console to set the NPC
down to below the XP Cap.

=======================================
* License
=======================================
    XPSync Infinity Engine mod
    Copyright (C) 2023 Robert Thiem

    Licensed under Attribution-NonCommercial 3.0 Unported (CC BY-NC 3.0) 

    https://creativecommons.org/licenses/by-nc/3.0/

    The setup-xpsync.exe file bundled with this mod is licensed under the 
    GPL (details can be found at weidu.org)
    A copy of the GPL 3.0 is included with this mod.

=======================================
* Credits
=======================================
Creatures are based on the core BGEE Squirrel.
Spells are derivatives of the core BGEE Cure Light Wounds.

Credit goes to avenger77 for providing inspiration on how to add innate powers
via global scripts via Tweaks Anthology.
The Level 1 NPCs developers wrote the the original dialogue insertion code,
that guided me in my implementation and deserve credit for making a mod 
so wonderful that I was inspired to write an earlier (very slow, 
spaghetti code) version of this sync mod back in 2014 to work with it.

These are both standout mods - and well worth a look:

https://gibberlings3.github.io/Documentation/readmes/readme-cdtweaks.html

https://gibberlings3.github.io/Documentation/readmes/readme-level1npcs.html

Tools used:
WeiDU
Near Infinity
VS Code
BG Forge MLS
Git (oh, how did I live without you, Git?)
Python 3
Sed

TODO: Track down author lists for the above tools





