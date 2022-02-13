"""Creates the jinja template for the homepage."""
import os
import random
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
def making_hp_template():
    """
    We'll build a template that chooses
    randomly 15 small pics and shows
    them in the homepage.
    """

    folder = "/usr/share/nginx/html/bkmks_ilustrated/support_files/templates/"
    hptemp = f"{folder}/hp.tpl"
    temp_lst = os.listdir(folder)

    if "hp.tpl" in temp_lst:
        os.remove(hptemp)

    f = open(hptemp, "a")
    f.write('{% extends "base.tpl" %}\n')
    f.write("{% block content %}\n")
    f.write('    <div class="grid-container">\n')
    f.close()

    folder1 = "/usr/share/nginx/html/bkmks_ilustrated/support_files/screenshots/small_sizes"
    small_sizes_list = os.listdir(folder1)
    hp_pics = random.sample(small_sizes_list, 15)

    for pic in hp_pics:
        f = open(hptemp, "a")
        f.write('    <div class="grid-item">\n')
        f.write(f'   <img src="support_files/screenshots/small_sizes/{pic}" alt="alt_{pic}">\n')
        f.write("    </div>\n")
        f.close()

    with open(hptemp, "a") as f:
        f.write("</div>\n")
        f.write("{% endblock %}")


if __name__ == "__main__":
    making_hp_template()
