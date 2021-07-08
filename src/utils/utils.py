import requests
from bs4 import BeautifulSoup, re
from datetime import datetime

from src import db
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
    ":",
    "#",
    "wikipedia"
]


def check_valid(link: str) -> bool:
    """Checks if the passed link is a valid WikiPedia Link"""
    if any(i in link for i in invalid_formats):
        return False
    return True


def get_links(soup: BeautifulSoup) -> list:
    """Gets all links from a Page"""
    if soup.table:
        soup.table.decompose()
    raw_links = soup.find(id="mw-content-text").find_all(
        "a", {"class": False, "href": re.compile("/wiki/.")}
    )
    clean_links = set()
    link_list = list()
    for i in raw_links:
        if i.find_parent("p"):
            term = clean_link(i.get("href"))
            if check_valid(term) and term not in clean_links:
                clean_links.add(term)
                link_list.append(term)
    link_str = str(link_list).strip("[]")
    link_str = link_str.replace("'", "")
    link_str = link_str.replace(" ", "")
    return link_str


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
    response = requests.get(
        f"https://en.wikipedia.org/wiki/{term}", allow_redirects=True
    )
    links = get_links(BeautifulSoup(response.text, features="html.parser"))
    return links


def check_match_cache(t1: str, t2: str):
    cache = Matches.query.filter_by(name=f"{t1} => {t2}").first()
    if cache:
        return True, cache
    return False, cache


def get_degree(p1: str, p2: str) -> Matches:
    """Gets the degree of seperation between links"""
    isCached, cache = check_match_cache(p1, p2)
    if isCached:
        return True, cache

    # gets or creates Page models for provided terms
    page1 = get_page(p1)
    page2 = get_page(p2)

    if any(i in (p1 or p2) for i in invalid_formats):
        return False, Matches(
            name=f"{p1} => {p2}",
            url1=page1,
            url2=page2,
            degrees=None,
            last=datetime.now(),
        )

    # gets the string to search for
    match_string: str = page2.name.replace(" ", "_")
    match_string: str = match_string.lower()

    new_match = Matches(
        name=f"{p1} => {p2}",
        url1=page1,
        url2=page2,
        degrees=0,
        last=datetime.now()
    )

    # search for page 2 through many iterations
    iterations = 0
    found_match = False
    links = page1.links
    links = links.split(",")
    comp = page1.links.lower()
    visited = set()
    while iterations < 1000 and not found_match:
        link_num = 0
        if match_string in comp:
            new_match.degrees = iterations + 1
            db.session.add(new_match)
            db.session.commit()
            found_match = True
            break

        while(link_num < len(links) and links[link_num]
                in visited):
            link_num += 1

        if link_num >= len(links):
            break
        visited.add(links[link_num])
        links = get_page(links[link_num])
        comp = links.links.lower()
        links = links.links.split(",")
        if len(links) < 1:
            links = get_page(links[link_num+1])

        iterations += 1
    new_match.degrees = iterations
    return found_match, new_match
