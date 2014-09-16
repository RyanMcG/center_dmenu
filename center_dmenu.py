#!/usr/bin/env python2

# Copyright 2013 Ryan McGowan
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from Xlib import display
import sys
from os import system


def pixels_per_point():
    current_display = display.Display()
    current_screen = current_display.screen()
    height_in_inches = current_screen['height_in_mms'] / 25.4
    height_in_points = height_in_inches * 72
    return current_screen['height_in_pixels'] / height_in_points


def parse_dmenu_args(args):
    num_args = len(args)
    # Get arguments from the command line.

    # 20% padding means only 80% of the screen is used by dmenu with 10%
    # padding on each side.
    padding = float(args[1]) if num_args > 1 else .24

    # Font size and lineheight are in points
    line_height = int(args[2]) if num_args > 2 else 24
    font_size = int(args[3]) if num_args > 3 else 11

    typeface = args[4] if num_args > 4 else 'Inconsolata'

    # Set some default values for dmenu args
    dmenu_run_args = {
        'padding': padding / 2,
        'height': int(round(line_height * pixels_per_point(), 0)),
        'extra_args': "-fn '{0}:size={1}'".format(typeface, font_size)
    }

    return dmenu_run_args


def main(args):
    dmenu_run_args = parse_dmenu_args(args)
    cmd_tmpl = "dmenu_run -c {extra_args} -d {padding} -h {height}"
    cmd = cmd_tmpl.format(**dmenu_run_args)
    return system(cmd)


def console_main():
    sys.exit(main(sys.argv))

if __name__ == '__main__':
    console_main()
