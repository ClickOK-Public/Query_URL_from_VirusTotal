import json, assessURL, encodeURL #, requests

# from pyparsing import line

url_list = []
url_json_data_list = []

# --------------------IMPORTANT------------------------
# Using this script requires an A list of URL's to scan
# -----------------------------------------------------
#
# Insert URLs into URLs.txt file, on the say directory as this .py script file.

with open("URLs_test.txt", "r") as urls:
    for item in urls:
        url_list.append(encodeURL.encodeURL(item).rstrip())

for item in url_list:
    print(item)
    assessURL_rv = assessURL.query_url(item)
    print(assessURL_rv)
    url_json_data_list.append(json.loads(assessURL_rv))

# This section parses the JSON data into a local file
# Optional comment out if not required.
# START - optional section
with open("Temp_URL_query_result.json", "w") as newfile:
    json.dump(url_json_data_list, newfile, indent=2)
# END - optional section

# Modifiy this section according to what data is required from the API respose.
# START
for item in url_json_data_list:
    _url = item["data"]["attributes"]["url"]
    _harmless = item["data"]["attributes"]["last_analysis_stats"]["harmless"]
    _malicious = item["data"]["attributes"]["last_analysis_stats"]["malicious"]
    _suspicious = item["data"]["attributes"]["last_analysis_stats"]["suspicious"]
    _undetected = item["data"]["attributes"]["last_analysis_stats"]["undetected"]
    _timeout = item["data"]["attributes"]["last_analysis_stats"]["timeout"]
# END


# This section determines what is shown on terminal or parsed to a file.
# print details (from url_json_data_list) on-screen
    print(_url, f'{" - Positively malicious site, rating: " if item["data"]["attributes"]["last_analysis_stats"]["malicious"] > 0 else " - Not Malicious site, rating: "}', f"{_malicious}/{int(_harmless) + int(_suspicious) + int(_undetected) + int(_timeout) }")

# print details (from url_json_data_list) to a file.
    with open("Temp_URL_query_result.txt", "a") as newfile:
        line_to_write_str = _url, f'{" - Positively malicious site, rating: " if item["data"]["attributes"]["last_analysis_stats"]["malicious"] > 0 else " - Not Malicious site, rating: "}', f"{_malicious}/{int(_harmless) + int(_suspicious) + int(_undetected) + int(_timeout) } \n"
        newfile.writelines(line_to_write_str)
