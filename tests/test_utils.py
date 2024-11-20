from app.utils import process_text

def test_process_text():
    raw_text = "   This  is    a  test.   "
    clean_text = process_text(raw_text)
    assert clean_text == "This is a test."
