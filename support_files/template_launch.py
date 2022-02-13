import os
import subprocess

import isort
import snoop
from jinja2 import Template, environment, filesystemloader  # noqa: f401
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="info", format=fmt, backtrace=True, diagnose=True)  # noqa: e501
logger.add("../logs/error.log", level="error", format=fmt, backtrace=True, diagnose=True)  # noqa: e501

subprocess.run(["isort", __file__])


@logger.catch
@snoop
def template_launch():
    """this module launches the templates and performs the actual changes in the site"""

    with open("template_records.txt", "r") as f:
        content = f.readlines()

    for i in content:
        env = environment(loader=filesystemloader("/usr/share/nginx/html/bkmks_ilustrated/support_files/templates/"))
        template = env.get_template("article")
        with open("article", "w") as d:
            d.write(
                template.render(
                    ["description=content[i][1]", "link=content[i][2]"],
                )
            )

        env = environment(loader=filesystemloader("/usr/share/nginx/html/bkmks_ilustrated/support_files/templates/"))
        template = env.get_template("base")
        with open("base", "w") as d:
            d.write(
                template.render(
                    "title=content[i][0]",
                    "description=content[i][1]",
                    "page_url=http://localhost/{project_name}/pages/{content[i][0]}.php",
                    "refresh=1000",
                )
            )

        env = environment(loader=filesystemloader("/usr/share/nginx/html/bkmks_ilustrated/support_files/templates/"))
        template = env.get_template("header")
        with open("header", "w") as d:
            d.write(
                template.render(
                    "header_title=BKMKS_ILUSTRATED",
                    "project=bkmks_ilustrated",
                )
            )

        env = environment(loader=filesystemloader("/usr/share/nginx/html/bkmks_ilustrated/support_files/templates/"))
        template = env.get_template("hp")
        with open("hp", "w") as d:
            d.write(
                template.render(
                    "header_title=BKMKS_ILUSTRATED",
                    "project=bkmks_ilustrated",
                )
            )
