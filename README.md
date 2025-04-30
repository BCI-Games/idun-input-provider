# IDUN Guardian Input Provider
A python application built to pipe realtime predictions outside of the python environment through a TCP socket.

Currently sends "True" or "False" utf-8 strings corresponding to jaw clench predictions.

## Options
- -h, --help
- -t, --api-token : token required for IDUN API calls
- -a, --address : MAC address of the guardian earbuds
- -d, --debug : whether to start the IDUN client in 'debug' mode
- -s, --simulate-input : whether to send dummy prediction data without connecting to a real device, mutually exclusive with api token
- -sh, --socket-host : host address of the socket connection
- -p, --socket-port : port of the socket connection