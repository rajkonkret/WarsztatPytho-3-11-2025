from typing import Protocol


# realizacja interfejsu za pomocą Protocol
class Foo(Protocol):
    def bar(self) -> None: ...
