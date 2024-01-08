# Readme

[Readme: Italian](./README_IT.md)

[Readme: English](./README.md)

# SSHClient

SSHClient is a Python class that uses the `paramiko` library to establish an SSH connection with a remote host and execute a series of specified commands.

## Installation

Before starting, you need to install `paramiko` if it is not already installed. You can do this by using `pip`:

```bash
pip install paramiko
```

## Usage

To use `SSHClient`, you can create an instance of the class and use the `connect` method to establish a connection with the remote host. The `connect` method requires the following parameters:

- `hostname`: The IP address or the name of the host you want to connect to.
- `username`: The username to use for authentication.
- `password`: The password to use for authentication.
- `commands`: A list of commands to execute on the remote host.
- `port`: The port to use for the SSH connection. This parameter is optional and its default value is 22.

After executing the commands, you can use the `close` method to close the connection.

Here is an example of usage:

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

The `connect` method can return errors in case there are problems with authentication, with the SSH connection itself, or with any other exception. In such case, it will return a list containing an error message.

# `client_ssh.py` Script

## Requirements
Before running this script, make sure you have installed the following python packages:

- paramiko
- configparser

You can install these packages using pip:

```
pip install paramiko configparser
```

## Configuration
To use this script, you need to create a configuration file called `config.ini` in the same directory as the script. The configuration file should have the following format:

```
[SSH_CONFIG]
hostname = your_hostname
username = your_username
password = your_password
port = your_port
```

Where:
- `your_hostname` is the IP address or the host name of the server you want to connect to.
- `your_username` is the username to log in with.
- `your_password` is the password for the specified user.
- `your_port` is the port on which the SSH server is listening (optional, if not specified port 22 is used).

## Usage
To run the script, use the following command:

```
python client_ssh.py
```

After starting the script, an SSH connection will be established with the server specified in the configuration file. 

You can then start typing commands as if you were directly connected to the server via SSH. The output of each command will be printed on the console.

To stop the script, use `Ctrl+C`.