# Query_URL_from_VirusTotal
Use VirusTotal API to query information on a given URL

## Important/Prerequisites
- Personal VirusTotal account required to obtain API key
  - Insert said key into the key.txt file.
- A list of URLs to scan
  - Provide URLS in the URLs.txt file
  - 1 URL per line

## General use

There are two python scripts required to be imported as modules:
- assessURL.py
- encodeURL.py

These scripts can be run individually from command line.

The "main" script is:
- assess_urls_VirusTotal.py

This script imports the two modules mentioned earlier, and utilize them to create output files:
- URL_query_result.json
- URL_query_result.txt