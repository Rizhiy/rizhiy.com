import datetime as dt
import pickle  # noqa: S403
import uuid
from functools import cache
from pathlib import Path

import bs4
import requests
from currency_converter import CurrencyConverter

CURRENT_DIR = Path(__file__).parent
CURRENCY_CONVERTER = CurrencyConverter()


def get_url_title(url: str) -> str:
    r = requests.get(url)
    title = bs4.BeautifulSoup(r.text).title
    return title.text if title else ""


@cache
def get_exchange_rate(currency: str) -> float:
    if currency == "USD":
        return 1.0
    cache_path = CURRENT_DIR / ".currency_cache" / f"{currency}.pkl"
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
