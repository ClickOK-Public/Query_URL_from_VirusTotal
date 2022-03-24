
import requests

# --------------------IMPORTANT------------------------
# Using this script requires an API key from VirusTotal
# -----------------------------------------------------
#
# Insert your private API key into key.txt file, on the say directory as this .py script file.
with open("key.txt", "r") as rawd:
    api_key = rawd.readline()

vt_url = "https://www.virustotal.com/api/v3/urls/"
headers = {
    "Accept": "application/json",
    "x-apikey": api_key
}

def query_url(target_url):
    response = requests.request("GET", f"{vt_url}{target_url}", headers=headers)
    # print(response.text)
    return response.text

if __name__ == "__main__":
    query_url(input("Provide URL:"))