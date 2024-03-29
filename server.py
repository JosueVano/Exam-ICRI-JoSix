#Importation des focntions necessaire
import socket
import os,time

#definition de l'adresse pour ce connecter/ localHost
host, port = ('',5566)

#creation de variable de type socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#mis en connection du socket
sock.bind((host, port))
print("Le serveur est demarré ...")

#serveur en attente de client
sock.listen()
conn, adresse = sock.accept()

#serveur en attente de demande de fichier
print("En attente de demande...")

#reception du nom de fichier
file_name = conn.recv(1024)
if os.path.exists(file_name):

    file_name = file_name.decode("utf8")
    file_size = os.path.getsize(file_name)

    #envoi des informations pour stocker le fichier envoyé
    conn.send(file_name.encode())
    conn.send(str(file_size).encode())

    #Envoye de fichier
    with open(file_name,"rb") as file:
        c = 0

        start_time = time.time()

        while c <= file_size:
            data = file.read(1024)
            if not (data):
                break
            conn.sendall(data)
            c += len(data)

        end_time = time.time()

    print("Fichier tansferé. Temps total:",end_time - start_time)

else:
    #Message d'erreur si fichier inexistant
    conn.send("Erreur".encode())

#fermeture du client connecté et du socket en cours
conn.close()
sock.close()