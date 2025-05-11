import sqlite3
import ssl
from urllib.parse import urlparse

def check_url_safety(url):
    conn = sqlite3.connect("database/ratings.db")
    c = conn.cursor()
    c.execute("SELECT is_safe FROM urls WHERE url=?", (url,))
    row = c.fetchone()
    if row:
        return bool(row[0])

    parsed = urlparse(url)
    if parsed.scheme != "https":
        is_safe = False
    elif any(tld in parsed.netloc for tld in [".gov", ".edu", ".org"]):
        is_safe = True
    else:
        is_safe = False

    c.execute("INSERT INTO urls (url, is_safe) VALUES (?, ?)", (url, int(is_safe)))
    conn.commit()
    conn.close()
    return is_safe
