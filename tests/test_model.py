import os
import subprocess
import sys


def test_entrenamiento_modelo():
    resultado = subprocess.run(
        [sys.executable, "src/train.py"],
        capture_output=True,
        text=True
    )

    assert resultado.returncode == 0
    assert os.path.exists("models/modelo.pkl")
