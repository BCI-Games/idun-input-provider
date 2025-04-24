from argparse import ArgumentParser

parser = ArgumentParser(
    prog="IDUN Guardian Jaw Clench Input Provider",
    description="A simple app to pipe jaw clench predictions" \
        "from the IDUN Guardian to binary input values"
)

parser.add_argument('-k', '--api-key')


class CommandLineArguments:
    api_key: str


def get_command_line_arguments() -> CommandLineArguments:
    return parser.parse_args()