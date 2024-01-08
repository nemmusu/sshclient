import paramiko
import configparser
import time
import threading
import sys

def read_config():
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
        hostname = config['SSH_CONFIG']['hostname']
        username = config['SSH_CONFIG']['username']
        password = config['SSH_CONFIG']['password']
        port = config['SSH_CONFIG'].getint('port', 22)  # Lettura della porta, con 22 come valore predefinito
        return hostname, username, password, port
    except FileNotFoundError as e:
        print(f"Errore: file di configurazione non trovato: {e}")
        sys.exit(1)
    except (configparser.Error, KeyError) as e:
        print(f"Errore nella lettura del file di configurazione: {e}")
        sys.exit(1)

def receive_output(stdout, stop_event):
    try:
        while not stop_event.is_set():
            if stdout.channel.recv_ready():
                output = stdout.channel.recv(1024).decode()
                print(output, end='')
            if stdout.channel.exit_status_ready():
                break
    except paramiko.SSHException as e:
        print(f"Errore durante la lettura dell'output: {str(e)}")

def main():
    stop_event = threading.Event()
    ssh = None
    output_thread = None
    try:
        hostname, username, password, port = read_config()
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port=port, username=username, password=password)
        channel = ssh.invoke_shell()
        stdin = channel.makefile('wb')
        stdout = channel.makefile('rb')
        output_thread = threading.Thread(target=receive_output, args=(stdout, stop_event))
        output_thread.start()
        while not stop_event.is_set():
            if stdout.channel.exit_status_ready():
                break
            command = input('')
            stdin.write(command + '\n')
            stdin.flush()
            time.sleep(0.5)  # Breve attesa per la ricezione dell'output
    except KeyboardInterrupt:
        print("\nOperazione interrotta dall'utente.")
    except paramiko.AuthenticationException:
        print("Errore di autenticazione: verifica le credenziali.")
    except paramiko.SSHException as ssh_e:
        print(f"Errore SSH: {str(ssh_e)}")
    finally:
        stop_event.set()  # Imposta l'evento per interrompere il thread
        if output_thread is not None:
            output_thread.join()
        if ssh is not None:
            ssh.close()
            
if __name__ == '__main__':
    main()
