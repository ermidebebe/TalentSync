"""
create_tables module
"""
import pandas as pd
from tenacity import (
    retry,
    wait_random_exponential,
    retry_if_not_exception_type,
)
import sqlalchemy as db
from sqlalchemy.exc import ProgrammingError, IntegrityError, DataError


class CrudOperations:
    """
    This class creates tables on a database.
    """
    @staticmethod
    @retry(
        wait=wait_random_exponential(min=1, max=20),
        retry=(
            retry_if_not_exception_type(ProgrammingError)
            & retry_if_not_exception_type(IntegrityError)
            & retry_if_not_exception_type(DataError)
        ),
    )
    def read_data(query: str, connection_url) -> pd.DataFrame:
        """
        This method reads data from a database table.
        :param connection:
        :param query:
        :return pd.DataFrame:
        """
        engine = db.create_engine(connection_url)
        connection = engine.connect()
        data = pd.read_sql(query, connection)
        connection.close()
        engine.dispose()
        return data
