#!/bin/bash

# Ask user for target IP address
read -p "Enter the IP address of the target system: " ip_address

# Scan target for open ports and services with Nmap
nmap $ip_address 

# Ask user if they want to save the results in a PDF file
read -p "Do you want to save the results in a PDF file? (y/n) " save

if [ "$save" == "y" ]; then
    # Save results in a PDF file using Pandoc and LaTeX
    nmap $ip_address -oN nmap_results.txt
    pandoc -o nmap_results.pdf nmap_results.txt
    #rm nmap_results.txt
    echo "Results saved in nmap_results.pdf"
fi