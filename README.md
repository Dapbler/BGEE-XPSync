# XPSync - a BG(2)EE mod for matching XP for party members

## Overview

This mod is all about accurately syncing the experience of party members in Baldur's Gate Enhanced Edition (BGEE) and Baldur's Gate II Enhanced Edition (BG2EE).

It'll generally sync party members to within about half a percent of the PC's
experience.

It's a weidu mod that will integrate with experience table changes and with third party NPCs, but only uses generic classes for some Dual Class XP calculations so may give unpredictable results if you're using "out of the box" custom classes or kits.

## Installation

For installation you will need he contents of /xpsync.

1. Place xpsync folder in your BG(2)EE installation folder (at the same level as override)
2. From your BG(2)EE folder install using "weinstall xpsync". An alternative is to rename a copy of weinstall.exe (if on windows) to setup-xpsync.exe
3. Answer the installation questions.

Weinstall is one of the weidu programs available from weidu.org.

## Building

The contents of xpsync are complete and can be directly modified.
Some of the scripts are... a bit long... I built them using the python and bash scripts in /build and the build.sh script.

If you're on a un*x like system these will probably work fine.

1. Modify build python scripts (in /build)
2. Run build.sh

If you don't have sed (for instance on Windows) then a good option would be to add a parameter to some of the build scripts and run with parmeters for each power of ten.

## License

I'm using a chunk of a77's code for global script addition and learned
dialogue hooking from the Level 1 NPCs mod code. The Creative Commons
license used by L1NPCs seemed appropriate. (See LICENSE.txt)

If you need to use the novel bits I wrote (or can get a release from
a77/L1NPCs team for the other parts) and the CC license included isn't
workable please contact me.

The Weidu software (which may be bundled if I add a windows zip for
release) is licensed under the Gnu Public License v3 - included in this
repository.