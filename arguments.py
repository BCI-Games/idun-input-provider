from argparse import ArgumentParser
from classes import CommandLineArguments


parser = ArgumentParser(
    prog='IDUN Guardian Jaw Clench Input Provider',
    description='A simple app to pipe jaw clench predictions' \
        'from the IDUN Guardian to binary input values'
)

parser.add_argument(
    '-t', '--api-token', default=None, required=True,
    help='API Token required for IDUN API Calls'
)
parser.add_argument(
    '-a', '--address', default=None,
    help='MAC address of the guardian earbuds'
)
parser.add_argument(
    '-d', '--debug', action='store_true', 
    help='Enable debug mode'
)

parser.add_argument(
    "--websocket-host", default='',
    help='Web Socket connection host'
)
parser.add_argument(
    '-p', '--websocket-port', default=8005,
    help='Web Socket connection port'
)


def get_command_line_arguments() -> CommandLineArguments:
    return parser.parse_args()