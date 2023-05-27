### SECURE - Security Evaluation and Compliance Unified Reporting Engine
### Auteur : Loïc LIM
### Date de création : 31/04/2023

import subprocess
import pyfiglet
import os
import shodan
import glob


def execute_command(command, output_file):
    # Exécute une commande et enregistre la sortie dans un fichier
    try:
        print(f"[+] Exécution de la commande {command[0]}...\n")
        result = subprocess.check_output(command, universal_newlines=True)

        with open(output_file, "w") as file:
            file.write(result)

    except subprocess.CalledProcessError as e:
        print(f"\n[-] Une erreur s'est produite lors de l'exécution de la commande {command[0]}:")
        print(e.output)


def run_command(command, target, output_file):
    # Exécute une commande avec une cible spécifique et enregistre la sortie dans un fichier
    command = [command] + command_options[command].split() + [target]
    execute_command(command, output_file)


def run_shodan(target):
    try:
        # Effectue un ping vers la cible
        command = ["ping", "-c", "1", target]
        result = subprocess.run(command, capture_output=True, text=True)

        # Récupère l'adresse IP à partir de la sortie du ping
        ip_address = None
        for line in result.stdout.splitlines():
            if "from" in line:
                ip_address = line.split("from ")[1].split()[0].strip()

        if ip_address:
            print(f"\n[+] Adresse IP associée à {target}: {ip_address}\n")
        else:
            print("[-] Impossible de récupérer l'adresse IP.")
    except subprocess.CalledProcessError as e:
        print(f"[-] Une erreur s'est produite lors de l'exécution de la commande ping : {e}")

    # Initialise la clé d'API Shodan
    shodan_api_key = "N0HuWoSnikLfTDa4VouMpzvrZuWEFdZ3"
    api = shodan.Shodan(shodan_api_key)

    try:
        print("\n[+] Exécution de la commande Shodan...\n")
        # Effectue une recherche d'informations sur la cible avec Shodan
        results = api.host(ip_address)
        print("[+] Résultat de Shodan :")

         # Affiche les informations essentielles
        output = "\n".join(
            [
                f"Organisation: {results.get('org', '')}",
                f"Pays: {results.get('country_name', '')}",
                f"Ports ouverts: {', '.join(map(str, results.get('ports', [])))}",
                f"Vulnérabilités connues: {', '.join(map(str, results.get('vulns', [])))}"
            ]
        )

        # Enregistrer le résultat dans un fichier .txt
        with open("shodan.txt", "w") as file:
            file.write(output)

    except shodan.APIError as e:
        print("\n[-] Une erreur s'est produite lors de l'exécution de la commande Shodan :")
        print(e)


def report():
    # Texte à afficher
    texte = "SECURE"
    signification = "Security Evaluation and Compliance Unified Reporting Engine"

    # Crée une instance de l'objet Figlet
    figlet = pyfiglet.Figlet(font="slant")

    # Obtient le texte en ASCII art
    ascii_art = figlet.renderText(texte)

    # Obtient le chemin absolu du répertoire courant
    current_directory = os.path.abspath(os.getcwd())

    # Liste tous les fichiers .txt dans le répertoire courant
    txt_files = [file for file in os.listdir(current_directory) if file.endswith(".txt")]

    #Vérifie si un fichier resultats existe déjà
    if os.path.exists(os.path.join(current_directory, "resultats.txt")):
        os.remove(os.path.join(current_directory, "resultats.txt"))

    # Rassemble tous les fichiers .txt dans un seul fichier
    output_file = os.path.join(current_directory, "resultats.txt")

    with open(output_file, "w") as output:
        # Affiche l'entête SECURE
        output.write(ascii_art)
        output.write(signification + "\n\n")

        # Parcourt tous les fichiers .txt et écrit leur contenu dans le fichier de sortie
        for txt_file in txt_files:
            with open(txt_file, "r") as file:
                output.write(f"=== {txt_file} ===\n")
                output.write(file.read())
                output.write("\n\n")

    # Liste tous les fichiers .txt dans le répertoire courant
    txt_files = glob.glob("*.txt")

    # Supprime tous les fichiers .txt sauf le fichier de rapport
    for file in txt_files:
        if file != "resultats.txt":
            os.remove(file)

    print(f"\n[+] Les résultats ont été enregistrés dans le fichier : {output_file}")


def run_all(target):
    for command in command_options:
        run_command(command, target, command + ".txt")

    run_shodan(target)
    report()


# Options des commandes
command_options = {
    "nslookup": "",
    "nmap": "-p22,21,23,443,80,53,135,8080,8888 -A -O -sV -sC -T4",
    "whois": "",
    "sublist3r": "-d",
    "theHarvester": "-d",
    "sslscan": "",
    "sqlmap": "-u"
}

# Définit le texte à afficher
texte = "SECURE"
signification = "Security Evaluation and Compliance Unified Reporting Engine"

# Crée une instance de l'objet Figlet
figlet = pyfiglet.Figlet(font="slant")

# Obtient le texte en ASCII art
ascii_art = figlet.renderText(texte)

# Affiche le texte en ASCII art
print("\033[32m" + ascii_art + "\033[0m")

# Affiche la signification de SECURE
print("\033[32m" + signification + "\033[0m")

# Demande à l'utilisateur d'entrer une adresse IP ou un nom de domaine
target = input("Entrez une adresse IP ou un nom de domaine : ")

# Appelle la fonction run_all avec la cible spécifiée
run_all(target)