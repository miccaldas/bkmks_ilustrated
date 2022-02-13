"""Downloads the content of the bkmks datqabase."""
import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger
from mysql.connector import Error, connect

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


@logger.catch
@snoop
def download_db():
    """Selects all content and returns a list."""

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="bkmks")
        cur = conn.cursor()
        query = """ SELECT * FROM bkmks"""
        cur.execute(query)
        records = cur.fetchall()
        return records
        conn.close()
    except Error as e:
        print("Error while connecting to db", e)


if __name__ == "__main__":
    download_db()
