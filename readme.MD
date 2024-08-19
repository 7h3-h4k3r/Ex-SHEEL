
---

# Reverse Shell Server

This Python script implements a basic reverse shell server. The server listens for incoming connections from clients and allows them to execute shell commands remotely on the server machine. The output of the commands is sent back to the client, making it a simple tool for remote system monitoring and control.

## Features

- **Multi-threaded Handling**: The server can handle multiple clients simultaneously using threading.
- **Command Execution**: Clients can execute shell commands on the server, and the results are sent back to them.
- **Educational Use**: Designed for educational purposes, particularly for students learning about system monitoring and network programming.

## Usage

1. **Running the Server**:
   - Run the script on your server machine.
   - The server listens on all available interfaces (`HOST = ""`) and on port `7878`.
   - The server waits for incoming client connections.

2. **Client Interaction**:
   - Once connected, the client can execute shell commands.
   - The server responds with the output of the commands.
   - To disconnect, the client can simply close the connection.

## Example

```bash
$ python3 shell_server.py
```

The client will receive a welcome message and can start executing commands.

```bash
shell server (2024: version 0.1 reverse shell Monitor)
rs# --help to show user Manual
Disclaimer: don't abuse it (only for student system Monitoring)
rs#:
```

## Code Overview

- **`Shell_server_client_handle` Class**: Handles each client connection in a separate thread. This allows the server to manage multiple clients simultaneously.
- **`subprocess.run()`**: Executes the received shell command and captures the output.
- **Socket Setup**: The server is configured to reuse the address and port to avoid binding issues on restarts.

## Disclaimer

This tool is for educational purposes only. Misuse of this tool is not encouraged or supported.

## Author

Authored by Sridharanitharan.

--- 