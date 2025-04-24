from argparse import ArgumentParser

parser = ArgumentParser(
    prog='IDUN Guardian Jaw Clench Input Provider',
    description='A simple app to pipe jaw clench predictions' \
        'from the IDUN Guardian to binary input values'
)

parser.add_argument(
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


class CommandLineArguments:
    api_token: str | None
    address: str | None
    debug: bool


def get_command_line_arguments() -> CommandLineArguments:
    return parser.parse_args()