"""Very simple entry point for the game"""

import optparse
from typing import Any

from lib import buggyGame

USAGE = """%prog [-fjns]"""
VERSION = "%prog v" + buggyGame.SYSVERSION


def parse_options() -> tuple[Any, list[str]]:
    """
    Parse any command-line options given.

    Returns:
        tuple: A tuple containing the options and arguments
    """
    parser = optparse.OptionParser(usage=USAGE, version=VERSION)

    parser.add_option("-f", "--fullscreen",
        action="store_true", default=False, dest="fullscreen",
        help="enable fullscreen mode")

    parser.add_option("-j", "--joystick",
        action="store_true", default=False, dest="joystick",
        help="enable joystick use (disables keyboard)")

    parser.add_option("-n", "--nosound",
        action="store_true", default=False, dest="nosound",
        help="disable sound")

    parser.add_option("-s", "--skipintro",
        action="store_true", default=False, dest="skipintro",
        help="skip fydo.net intro")

    return parser.parse_args()


if __name__ == '__main__':
    """"""
    # Welcome the player
    print(f"fydo's buggyGame v{buggyGame.SYSVERSION} - http://www.fydo.net")

    # Parse the options up! Woo
    opts, _ = parse_options()

    # Play time
    buggyGame.main(opts.fullscreen, opts.joystick, opts.nosound, opts.skipintro)

    # Say goodbye like every good little program should
    print("\nThanks for playing!")
