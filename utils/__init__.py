import os

from dotenv import load_dotenv

load_dotenv()


def cprint(info: str) -> None:
    print(f"\033[0;30;43m{info}\033[0m")


api_base = os.environ.get("API_BASE")
api_keys = os.environ.get("API_KEYS")
