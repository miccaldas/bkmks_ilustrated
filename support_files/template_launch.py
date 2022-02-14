import os
import subprocess

import isort
import snoop
from jinja2 import Environment, FileSystemLoader, Template  # noqa: f401
from loguru import logger
from template_info import template_info_cleaning

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: e501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: e501

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return 'type({})'.format(source), type(value)


snoop.install(watch_extras=[type_watch])


@logger.catch
@snoop
def template_launch():
    """    this module launches the templates and performs the actual changes in the site"""

    tups = template_info_cleaning()
    for t in tups:
        print(t)

    env = Environment(loader=FileSystemLoader('/usr/share/nginx/html/bkmks_ilustrated/support_files/templates/'))
    template = env.get_template('article.tpl')
    for i in range(len(tups)):
        pag = f"/usr/share/nginx/html/bkmks_ilustrated/pages/{tups[i][0]}.php"
        with open(pag, 'w') as d:
            d.write(template.render(title=f'{tups[i][0]}', description=f'{tups[i][1]}', link=f'{tups[i][2]}'))

    env = Environment(loader=FileSystemLoader('/usr/share/nginx/html/bkmks_ilustrated/support_files/templates/'))
    template = env.get_template('header.tpl')
    with open("/usr/share/nginx/html/bkmks_ilustrated/partials/header.php", "w") as d:
        d.write(template.render(
            header_title='BKMKS_ILUSTRATED', project='bkmks_ilustrated',))

    env = Environment(loader=FileSystemLoader('/usr/share/nginx/html/bkmks_ilustrated/support_files/templates/'))
    template = env.get_template('hp.tpl')
    with open("/usr/share/nginx/html/bkmks_ilustrated/index.php", "w") as d:
        d.write(template.render(header_title='BKMKS_ILUSTRATED', project='bkmks_ilustrated',))


if __name__ == '__main__':
    template_launch()
