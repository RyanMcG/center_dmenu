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


def get_dimensions():
    current_display = display.Display()
    current_screen = current_display.screen()

    return (current_screen['width_in_pixels'],
            current_screen['height_in_pixels'],
            current_screen['width_in_mms'],
            current_screen['height_in_mms'])


def parse_dmenu_args(args):
    x_width, x_height, mms_width, mms_height = get_dimensions()
    num_args = len(args)

    # Do some math to determine a multiplier to go from points to pixels.
    pixels_per_point = x_height / (mms_height / 25.4) / 72

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
        'x': int(round(padding * x_width / 2.0, 0)),
        'height': int(round(line_height * pixels_per_point, 0)),
        'extra_args': "-fn '{0}:size={1}'".format(typeface, font_size)
    }

    # Determine propper height and width for input into dmenu
    dmenu_run_args['width'] = x_width - (2 * dmenu_run_args['x'])
    dmenu_run_args['y'] = (x_height - dmenu_run_args['height']) / 2
    return dmenu_run_args


def main(args):
    dmenu_run_args = parse_dmenu_args(args)
    return system(("dmenu_run {extra_args} -w {width} -x {x} -y {y}"
                   " -h {height}").format(**dmenu_run_args))


def console_main():
    sys.exit(main(sys.argv))

if __name__ == '__main__':
    console_main()
