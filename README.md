# XPSync - a BG(2)EE mod for matching XP for party members

## Overview

This mod is all about accurately syncing the experience of party members in Baldur's Gate Enhanced Edition (BGEE) and Baldur's Gate II Enhanced Edition (BG2EE).

It'll generally sync party members to within about half a percent of the PC's experience.

It's a weidu mod that will integrate with experience table changes and with third party NPCs, but only uses generic classes for some Dual Class XP calculations so may give unpredictable results if you're using "outside the box" custom classes or kits.

I suggest putting this at the end of your mod install order. The dialogue hook addition can only work with mods that are already installed (so xpsync should be installed after anything that chanes party joining dialogues). Also if there's ever any suspicion that xpsync has broken a dialogue having it installed late means that weidu has less to uninstall and then reinstall if you remove xpsync for testing.

## Installation

The "build" folder contains programs used to create this mod, they're not required for installation for play.

For installation you will need he contents of the "xpsync" folder.

*NOTE* - Do not delete the xpsync folder after installation. It contains backup information you will need if you uninstall.

### Linux:

1. Place xpsync folder in your BG(2)EE installation folder (at the same level as override)
2. From your BG(2)EE folder install using "weinstall xpsync".
3. Answer the installation questions.

Weinstall is one of the weidu programs available from weidu.org.

### Windows:

1. Place setup-xpsync.exe and xpsync folder in your BG(2)EE installation folder (at the same level as override)
2. From your BG(2)EE folder install using setup-xpsync.exe
3. Answer the installation questions.

## Uninstalling

Repeat running "weinstall xpsync" or "setup-xpsync.exe" as done during installtion and choose the uninstall option.
If you've been working with weidu mods uninstalling with intelligently uninstall weidu mods set up after xpsync, uninstall xpsync, and then reinstall the later mods (weidu is very clever).

## Building

The contents of xpsync are complete and can be directly modified.
Some of the scripts are... a bit long... I built them using the python and bash scripts in xpsync_build and the xpsync_build/build.sh script.

If you're on a un*x like system these will probably work fine.

1. Modify build python scripts (in /build)
2. cd xpsync_build; ./build.sh

If you don't have sed (for instance on Windows) then another option would be to add a parameter to some of the build scripts and run with parmeters for each power of ten.

## License

I'm using a chunk of a77's code for global script addition and learned dialogue hooking from the Level 1 NPCs mod code. The Creative Commons license used by L1NPCs seemed appropriate. (See LICENSE.txt)

If you need to use the novel bits I wrote (or can get a release from a77/L1NPCs team for the other parts) and the CC license included isn't workable please contact me.

The Weidu software (included as Setup-xpsync.exe for Windows users) is licensed under the Gnu Public License v3 - a copy is included repository. See weidu.org for more information on Weidu.
