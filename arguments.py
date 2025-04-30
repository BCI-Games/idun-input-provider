from argparse import ArgumentParser
from classes import CommandLineArguments


parser = ArgumentParser(
    prog='IDUN Guardian Jaw Clench Input Provider',
    description='A simple app to pipe jaw clench predictions ' \
        'from the IDUN Guardian to binary input values'
)

input_group = parser.add_mutually_exclusive_group(required=True)
input_group.add_argument(
    '-t', '--api-token', default=None,
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
input_group.add_argument(
    '-s', '--simulate-input', action='store_true',
    help='Send dummy prediction data without connecting to a real device'
)

parser.add_argument(
    '-sh', '--socket-host', default='',
    help='Socket connection host'
)
parser.add_argument(
    '-p', '--socket-port', default=8005,
    help='Socket connection port'
)


def get_command_line_arguments() -> CommandLineArguments:
    return parser.parse_args()