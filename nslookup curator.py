"""
Program: Domain Name Resolver
Author: James Byrd
Date: 6/10/2024

Description:
This program reads a list of domain names from a file, resolves them to their respective IP addresses,
and writes the results to an Excel file. It also excludes specified IP addresses based on an exclusion list.

Files:
- nslookuplist.txt: Contains the domain names to be resolved.
- excludedips.txt: Contains the IP addresses to be excluded.
- resolved_ips.xlsx: The output Excel file with resolved IP addresses.

Usage:
Ensure the input files (nslookuplist.txt and excludedips.txt) are in the same directory as this script.
Run the script to generate the resolved_ips.xlsx file.
"""

import socket                                                          # Import socket module
import xlsxwriter                                                      # Import xlsxwriter module

# File paths
domain_file_name = r'C:\Users\morbi\nslookuplist.txt'                  # domain_file_name gets domain file
excluded_ips_file_name = r'C:\Users\morbi\excludedips.txt'             # excluded_ips_file_name gets excluded ip file
output_file_name = r'C:\Users\morbi\resolved_ips.xlsx'                 # 

# Function to read domain names from a file
def read_file(file_name):                                              # read_file function gets file name, returns set. 
    try:                                                               # try block
        with open(file_name, 'r') as file:                             # open file in read mode within a context manager
            lines = file.readlines()                                   # read lines of the file, saved in variable lines
        return {result.strip() for result in lines}                    # a set comprehension that processes each line and removes leading and trailing whitespace and returns the set
    except FileNotFoundError:                                          # except block
        print(f"File '{file_name}' not found!")                        # print file not found
        return set()                                                   # return empty set

# Function to resolve domain names and print IP addresses
def resolve_domains(domain_file_name, excluded_ips_file_name):         # resolve_domains function gets domain file name and excluded ip file name
    domains = read_file(domain_file_name)                              # domains calls read_file function with domain file name
    exclude_ips = read_file(excluded_ips_file_name)                    # exclude_ips calls read_file function with excluded ip file name

    workbook = xlsxwriter.Workbook(output_file_name)                   # workbook gets xlsxwriter.Workbook
    worksheet = workbook.add_worksheet("Resolved IPs")                 # worksheet gets workbook.add_worksheet

    # Write headers
    worksheet.write(0, 0, "Domain")                                    # write domain
    worksheet.write(0, 1, "IP Addresses")                              # write ip addresses

    row = 0                                                            # row gets 0 for an initial value
    for fqdn in domains:                                               # for loop.  For each FQDN in the domains set
        ip_set = set()                                                 # ip_set gets set.  Creates a blank set.
        try:                                                           # try block
            addr_info = socket.getaddrinfo(fqdn, 0, socket.AF_INET)    # Retrieve address information for the domain name (fqdn) #getaddrinfo returns a list of tuples(family, socktype, proto, canonname, sockaddr)
            for ipaddr in addr_info:                                   # for loop.  For each ip address in the address information list
                ip_set.add(ipaddr[-1][0])                              # ip_set.add [-1][0].Last tuple, 0th entry of the tuple.  Add IP address to the set.
            ip_set -= set(exclude_ips)                                 # Removes unwanted entries from the set.
            if len(ip_set) > 0:                                        # if ip_set is not empty, print and write entry
                row += 1                                               # row += 1
                ips = ', '.join(ip_set)                                # Join IP addresses in the ip_set set into a comma-separated string
                print(f"{fqdn}", ips)                                  # print fqdn, ips. This was for an earlier version/testing, but added back in.
                worksheet.write(row, 0, fqdn)                          # write fqdn in excel sheet
                worksheet.write(row, 1, ips)                           # write ips in excel sheet
        except socket.error:                                           # except block to catch general socket errors
            pass                                                       # pass to continue on to the next line

    workbook.close()                                                   # Close the workbook                
    print(f"\nData successfully written to {output_file_name}")        # print data successfully written to output_file_name

# Resolve domains and write to Excel
resolve_domains(domain_file_name, excluded_ips_file_name)              # resolve_domains function gets domain file name and excluded ip file name