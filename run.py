import subprocess
import sys
import os

os.chdir(os.path.dirname(__file__))

executable = os.path.join(".venv", "Scripts", "python")

if not os.path.isdir(".venv"):
    subprocess.check_call((sys.executable, "-m", "venv", ".venv"))
    subprocess.check_call(
        (executable, "-m", "pip", "install", "--upgrade", "pip"))
    subprocess.check_call(
        (executable, "-m", "pip", "install", "-r", "requirements.txt"))

subprocess.check_call((executable, "-m", "src.main"))
