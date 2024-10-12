from duckdb_sqllogictest.base_decorator import BaseDecorator
from duckdb_sqllogictest.token import Token


class SkipIf(BaseDecorator):
    def __init__(self, token: Token):
        super().__init__(token)