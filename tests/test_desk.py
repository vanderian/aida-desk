import aida_desk


def test_the_page_is_served_and_is_self_contained():
    html = aida_desk.page().decode()
    assert "<title>aida desk</title>" in html
    assert "http://" not in html.replace("http://127.0.0.1", "") and "https://" not in html, "the page loads nothing from anywhere"
