timedprocess.py
===============

What is it?
---------------
Run a program for a specified lenght of time, via an easy to use command line interface.

How do I install it?
---------------
Once you have [python][1](Recommended v2.7.5), you can run it either from the command line or by running the script normally.

Features?
---------------
Currently you can run it from the command line with these paramaters:

    timedprocess.py [-h] [-s] path time
        UNIMPLEMENTED -h: print the help file
        UNIMPLEMENTED -s: shutdown once the program is finished

        time can be a time, or can be any consecutive instances of time.
        time format: [float]h/m/s
        Unit Legend: s=second | m=minutes | h=hour

If it wasn't run with arguments it will ask for the arguments with the default python command line.

Notes
---------------
A GUI interface is currently planned, though I'd like to cement most of the features first.

[1]: http://www.python.org/download/ "Python"