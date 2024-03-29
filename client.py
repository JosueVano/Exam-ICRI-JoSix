import socket
import os, time

#definition de l'adresse pour ce connecter/ localHost
host, port =('localhost',5566)

#creation de variable de type socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connection d'un client
try:
    sock.connect((host, port))
    print("Client connecté")

    #Insertion du nom de fichier à telecharger
    text = str(input("Nom Fichier:"))
    text = text.encode("utf8")
    sock.sendall(text)

except:
    print("Connexion au server echouée !")
    exit(0)

#reception des details du fichier
file_name = sock.recv(100).decode()
file_size = sock.recv(100).decode()

#gestion d'erreur lors d'inexistance du fichier dans la base de donnée
if file_name == "Erreur":
    print("Fichier inexistant dans la base")

#telechargement du fichier demandé    
else:
    with open("./rec/" +file_name,"wb") as file:
        c = 0
        start_time = time.time()

        while c <= int(file_size):
            data = sock.recv(1024)
            if not (data):
                break
            file.write(data)
            c += len(data)

        end_time = time.time()

    print("Transfer complet. Temps de transfer: ",end_time - start_time)

#fermeture du socket
sock.close()
