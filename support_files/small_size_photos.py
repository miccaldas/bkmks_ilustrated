"""Uses Imagemagick to create smaller versions of the photos,
   to put on the homepage."""
import os
import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


@logger.catch
@snoop
def small_size_photos():
    """We use subprocess to access Imagemagick."""

    folder = "screenshots/"
    for filename in os.listdir(folder):
        cmd = f"magick '{filename}' -resize 30% small_{filename}"
        subprocess.run(cmd, cwd="screenshots/", shell=True)


if __name__ == "__main__":
    small_size_photos()
