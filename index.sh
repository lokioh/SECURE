#!/bin/bash

# Launch the start header of the tool
./layout/startHeader.sh

# Define functions for menu options
function nmap_scan() {
    echo "Runnin nmap scan..."
    ./scripts/reconnaissance/nmap.sh
}

# Display main menu
while true
do

    # Write in green
    echo -e "\033[32m"
    echo "Automated Penetration Testing Tool"
    echo "----------------------------------"

    #Write in default color
    echo -e "\033[0m"
    echo "1. Nmap Scan"
    echo -e "2. Exit\n"
    read -p "Enter option number: " choice

    case $choice in
        1)
            nmap_scan
            ;;
        2)
            exit 0
            ;;
        *)
            echo -e "\nInvalid option. Please enter a valide option."
            read -p "Press Enter to continue..."
            ;;
    esac
done