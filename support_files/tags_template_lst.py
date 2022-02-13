"""
Lists all tags for the templates.
This way, there is just one file that defines
this information.
"""
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
def tags_template_lst():
    """
    Create a list with the tags as
    its components.
    """

    tags_dict = {}
    cwd = os.getcwd()

    project_name = "bkmks_ilustrated"
    tags_dict["project_name"] = project_name

    env_folder = f"/usr/share/nginx/html/{project_name}/support_files/templates"
    tags_dict["folder"] = env_folder

    tmp_names = os.listdir("templates/")
    temp_names = [i[:-4] for i in tmp_names]
    tags_dict["templates"] = temp_names

    page_address = "/usr/share/nginx/html/{project_name}/pages/{content[i][0]}.php"
    tags_dict["page"] = page_address

    pg_url = ("http://localhost/{project_name}/pages/'{content[i][0]}'.php",)
    tags_dict["url"] = pg_url

    refresh_rate = 1000
    tags_dict["refresh"] = refresh_rate

    header_title = project_name.upper()
    tags_dict["site_title"] = header_title

    content_tags = {
        "title": "title=content[i][0]",
        "description": "description=content[i][1]",
        "link": "link=content[i][2]",
        "project": project_name,
        "page_url": pg_url,
        "refresh": refresh_rate,
        "header_title": header_title,
    }

    temp_names = os.listdir("templates")
    ltemptags = {}
    for temp in temp_names:
        tp = temp[:-4]
        cmd = f"grep -o -w -P '(?<={{ )[^\s]*(?= }})' {cwd}/templates/{temp} > ../tag_lists/{tp}_tags.txt"  # noqa: W605
        subprocess.run(cmd, cwd="templates/", shell=True)
        with open(f"tag_lists/{tp}_tags.txt", "r") as f:
            co = f.readlines()
            con = []
            for c in co:
                cn = c[:-1]  # Here to remove the '\n' symbol.
                con.append(cn)
            if len(con) != 0:
                cont = list(set(con))
            else:
                pass
            extract = []
            for i in cont:
                ext = {k: v for (k, v) in content_tags.items() if k == i}
                extract.append(ext)
            tags_dict[tp] = extract

    return tags_dict


if __name__ == "__main__":
    tags_template_lst()
