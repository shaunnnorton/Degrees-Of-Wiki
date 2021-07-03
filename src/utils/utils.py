import requests
from bs4 import BeautifulSoup, re

from src import app, db
from src.models import Page, Matches

invalid_formats = [
    "Wikipedia:",
    "Special:",
    "Main_Page",
    "Portal:",
    "Help:",
    ".jpg",
    "ISBN",
    ".org",
    "File:",
    "(disambiguation)",
]


def check_valid(link: str) -> bool:
    """Checks if the passed link is a valid WikiPedia Link"""
    if any(i in link for i in invalid_formats):
        return False
    return True


def get_links(soup: BeautifulSoup) -> list:
    """Gets all links from a Page"""
    raw_links = soup.find(id="mw-content-text").find_all(
        "a", href=re.compile("/wiki/.")
    )
    clean_links = set()
    for i in raw_links:
        term = clean_link(i.get("href"))
        if check_valid(term):
            clean_links.add(term)
    return clean_links


def clean_link(link: str):
    """Cleans links to a more manageable format"""
    split_string = link.split("/")
    clean = split_string[2]
    return clean


def get_page(term: str) -> Page:
    query = Page.query.filter_by(name=term).first()
    if query:
        return query
    new_page = Page(name=term, links=str(fetch_article_links(term)), queried=1)
    db.session.add(new_page)
    db.session.commit()
    return new_page


def fetch_article_links(term: str):
    response = requests.get(f"https://en.wikipedia.org/wiki/{term}")
    links = get_links(BeautifulSoup(response.text, features="html.parser"))
    return links


def check_match_cache(t1, t2):
    cache = Matches.query.filter_by(name=f"{t1} => {t2}").first()
    if cache:
        return True, cache
    return False, cache


def get_degree(p1, p2):
    """Gets the degree of seperation between links"""
    pass


# print(check_valid("Wikipedia:"))
# print(check_valid("Wikipedia"))
# print(check_valid("Wiki"))
# print(check_valid("Help:"))
# print(clean_link("https://en.wikipedia.org/wiki/Portal:Current_events"))
# print(fetch_article_links("Short_circuit"))
# print(get_page("Short_Circuit"))
