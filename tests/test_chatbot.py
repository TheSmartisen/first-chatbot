from utils import translate_to_french

def test_translation():
    result = translate_to_french("Hello")
    assert result.lower() == "bonjour."
