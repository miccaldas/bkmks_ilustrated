import os
import isort
import subprocess
import snoop
from jinja2 import Environment, FileSystemLoader, Template  # noqa: f401
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: e501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: e501

subprocess.run(["isort", __file__])


@logger.catch
@snoop
def template_launch():
    """    this module launches the templates and performs the actual changes in the site"""

    tups = template_info_cleaning()
    for t in tups:
        print(t)

    env = Environment(loader=FileSystemLoader('/usr/share/nginx/html/bkmks_ilustrated/support_files/templates/'))
   template = env.get_template(f'{fl[0]}')
    for i in range(len(tups)):
        pag = f'/usr/share/nginx/html/bkmks_ilustrated/pages/{tups[i][0]}.php'
   with open(f"{pag}", "w") as d:
            d.write(template.render(                fl[-1],                    ))

    env = Environment(loader=FileSystemLoader('/usr/share/nginx/html/bkmks_ilustrated/support_files/templates/'))
   template = env.get_template(f'{fl[0]}')
    for i in range(len(tups)):
        pag = f'/usr/share/nginx/html/bkmks_ilustrated/pages/{tups[i][0]}.php'
   with open(f"{pag}", "w") as d:
            d.write(template.render(                fl[-1],                    ))

    env = Environment(loader=FileSystemLoader('/usr/share/nginx/html/bkmks_ilustrated/support_files/templates/'))
   template = env.get_template(f'{fl[0]}')
    for i in range(len(tups)):
        pag = f'/usr/share/nginx/html/bkmks_ilustrated/pages/{tups[i][0]}.php'
   with open(f"{pag}", "w") as d:
            d.write(template.render(                fl[-1],                    ))

    env = Environment(loader=FileSystemLoader('/usr/share/nginx/html/bkmks_ilustrated/support_files/templates/'))
   template = env.get_template(f'{fl[0]}')
    for i in range(len(tups)):
        pag = f'/usr/share/nginx/html/bkmks_ilustrated/pages/{tups[i][0]}.php'
   with open(f"{pag}", "w") as d:
            d.write(template.render(                fl[-1],                    ))


if __name__ == '__main__':
    template_launch()