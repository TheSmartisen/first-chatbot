from config import Config

def test_config():
    """Vérifie que la clé TOKEN_KEY est bien chargée."""
    assert Config.TOKEN_KEY is not None, "❌ ERREUR : TOKEN_KEY n'est pas défini !"
    assert isinstance(Config.TOKEN_KEY, str), "❌ TOKEN_KEY doit être une chaîne de caractères."
