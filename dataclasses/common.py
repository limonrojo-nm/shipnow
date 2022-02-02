from dataclasses import asdict


class WithAsDict:
    @property
    def as_dict(self): return asdict(self)
