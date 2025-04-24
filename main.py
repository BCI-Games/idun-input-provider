import sys
from argparse import ArgumentParser

parser = ArgumentParser(
    prog="IDUN Guardian Jaw Clench Input Provider",
    description="A simple app to pipe jaw clench predictions" \
        "from the IDUN Guardian to binary input values"
)

parser.add_argument('-k', '--api-key')
args = parser.parse_args()
print(args.api_key)

api_token = sys.argv[1]

from idun_guardian_sdk import GuardianClient
client = GuardianClient(api_token="my-api-token")