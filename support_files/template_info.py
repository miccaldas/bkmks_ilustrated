"""Module sources the database as the values for the jinja templates,
   which are loaded in this file."""
import ast
import inspect
import os
import pdb
import re
import subprocess
import sys
import trace

import isort  # noqa: F401
import snoop
from jinja2 import Environment, FileSystemLoader, Template  # noqa: F401
from loguru import logger
from making_hp_template import making_hp_template
from mysql.connector import Error, connect
from snoop import pp, spy

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return 'type({})'.format(source), type(value)


snoop.install(watch_extras=[type_watch])


@logger.catch
@snoop
def run_hp_template():
    """
    As the homepage template has a random component
    that it's cumbersome to implement in jinja, we
    call python modules that creates the template,
    each time with a new composition.
    """
    making_hp_template()


if __name__ == '__main___':
    run_hp_template()


@logger.catch
@snoop
def template_info():
    """Iterating through the titles that have a image, we build a
    list of db information relating only to the entries that we
    have valid pics to show."""

    images = os.listdir("screenshots/")
    new_lst = []
    for image in images:
        new_lst.append(image[:-4])

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="bkmks")
        cur = conn.cursor()
        for new in new_lst:
            args = [new]
            query = "SELECT title, comment, link FROM bkmks WHERE title=%s"
            cur.execute(query, args)
            records = cur.fetchall()
            for row in records:
                with open("screenshots_db.txt", "a") as f:
                    f.write(f"{row[0]}, ")
                    f.write(f"{row[1]}, ")
                    f.write(f"{row[2]},\n")
    except Error as e:
        print("Error while connecting to db", e)
    conn.close()


if __name__ == "__main__":
    template_info()


@logger.catch
@snoop
def dock_checker():
    """
    As the db document is in append mode, running again the
    module, adds repetition to it, making it unusable. To
    ensure this situation doesn't happen, we'll rename the
    db document, so, in case of re-running the script, it
    creates two different documents. But so as not have a
    imensitude of unneeded files, we'll first check if
    it exists a file with the replacement name. If yes, it
    will be deleted, and then rename the new db file to it.
    If it doesn't exist, it will just be renamed.
    """

    file_list = []
    for filename in os.listdir("./"):
        file_list.append(filename)
    if "img_content_lst.txt" in file_list:
        os.remove("img_content_lst.txt")
        os.rename("screenshots_db.txt", "img_content_lst.txt")
    else:
        os.rename("screenshots_db.txt", "img_content_lst.txt")


if __name__ == "__main__":
    dock_checker()


@logger.catch
@snoop
def template_info_cleaning():
    """
    :    We need to make changes to 'template_info'
        so that the final fields, per line,
        look like this:
        First - All info from beginning of line to
                the first comma.
        Second - Info from the end of First + 1,
                 and the penultimate comma.
        Third - Info from end of Second + 1, to
                end of line.
        Then we transform each line in tuples,
        create an new list to house them and, just
        for commodity, create a file with the
        same information as the list.
    """

    with open("img_content_lst.txt", "r") as f:
        imgs = f.readlines()

    character = ","
    comma_idxs = []
    for i in range(len(imgs)):
        icomma = [idx for idx, char in enumerate(imgs[i]) if char == character]
        comma_idxs.append(icomma)

    combi = zip(imgs, comma_idxs)
    lst = []
    tup_lst = []

    if "template_records.txt" in os.listdir("./"):
        os.remove("template_records.txt")

    with open("template_records.txt", "a") as f:
        f.write("[\n")
    for x, y in list(combi):
        inistart = 0
        iniend = y[0]
        ini = x[inistart:iniend]
        scdstart = iniend + 1
        scdend = y[-2]
        scd = x[scdstart:scdend]
        trd = x[(scdend + 1) : -2]  # noqa: E203
        lst = []
        lst.append(ini.strip())
        lst.append(scd.strip())
        lst.append(trd.strip())
        tup = tuple(lst)
        tup_lst.append(tup)
        with open("template_records.txt", "a") as f:
            f.write(f"{tup},\n")
    with open("template_records.txt", "a") as f:
        f.write("]")

    return tup_lst


if __name__ == "__main__":
    template_info_cleaning()


@snoop
@logger.catch
def template_ordering():
    """
    We are ging to setup a system that nobody needs to
    the contents of tags because it is all done
    automatically. This system will extract all information
    by template, and put them in lists, ready to be
    implemented.
    """

    null = []
    with open("temp1.txt", "r") as f:
        data = f.readlines()
    for idx, val in enumerate(data):
        if val == "\n":
            null.append(idx)

    template_names = []
    template_names.append(data[0])
    template_names.append(data[5])
    template_names.append(data[11])
    template_names.append(data[15])
    for u in template_names:
        for d in range(len(data)):
            for i in range(len(data)):
                if u == data[d]:
                    valbox = []
            for n in null:
                rng = range(d < n)
                lenr = len(rng)
                lenr = str(rng)
                rg = (n, val)
                valbox.append(str(rg))

    mic = ["article", "base", "header", "hp"]
    try:
        final = min(mic for mic in valbox if len(mic) > data[d])
    except TypeError:
        pass
    return data


