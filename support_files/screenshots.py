"""Module that gets screenshots from all sites on the bookmarks
   database, by running through all the urls with a app called
   pageres-cli."""
import subprocess

import isort  # noqa: F401
import snoop
from download_db import download_db
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


@logger.catch
@snoop
def screenshots():
    """We feed the list of urls to a pageres command that
    takes screenshots with an height of 768, in intervals
    of five seconds, to let the pages load."""

    rows = download_db()
    print(rows)
    screen_lst = []
    for row in rows:
        screen_lst.append((row[1], row[3]))

    prefix = "http"
    clean_lst = [x for x in screen_lst if x[1].startswith(prefix)]  # Not all links are located in row[3], so we needed to clean the list.

    for clean in clean_lst:
        cmd = f'pageres {clean[1]} 1366x768 --filename="{clean[0]}" --delay=2 --crop'
        subprocess.run(cmd, cwd="screenshots/", shell=True)


if __name__ == "__main__":
    screenshots()
