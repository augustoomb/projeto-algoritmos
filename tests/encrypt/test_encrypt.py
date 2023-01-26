from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    pass
    with pytest.raises(TypeError):
        encrypt_message(123, "não é um int")

    assert encrypt_message("BCAPAC", "não é um indice valido") == "CAPACB"

    assert encrypt_message("BCAPAC", 3) == "CAP_ACB"

    assert encrypt_message("BCAPAC", 4) == "CA_PACB"
