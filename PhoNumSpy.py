import phonenumbers
import requests
import pyfiglet
import time
from googlesearch import search
from phonenumbers.phonenumberutil import region_code_for_number


def web_search(query, **kwargs):
    try:
        return list(search(query, **kwargs))
    except Exception as error:
        print(f"[!] Search failed for '{query}': {error}")
        return []

from phonenumbers import geocoder, carrier, timezone
import os
print("\n")
Ascii_Art = pyfiglet.figlet_format("PhoNumSpy")
print(Ascii_Art)
version = "Version 1.0"
print(version)
print("\n")
time.sleep(1)
maininput = input("Input the target phone number using this format: +(prefix)(phonenumber) ES: +447455869664\n-->")
lookuptarget = maininput.strip("+")
fileoutput = open(f"{maininput}_results.txt", "w")
fileoutput.write("\n")
fileoutput.write(Ascii_Art)
fileoutput.write("\n")
fileoutput.write("\n")
fileoutput.write(version)
fileoutput.write("\n")
fileoutput.write("\n")
print("\n")
print("-------------------------")
print("Target:" + maininput)
print("-------------------------")
print("\n")
print("Processing...")
print("\n")
fileoutput.write("-------------------------")
fileoutput.write("\n")
fileoutput.write(f"Target: {maininput}")
fileoutput.write("\n")
fileoutput.write("-------------------------")
fileoutput.write("\n")
fileoutput.write("\n")
fileoutput.write("Processing...")
fileoutput.write("\n")
fileoutput.write("\n")
print("-------------------------")
print("Phone Number Informations")
print("-------------------------")
print("\n")
target = phonenumbers.parse(maininput)
TZ = timezone.time_zones_for_number(target)
print("Location: ", TZ)
CC = region_code_for_number(target)
print("Country Code: ", CC)
CR = carrier.name_for_number(target, CC)
print("Carrier: ", CR)
fileoutput.write("-------------------------")
fileoutput.write("\n")
fileoutput.write("Phone Number Informations")
fileoutput.write("\n")
fileoutput.write("-------------------------")
fileoutput.write("\n")
fileoutput.write("\n")
fileoutput.write("Location: ")
fileoutput.write(str(TZ))
fileoutput.write("\n")
fileoutput.write("Country Code: ")
fileoutput.write(str(CC))
fileoutput.write("\n")
fileoutput.write("Carrier: ")
fileoutput.write(str(CR))
fileoutput.write("\n")
fileoutput.write("\n")
print("\n")
print("--------------------------")
print("Phone Number Web Footprint")
print("--------------------------")
print("\n")
fileoutput.write("--------------------------")
fileoutput.write("\n")
fileoutput.write("Phone Number Web Footprint")
fileoutput.write("\n")
fileoutput.write("--------------------------")
fileoutput.write("\n")
fileoutput.write("\n")
footprintsearch = ""
footprint_queries = list(dict.fromkeys([maininput, lookuptarget]))
footprint_results = []
for footprint_query in footprint_queries:
    for footprintsearch in web_search(footprint_query, num_results=10, sleep_interval=2):
        if footprintsearch not in footprint_results:
            footprint_results.append(footprintsearch)
            print(f"[+] Result found on: {footprintsearch}")
            fileoutput.write(f"{footprintsearch}\n")
if not footprint_results:
    print("[-] No web footprint found")
    fileoutput.write("[-] No web footprint found")

print("\n")
print("--------------------------------------------------")
print("Targeted Searches on Online Phone Number Providers")
print("--------------------------------------------------")
print("\n")
fileoutput.write("\n")
fileoutput.write("------------------------------------------------")
fileoutput.write("\n")
fileoutput.write("Targeted Searches on Onine Phone Number Provider")
fileoutput.write("\n")
fileoutput.write("------------------------------------------------")
fileoutput.write("\n")
fileoutput.write("\n")

with open("websites.txt", "r") as extractedwebsites:
    extractedwebsitesread = extractedwebsites.read()
    varwebsites = extractedwebsitesread.splitlines()

i = 0
provider_hits = 0
while i < len(varwebsites):
    query = f"allinurl:{varwebsites[i]} {lookuptarget}"
    for querysearch in web_search(query, num_results=1):
        print(f"[+] Result found: {querysearch}")
        fileoutput.write(f"{querysearch}\n")
        provider_hits += 1
    i += 1
if provider_hits == 0:
    print("[-] No result found")
    fileoutput.write("[-] No result found")

print("\n")
print(Ascii_Art)
print("\n")
fileoutput.write("\n")
fileoutput.write("\n")
fileoutput.write(Ascii_Art)
fileoutput.write("\n")
fileoutput.write("\n")
fileoutput.write(version)
fileoutput.write("\n")
fileoutput.write("\n")
fileoutput.close()

filepath = os.getcwd()
filename = f"{maininput}_results.txt"
print(f"{maininput} Logs saved in {filepath} as '{filename}'")
