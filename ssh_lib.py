import paramiko

class SSHClient:
    def __init__(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self, hostname, username, password, commands, port=22):
        try:
            self.client.connect(hostname, port=port, username=username, password=password)
            output = []

            for command in commands:
                stdin, stdout, stderr = self.client.exec_command(command)
                result = stdout.read().decode()
                error = stderr.read().decode()

                if error:
                    output.append(f"Host: {hostname}\nCommand: {command}\nError: {error}")
                else:
                    output.append(f"Host: {hostname}\nCommand: {command}\n{result}")

            return output

        except paramiko.AuthenticationException:
            return ["Errore di autenticazione: verifica le credenziali."]
        except paramiko.SSHException as e:
            return [f"Errore SSH: {str(e)}"]
        except Exception as e:
            return [f"Errore durante la connessione: {str(e)}"]

    def close(self):
        self.client.close()

# Utilizzo:
if __name__ == "__main__":
    ssh = SSHClient()
    hostname = 'your_hostname'
    username = 'your_username'
    password = 'your_password'
    commands = ['ls', 'pwd', 'whoami']  # Lista dei comandi da eseguire
    port = 22  # Porta da utilizzare, puoi modificarla secondo le tue necessità

    result = ssh.connect(hostname, username, password, commands, port)

    for output in result:
        print(output)

    ssh.close()
