#!/usr/bin/env python3
"""Duck typing - first element of a sequence."""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """Return first element of sequence or None if sequence is empty."""
    if lst:
        return lst[0]
    else:
        return None
