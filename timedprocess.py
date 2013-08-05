#!/usr/bin/python

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

script_info = """
This program will run a process for the amount of time you enter.

You can run it from the command line with these paramaters:
timedprocess.py [-h] [-s] path time
\t UNIMPLEMENTED -h: print the help file
\t UNIMPLEMENTED -s: shutdown once the program is finished

\t time can be a time, or can be any consecutive instances of time.
\t time format: [float]h/m/s
\t Unit Legend: s=second | m=minutes | h=hour

If it recieves no arguments it will gather input using pythons raw_input
"""

import shlex
import subprocess
import sys
from time import sleep

command_line_warning =      "\nWARNING: these will be passed to the command line.\n"
invalid_arguments_error =   "\nYou have entered an invalid argument, use -h to see usage."
process_open_error =        "\nThe program couldn't open that file. This is usually a problem with the path."
invalid_time_warning =      "\nWARNING: Invalid time argument: '%s'."
#flag_definitions =          {'-h':'print_help', '-s':'shutdown'}

def main():
    arguments = sys.argv[1:]
    process_path, time, flags = get_args(arguments)
    try:
        popen_process = subprocess.Popen(process_path)
        sleep(time)
        popen_process.terminate()
    except WindowsError:
        print process_open_error
    
def get_args(arguments):
    #if arguments in flag_definitions:
    #    print "Flags!"
    if len(arguments) <= 1:
        print command_line_warning
        arg_path = raw_input("Enter path to program: ")
        time = shlex.split(raw_input("Enter amount of time you'd like the process to run for: "))
        arg_total_seconds = parse_time(time)
    else:
        arg_path = arguments.pop(0)
        if arg_path in help_flags:
            print script_info
            arg_path = arguments.pop(0)
        arg_total_seconds = parse_time(arguments) 
    return arg_path, arg_total_seconds
     
def parse_time(time_argv):
    total_time = 0
    unit_conversions = {'s':0, 'm':60, 'h':60*60}
    for arg in time_argv:
        unit = arg[-1]
        time_str = arg[:len(arg)-1]
        try:
            total_time += int(time_str) * unit_conversions[unit]
        except ValueError:
            print invalid_time_warning % arg
        except KeyError:
            print invalid_time_warning % arg
    return total_time

main()

# Created by Aaron Delaney aka Koldof