"""Helpers for handling datum data."""
import json
import logging


def process_datum(datum: str) -> dict:
    """Decode a string as JSON. The format should look something like
    as follows.

    ```
    data = {}
    data["confirmation"] = True
    data["value"] = "1.234"
    ```
    """
    loaded = json.loads(datum)
    logging.info(loaded)
    return loaded.get("confirmation", False), loaded.get("value", 0)
