# Summary #

DuathlonStarter is a program designed for small Duathlon (but can be used in Triathlon too!) sporting events where running and biking (and swimming?) can't be done in the same place, so this program helps with that, and usually for swimming, the pool is not at the same place...

In essence how this works is, when athletes go through one section (i.e. running), the times are recorded, athletes relocate to where they'll be doing the next section (i.e. biking or swimming), recorded times are loaded into the program and the program counts down time difference and beeps when it reaches zero for each athlete.

This program is written in "Python 3" with PyQt5, therefore it's cross-platform, however only a Windows standalone binary is available for download. To use on other systems (Linux, Mac) the below requirements should be met.

The program interface (and commit messages) are in Lithuanian language, but they can be easily translated if you prefer another language.

## Features ##

+ Data loading
    * From file (text)
    + From memory
        * Can be pasted from time-logging programs (i.e. spreadsheets),  
          either from two side-by-side columns, or different columns.
    + Additional screens
        * Show a whole list of loaded athletes and their status
        * Show a big clock, current and next athletes
    + Settings
        * Change sound file (user can use their own) for a start
        * Choose a delay in seconds before first athlete
        * Change big clock size in percents

# Usage requirements #

+ To run the program
    * Python 3.6+
    * PyQt5  
    **OR**  
    * Just a Windows machine, if using the standalone binary
+ To use the program
    * Times has to be in format: **1337**_[tab]_**1:07,2**  
      Which translates to: **athlete_nr**_[tab]_**minute:seconds,millis**
  
# Known problems #

On a Windows system (can't say for others), when the clock is running and you press on a titlebar to move the window, the clock (or more precisely the thread that the clock runs in) pauses for a second, or until you move the window, or when you release the titlebar. This is by design on system level and can't be overriden.

More on this: https://stackoverflow.com/questions/35180772/pyqt4-qtimer-stops-when-close-button-is-held

Also, pywin32 doesn't change anything.

# Technical stuff #

The code is very well documented and easy to read (at least I think so :P).  
All generated UI files are named _*Dialog.py_ and _*Window.py_ and placed in the root folder.  
_GUIs_ folder contain the XML UI files needed for editing in QtDesigner.  
_sounds_ folder contains sample sound files  
_images_ folder contains a program icon.  
_start.py_ is where the fun begins. This is, as the name suggests, the file to run to start it all.

