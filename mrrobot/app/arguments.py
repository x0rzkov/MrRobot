import argparse

def parse():
    # Name and description
    parser = argparse.ArgumentParser(
        prog="mrrobot",
        description="A robot to automate the hacking process",
        add_help=True)
    # ---- Information
    information = parser.add_argument_group(title="information")
    # Version
    information.add_argument(
        "--version",
        action="version",
        version="MrRobot v1.0.0",
        help="Prints the version")
    # ---- Challenge
    chellenge = parser.add_argument_group(title="challenge")
    # Input (Challenge)
    chellenge.add_argument(
        "input",
        type=str,
        metavar="CHALLENGE",
        help="Challenge input (Can be a string or a file)")
    # Flag format
    chellenge.add_argument(
        "-f", "--flag",
        metavar="FLAG",
        action="store",
        help="Specifies the regex-based flag format (Default: .*)")
    # ---- Performance
    performance = parser.add_argument_group(title="configuration")
    # Clean
    performance.add_argument(
        "--clean",
        action="store_true",
        help="Removes the default configuration if exists")
    # File (Configuration)
    performance.add_argument(
        "-c", "--config",
        metavar="INI",
        action="store",
        help="Specifies the configuration file (Default: mrrobot.ini)")
    # Banner
    performance.add_argument(
        "--no-banner",
        action="store_true",
        help="Hides the banner")
    # Coding
    performance.add_argument(
        "--coding",
        metavar="CODING",
        type=str,
        help="Set the encoding method (Default: utf-8)")
    # Timeout
    performance.add_argument(
        "--timeout",
        metavar="SECONDS",
        type=float,
        help="Set the timeout to the specified number of seconds (Default: 10. Disabled: 0)")
    # ---- Units Group
    units = parser.add_argument_group(title="available categories")
    # All
    units.add_argument(
        "-a", "--all",
        action="store_true",
        help="Loads all the units (Default)"
    )
    # Crypto
    units.add_argument(
        "-uc", "--crypto",
        action="store_true",
        help="Loads the crypto units"
    )
    # Esoteric
    units.add_argument(
        "-ue", "--esoteric",
        action="store_true",
        help="Loads the esoteric units"
    )
    # Parse the arguments
    return parser.parse_args()