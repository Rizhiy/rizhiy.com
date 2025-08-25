import datetime as dt
import pickle  # noqa: S403
import uuid
from copy import copy
from functools import cache
from urllib.parse import urlparse

import bs4
import requests
from currency_converter import CurrencyConverter
from flask import current_app

CURRENCY_CONVERTER = CurrencyConverter()

HEADERS = {
    "User-Agent": "Rizhiy User Agent 1.0",
}


def get_soup_for_url(url: str) -> bs4.BeautifulSoup:
    headers = copy(HEADERS)
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return bs4.BeautifulSoup(r.text, features="html.parser")


@cache
def get_url_website_base_name(url: str) -> str:
    split_url = urlparse(url)
    split_url = split_url._replace(path="", params="", query="", fragment="")
    url = split_url.geturl()
    if not url:
        return ""
    title = get_soup_for_url(url).title
    if not title:
        return ""
    title = title.text.strip().split(maxsplit=1)[0]
    return title.removesuffix(":")


def get_url_title(url: str) -> str:
    if not url:
        return ""
    if "discogs" in urlparse(url).netloc:
        return "Discogs"
    if "ebay" in urlparse(url).netloc:
        return "Ebay"
    website_name = get_url_website_base_name(url)
    title = get_soup_for_url(url).title
    title = title.text.strip() if title else ""
    if len(title) > 30:
        title = title[:27] + "..."
    return f"{website_name}: {title}"


@cache
def get_exchange_rate(currency: str) -> float:
    if currency == "USD":
        return 1.0
    cache_path = current_app.instance_dir / ".currency_cache" / f"{currency}.pkl"
    if not cache_path.exists():
        cache_path.parent.mkdir(exist_ok=True)
        rate = float(CURRENCY_CONVERTER.convert(1, currency, "USD"))
        with cache_path.open("wb") as f:
            pickle.dump({"date": dt.date.today(), "rate": rate}, f)
        return rate

    with cache_path.open("rb") as f:
        cache = pickle.load(f)  # noqa: S301
    if cache["date"] < dt.date.today():
        cache_path.unlink()
        return get_exchange_rate(currency)
    return cache["rate"]


def get_id() -> str:
    return str(uuid.uuid4())
