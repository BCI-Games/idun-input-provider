from idun_guardian_sdk import GuardianClient
from arguments import get_command_line_arguments

args = get_command_line_arguments()

client = GuardianClient(api_token=args.api_key)