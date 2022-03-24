import base64

def encodeURL(url_str: str):
    rv = base64.urlsafe_b64encode(url_str.encode()).decode().strip("=")
    return rv

if __name__ == "__main__":
    print(encodeURL(input("Provide URL: ")))

