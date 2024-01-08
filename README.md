# Readme

[Readme: Italiano](./README_IT.md)
[Readme: English](./README.md)

# SSHClient

SSHClient is a Python class that utilizes the `paramiko` library to establish an SSH connection to a remote host and execute a series of specified commands.

## Installation

Before you begin, you need to install `paramiko` if it's not already installed. You can do this using `pip`:

```bash
pip install paramiko
```

## Usage

To use `SSHClient`, you can create an instance of the class and use the `connect` method to establish a connection to the remote host. The `connect` method requires the following parameters:

- `hostname`: The IP address or host name you want to connect to.
- `username`: The username to use for authentication.
- `password`: The password to use for authentication.
- `commands`: A list of commands to execute on the remote host.
- `port`: The port to use for the SSH connection. This parameter is optional and its default value is 22.

After executing the commands, you can use the `close` method to close the connection.

Here's an example of usage:

```python
from ssh_lib import SSHClient

ssh = SSHClient()
hostname = 'your_hostname'
username = 'your_username'
password = 'your_password'
commands = ['ls', 'pwd', 'whoami']  # List of commands to execute
port = 22  # Port to use, you can modify it according to your needs
result = ssh.connect(hostname, username, password, commands, port)
for output in result:
    print(output)
ssh.close()
```

## Error Handling

The `connect` method can return errors in case there are problems with the authentication, with the SSH connection itself, or with any other exception. In such cases, it will return a list containing an error message.