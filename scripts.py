import subprocess
import sys


def run_command(command):
    result = subprocess.run(command, shell=True, text=True)
    if result.returncode != 0:
        print(f"Command failed with exit code {result.returncode}")
        sys.exit(result.returncode)


def format():
    run_command("ruff format .")


def lint():
    run_command("ruff check .")


def fix():
    run_command("ruff check --fix .")
