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