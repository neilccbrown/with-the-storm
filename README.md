With the Storm
===

A simple utility program to use with the game [Against the Storm](https://store.steampowered.com/app/1336490/Against_the_Storm/).  It reads your save file and shows you the current blueprint choice, but annotates it to show which recipes can be satisfied now/in-the-future/never (within the current map that you are playing) by looking at the currently available resources, and the blueprints you have chosen so far.

To run it, download [the latest release](https://github.com/neilccbrown/with-the-storm/releases) and run the EXE.  (You may get a warning from Windows about running unrecognised executables, which is fair enough.  The EXE is built transparently direct on Github using the source code here.  If you prefer, you can checkout the source and run it in Python directly.)

**Note that the program reads your save file.  Against the Storm unfortunately (for our purposes) does not auto-save that often.  If the blueprint choice appears out-of-date, cancel the choice in the game, go to the menu and "Save and Quit" and then click Play to go straight back into the game.  This will force a save, and the window for this program will automatically update with the blueprint choice in the save file.**

If you notice any bugs, file an issue here.  The "Save.save" file from the "%userprofile%\appdata\locallow\Eremite Games\Against the Storm" directory will help immensely.

Changelog
===
- 1.0.6 (2024-01-10): Added some advanced buildings and corrected an existing building and resource node.
- 1.0.5 (2024-01-09): Tidied up the display when no blueprint choice is currently available.
- 1.0.4 (2024-01-08): Added another decoration, and stopped an unknown building being a fatal error.
- 1.0.3 (2024-01-05): Fixed more buildings and resources, and added recognition of yet more resource nodes.
- 1.0.2 (2024-01-04): Fixed more buildings and added recognition of more resource nodes.
- 1.0.1 (2024-01-03): Fixed some buildings and added recognition of more resource nodes.
- 1.0.0 (2024-01-03): Initial release.


