from asyncio import run, gather, sleep
from process_management import start_parent_process_dependency_loop
from arguments import get_command_line_arguments
from server import start_broadcast_server
from jaw_clench_client import create_jaw_clench_client
from input_simulation import start_simulated_input_broadcast_loop


async def main():
    args = get_command_line_arguments()
    server = await start_broadcast_server(args.socket_host, args.socket_port)

    if args.simulate_input:
        run_method = start_simulated_input_broadcast_loop(server)
    else:
        client = create_jaw_clench_client(
            server, api_token=args.api_token,
            address=args.address, debug=args.debug
        )
        run_method = client.start_recording()

    await gather(
        start_parent_process_dependency_loop(),
        run_method
    )


try: run(main())
except KeyboardInterrupt: pass
except InterruptedError: pass

print("exiting...")