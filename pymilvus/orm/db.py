from pymilvus import connections


def _get_connection(alias):
    return connections._fetch_handler(alias)


def using_database(db_name, using="default"):
    """ Using a database as a default database name within this connection

    :param db_name: Database name
    :type  db_name: str

    """
    _get_connection(using).reset_db_name(db_name)


def create_database(db_name, using="default", timeout=None):
    """ Create a database using provided database name

    :param db_name: Database name
    :type  db_name: str

    """
    _get_connection(using).create_database(db_name, timeout=timeout)


def drop_database(db_name, using="default", timeout=None):
    """ Drop a database using provided database name

    :param db_name: Database name
    :type  db_name: str

    """
    _get_connection(using).drop_database(db_name, timeout=timeout)


def list_database(using="default", timeout=None) -> list:
    """ List databases

    :return list[str]:
        List of database names, return when operation is successful
    """
    return _get_connection(using).list_database(timeout=timeout)
