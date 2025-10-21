from src.api import fetch_random_joke

def test_fetch_random_joke():
    joke = fetch_random_joke()
    assert isinstance(joke, str)
