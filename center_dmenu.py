#!/usr/bin/env python2
from Xlib import display
import sys
from os import system


def get_dimensions():
    current_display = display.Display()
    current_screen = current_display.screen()
    return (current_screen['width_in_pixels'],
            current_screen['height_in_pixels'])


def parse_dmenu_args(args):
    x_width, x_height = get_dimensions()
    num_args = len(args)

    # Set some default values for dmenu args
    dmenu_run_args = {
        'x': 200,
        'height': 50,
        'extra_args': "-fn 'Inconsolata:size=10'"
    }

    # Get arguments from the command line.
    if num_args > 1:
        dmenu_run_args['x'] = int(args[1])
    if num_args > 2:
        dmenu_run_args['height'] = int(args[2])
    if num_args > 3:
        dmenu_run_args['extra_args'] = args[3]

    # Determine propper height and width for input into dmenu
    dmenu_run_args['width'] = x_width - (2 * dmenu_run_args['x'])
    dmenu_run_args['y'] = (x_height - dmenu_run_args['height']) / 2
    return dmenu_run_args


def main(args):
    dmenu_run_args = parse_dmenu_args(args)
    return system(("dmenu_run {extra_args} -w {width} -x {x} -y {y}"
                   " -h {height}").format(**dmenu_run_args))

if __name__ == '__main__':
    sys.exit(main(sys.argv))
