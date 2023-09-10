eXPerience SYNC
=================================================================

This mod helps synchronize the experience of NPCs with the PC, removing the
penalty for switching between companions during the game to see their companion quests.

It has a few modes of operation:

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

( ^ Excluding dualed NPCs with very high level original classes exceeding the PC.
This should be rare and I couldn't justify another 12K lines of script for it
and instead used something accurate but noisy. )

======================================
* Compatibility
======================================

This uses some new BG(2)EE triggers that make finding dual class XP much simpler
so won't work in the original games.

So far I've tried it on BGEE, and BG2EE. If it seems appropriate for ther IE EE
games I'll look to add support as I play them.

XPSync only handles dual class costing for stock classes. If characters have
mod classes as their original dual class the XP for that is not used for
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
0. Download the XPSYNC zip

1. Virus scan the XPSYNC zip (really, you should be in this habit)

2. Unzip the XPSync zip
   Put the xpsync folder from the zip into your game folder (same level as "override")
   (If on Windows: Virus scan and then put the setup-xpsync.exe in your game folder as well.)

3a. Windows: run setup-xpsync.exe (ie. <your game path>\setup-xpsync.exe
3b Linux: Install weidu for linux (from weidu.org)
	cd <game directory>
	weinstall xpsync
3c OS X: ????

Note - if this mod is years old you may want to replace setup-xpsync.exe with
a newer version of weidu. Pick one up from weidu.org

=======================================
* Questions, Issues, fixes and workarounds
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

Q: What is the accuracy of the sync?
A: To avoid having a bunch of long scripts dealing with very small or large XP totals:
   1) All NPCs have a minimum of about 1000 XP,
   2) Khalid and Jaheira, as seasoned adventurers, have a minimum of about 
      4000 XP (WOW!),
   3) The sync won't do any adjustment of less than 100 XP and
      adjustments of less than 1000 are relatively coarse
      (up to 5%, which is 50 XP error!)
   4) NPCs will be boosted up to a maximum of about 100 million XP
   
   Once the main PC is above 1000 (or 4000 for Khalid and Jaheira) the 
   Train Party ability will bring party XP in line with the PC.
   
   For the range of 1000 - 100 million XP normally the scripts will be 
   accurate to about half a percent.

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
   it may take a while.
   The alternative is curating short lists of files to patch for each potential
   game/mod install - which I'm not confident I'd maintain long term.

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

Credit goes to avenger77 for the A7 Global Script Extender (taken from
the Tweaks Anthonlogy)
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
Python3
Sed

TODO: Track down author lists for the above tools





