import typing as t


T = t.TypeVar('T')


class IFormatter(t.Protocol):
    def handle(self, data: t.Any) -> t.Any: ...


class ITextFormatter(IFormatter):
    def handle(self, data: str) -> str: ...


class Pass(IFormatter):
    def handle(self, data: T) -> T:
        return data
