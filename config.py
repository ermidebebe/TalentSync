from os import environ


class Config:
    """
    This class holds configurations.
    """

    connection_url = environ.get("CONNECTION_URL")
