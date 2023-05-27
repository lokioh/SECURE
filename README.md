# SECURE - Security Evaluation and Compliance Unified Reporting Engine

![SECURE logo](./img/SECURE_logo.png)

Ce script est conçu pour effectuer une évaluation de sécurité et générer un rapport unifié des résultats. Il utilise différentes commandes système pour recueillir des informations sur une cible spécifiée, effectuer une recherche Shodan et générer un rapport final.

## Description 

Le script est développé en Python et utilise des modules tels que **'subprocess'**, **'pyfiglet'**, **'os'**, **'shodan'** et **'glob'**. Il permet d'automatiser la collecte d'informations sur une cible, d'effectuer une recherche Shodan pour obtenir des informations supplémentaires et de générer un rapport final contenant tous les résultats obtenus.

## Fonctionnalités

Le script propose les fonctionnalités suivantes:

- Exécute différentes commandes système pour recueillir des informations sur la cible :
    - **'nslookup'**: effectue une recherche DNS pour obtenir les informations liées à l'adresse IP ou au nom de domaine spécifié.
    - **'whois'**: récupère les informations Whois sur la cible.
    - **'nmap'**: effectue un balayage de ports sur la cible en utilisant les options spécifiées dans le dictionnaire **'command_options'**.
    - **'sublist3r'**: effectue une recherche de sous-domaines à partir du nom de domaine spécifié.
    - **'theHarvester'**: effectue une recherche d'informations sur la cible en utilisant des moteurs de recherche publics.
    - **'sslscan'**: effectue une analyse de la sécurité SSL/TLS du serveur cible.
    - **'sqlmap'**: effectue une injection SQL sur une URL spécifiée pour détecter d'éventuelles vulnérabilités.
- Effectue une recherche Shodan pour obtenir des informations supplémentaires sur la cible :
    - Effectue un ping vers la cible pour obtenir son adresse IP.
    - Utilise l'API Shodan pour effectuer une recherche d'informations sur la cible.
    - Récupère des détails tels que l'organisation, le pays, les ports ouverts et les vulnérabilités connues.
- Génère un rapport final unifié contenant tous les résultats obtenus :
    - Crée un fichier de rapport resultats.txt.
    - Ajoute les résultats de chaque commande exécutée dans le rapport.

## Usage

1. Assurez-vous d'avoir les pré-requis mentionnés ci-dessous.
2. Placez le script dans un répertoire de votre choix.
3. Ouvrez un terminal et accédez au répertoire où se trouve le script.
4. Exécutez le script à l'aide de la commande suivante (en utilisant **'sudo'** pour les privilèges d'administration) :
```sh
sudo python ./secure.py
```
5. Entrez une adresse IP ou un nom de domaine lorsque vous y êtes invité.
6. Le script exécute toutes les commandes définies dans le dictionnaire **'command_options'** avec la cible spécifiée. Il est donc très simple d'ajouter de nouvelles commandes si besoin.
7. Une recherche Shodan est effectuée pour obtenir des informations supplémentaires sur la cible.
8. Les résultats de chaque commande exécutée sont enregistrés dans des fichiers **'.txt'**.
9. Un rapport final est généré en rassemblant tous les fichiers **'.txt'** dans un fichier **'resultats.txt'**.
10. Le rapport final est affiché à l'écran et enregistré dans le répertoire courant.