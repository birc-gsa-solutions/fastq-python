from typing import TextIO, Iterator


def extract_reads(f: TextIO) -> Iterator[tuple[str, str]]:
    while True:
        try:
            name = next(f).strip()[1:]
            seq = next(f).strip()
            yield name, seq
        except StopIteration:
            return
