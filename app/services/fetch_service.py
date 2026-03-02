import urllib.request
import urllib.error
from bs4 import BeautifulSoup


def fetch_url_content(url: str) -> dict:
    """
    Fetch URL content and return summary + word count.
    """

    response = urllib.request.urlopen(url, timeout=5)
    html = response.read()

    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator=" ", strip=True)

    return {
        "summary": text[:200],
        "word_count": len(text.split())
    }
