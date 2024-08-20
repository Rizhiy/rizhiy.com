import pytest
from tenacity import retry, stop_after_attempt, wait_fixed

from rizhiy_com.utils import get_url_title


@retry(wait=wait_fixed(10), stop=stop_after_attempt(5))
@pytest.mark.parametrize(
    ("url", "expected"),
    [
        (
            "https://www.amazon.co.uk/dp/B0CJCKGRW1/?coliid=I1CO97PI86B4Y8&colid=30UEPNYNJCJ0W&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it",
            "Amazon.co.uk: The Book. The Ultimate Guid...",
        ),
        (
            "https://www.discogs.com/release/19884919-%D0%AE%D1%80%D0%B8%D0%B9-%D0%A8%D0%B5%D0%B2%D1%87%D1%83%D0%BA-%D0%98-%D0%94%D0%94%D0%A2-%D0%A1%D0%B1%D0%BE%D1%80%D0%BD%D0%B8%D0%BA-%D0%9F%D0%B5%D1%81%D0%B5%D0%BD",
            "Discogs",
        ),
    ],
)
def test_get_url_title(url: str, expected: str):
    assert get_url_title(url) == expected
