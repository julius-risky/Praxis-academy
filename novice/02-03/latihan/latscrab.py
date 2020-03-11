from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    """
    Berusaha mendapatkan konten di `url` dengan membuat permintaan HTTP GET.
    Jika tipe konten tanggapan adalah semacam HTML / XML, kembalikan
    konten teks, jika tidak kembalikan Tidak ada
    """
    try:
        with closing(get(url, stream=true)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
        
    except