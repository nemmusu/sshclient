# Readme

[Readme: Italiano](./README_IT.md)

[Readme: English](./README.md)

# SSHClient

SSHClient è una classe Python che utilizza la libreria `paramiko` per stabilire una connessione SSH con un host remoto e eseguire una serie di comandi specificati.

## Installazione

Prima di iniziare, è necessario installare `paramiko` se non è già installato. Puoi farlo utilizzando `pip`:

```bash
pip install paramiko
```

## Utilizzo

Per utilizzare `SSHClient`, è possibile creare un'istanza della classe e utilizzare il metodo `connect` per stabilire una connessione con l'host remoto. Il metodo `connect` richiede i seguenti parametri:

- `hostname`: L'indirizzo IP o il nome dell'host a cui si desidera connettersi.
- `username`: Il nome utente da utilizzare per l'autenticazione.
- `password`: La password da utilizzare per l'autenticazione.
- `commands`: Una lista di comandi da eseguire sull'host remoto.
- `port`: La porta da utilizzare per la connessione SSH. Questo parametro è opzionale e il suo valore predefinito è 22.

Dopo aver eseguito i comandi, è possibile utilizzare il metodo `close` per chiudere la connessione.

Ecco un esempio di utilizzo:

```python
from ssh_lib import SSHClient

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
```

## Gestione degli errori

Il metodo `connect` può restituire errori nel caso in cui ci siano problemi con l'autenticazione, con la connessione SSH in sé, o con qualsiasi altra eccezione. In tal caso, restituirà una lista contenente un messaggio di errore.

# Script `client_ssh.py`

## Requisiti
Prima di eseguire questo script, assicurati di aver installato i seguenti pacchetti python:

- paramiko
- configparser

Puoi installare questi pacchetti usando pip:

```
pip install paramiko configparser
```

## Configurazione
Per utilizzare questo script, è necessario creare un file di configurazione chiamato `config.ini` nella stessa directory dello script. Il file di configurazione dovrebbe avere il seguente formato:

```
[SSH_CONFIG]
hostname = your_hostname
username = your_username
password = your_password
port = your_port
```

Dove:
- `your_hostname` è l'indirizzo IP o il nome del host del server al quale vuoi connetterti.
- `your_username` è il nome utente con cui effettuare l'accesso.
- `your_password` è la password per l'utente specificato.
- `your_port` è la porta su cui il server SSH è in ascolto (facoltativo, se non specificato viene utilizzata la porta 22).

## Uso
Per eseguire lo script, usa il seguente comando:

```
python client_ssh.py
```

Dopo aver avviato lo script, verrà stabilita una connessione SSH con il server specificato nel file di configurazione. 

Puoi quindi iniziare a digitare comandi come se fossi connesso direttamente al server tramite SSH. L'output di ciascun comando verrà stampato sulla console.

Per interrompere lo script, usa `Ctrl+C`.