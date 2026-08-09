from dataclasses import dataclass


@dataclass
class PageDocument:
    page_number: int
    text: str