import hashlib
import base64


def shorten_url(url: str):
    """
    Shorten url using SHA256 and Base64 encoding
    """
    byte_url = url.encode() 
    sha256_obj = hashlib.sha256(byte_url)
    digest_str = sha256_obj.digest()
    encoded_str = base64.urlsafe_b64encode(digest_str)
    shortened_url = encoded_str.decode()[:7]
    return shortened_url


def store_url(orig_url: str, short_url: str):
    """
    Store url in a .txt file
    """
    with open("artifacts/urls.txt", "a") as urlfile:
        urlfile.write(f"{orig_url} {short_url}\n")