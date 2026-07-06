from dataclasses import dataclass
from bs4 import BeautifulSoup


@dataclass
class PageData:
    url: str
    html: str
    soup: BeautifulSoup
    links: list[str]
    status_code: int