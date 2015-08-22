#timedprocess.py

###What is it?

A simple command line tool to run a program for a specified duration.

###Features?
usage: timedprocess options duration path

Duration:
A string containing a time, for example:
```
"5h"
"5h25m"
"25m40s4h"
```

Options:
```
-hide-time-remaining		flags to hide the time remaining.
-help, -h, --help 			Show this message and exit.
```

###How do I install it?

The project uses setup_tools's automatic script creation, so if everything goes
well, after the project is installed you should be able to run it straight away
 from terminal the same way you would run pip for instance.

I recommend using pip to install:
```
pip install timedprocess.py
```

If you prefer you can try use easy_install on the setup.py, although I haven't tested this yet.

# Branches

The develop branch is only for use for development.

Use with caution.

# License
GNU GENERAL PUBLIC LICENSE, see LICENSE

----------------------

Made with <3 by Aaron Delaney (@devoxel)

##### PyPi Link: https://pypi.python.org/pypi/timedprocess.py/