if __name__ == "__main__":
    template_ordering()


@logger.catch
@snoop(depth=3)
def load_templates():
    """
    Where we'll load the site's templates
    with the information gathered in the
    last function.
    I came back with tail between my legs.
    I gave up and edited the output file
    by myself. But I'm already thinking
    in ways of solving this.
    """

    with open("temp1.txt", "r") as f:
        dat = f.readlines()
        data = [i.strip() for i in dat]

    cwd = os.getcwd()

    nulls = [idx for idx, val in enumerate(data) if val == ""]

    article_lst = []
    article_tags = []
    base_lst = []
    base_tags = []
    header_lst = []
    header_tags = []
    hp_lst = []
    hp_tags = []

    for i in range(0, nulls[0]):
        article_lst.append(data[i])
    for i in range(2, nulls[0]):
        article_tags.append(data[i])
        arttags = str([article_tags])
        article_lst.append(arttags[1:-1])

    for i in range(nulls[0] + 1, nulls[1]):
        base_lst.append(data[i])
    for i in range(nulls[0] + 2, nulls[1]):
        base_tags.append(data[i])
        basetags = str(base_tags)
        base_lst.append(basetags[1:-1])

    for i in range(nulls[1] + 1, nulls[2]):
        header_lst.append(data[i])
    for i in range(nulls[1] + 2, nulls[2]):
        header_tags.append(data[i])
        headertags = str(header_tags)
        header_lst.append(headertags[1:-1])

    for i in range((nulls[2]) + 1, len(data)):
        hp_lst.append(data[i])
    for i in range((nulls[2]) + 2, len(data)):
        hp_tags.append(data[i])
        hptags = str(hp_tags)
        hp_lst.append(hptags[1:-1])

    final_lst = [article_lst, base_lst, header_lst, hp_lst]
    print(final_lst)

    if 'template_default.py' in os.listdir(cwd):
        os.remove('template_default.py')

    with open("template_default.py", "a") as f:
        f.write("import os")
        f.write("\n")
        f.write("import isort")
        f.write("\n")
        f.write("import subprocess")
        f.write("\n")
        f.write("import snoop")
        f.write("\n")
        f.write("from jinja2 import Environment, FileSystemLoader, Template  # noqa: f401")
        f.write("\n")
        f.write("from loguru import logger")
        f.write("\n")
        f.write("\n")
        f.write('fmt = "{time} - {name} - {level} - {message}"')
        f.write("\n")
        f.write('logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: e501')
        f.write("\n")
        f.write('logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: e501')
        f.write("\n")
        f.write("\n")
        f.write('subprocess.run(["isort", __file__])')
        f.write("\n")
        f.write("\n")
        f.write("\n")
        f.write("@logger.catch")
        f.write("\n")
        f.write("@snoop")
        f.write("\n")
        f.write("def template_launch():")
        f.write("\n")
        f.write('    "')  # noqa: e202
        f.write('"')  # noqa: e202
        f.write('"')  # noqa: e202
        f.write("    this module launches the templates and performs the actual changes in the site")  # noqa: e202
        f.write('"')  # noqa: e202
        f.write('"')  # noqa: e202
        f.write('"')  # noqa: e202
        f.write("\n")
        f.write("\n")
        f.write("    tups = template_info_cleaning()")
        f.write("\n")
        f.write("    for t in tups:")
        f.write("\n")
        f.write("        print(t)")
        f.write("\n")
        f.write("\n")

    with open("template_default.py", "a") as f:
        for fl in final_lst:
            f.write("    env = Environment(loader=FileSystemLoader('/usr/share/nginx/html/bkmks_ilustrated/support_files/templates/'))")  # noqa: 821
            f.write("\n")
            f.write("   template = env.get_template(f'{fl[0]}')")
            f.write("\n")
            f.write("    for i in range(len(tups)):")
            f.write("\n")
            f.write("        pag = f'/usr/share/nginx/html/bkmks_ilustrated/pages/{tups[i][0]}.php'")
            f.write("\n")
            f.write('   with open(f"{pag}", "w") as d:')
            f.write("\n")
            f.write("            d.write(template.render(")
            f.write("                fl[-1],")
            f.write("                    ))")
            f.write("\n")
            f.write("\n")

    with open("template_default.py", "a") as f:
        f.write("\n")
        f.write("if __name__ == '__main__':")
        f.write("\n")
        f.write("    template_launch()")

    """
    For some reason, there are sed commands that work in command line, and not through python.
    As there will be a lot of them, I created a bash script called 'sed_scripts.sh', in this
    very folder, and it will execute them sequentially.
    """


if __name__ == "__main__":
    load_templates()

#    The solution of exporting data in lists of
#    dictionaries as values of another dictionary
#    has revealed itself as problematic. Suffice
#    to say that Im going to review this situation,
#    because the type-dysphoria it creates is very
#    cumbersome.
#    As a temporary remedy, Im going to make the
#    changes in a text file, and then convert it to
#    a list of tuples with ast.
#    This became sp time consuming that Im going to
#    review the file by hand. What is really
#    is going back and see how to export the data
#    in a more friendly manner. Thi stays here lest
#    we forget.
