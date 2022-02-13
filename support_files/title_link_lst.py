"""We'll create a file with tuples keeping the titles of the photos
   that were minimized as well as their links, so we can use them on
   the homepage of the site."""
import inspect
import os
import shutil
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
def title_link_lst():
    """
    We first take a list of links from the photos that were
    effectively taken, and add to it the titles and links to
    the minimized photographs.
    After that we have to clean the document, which is done
    mainly with Sed.
    """

    os.chdir("screenshots/small_sizes/")
    title_list = []
    for filename in os.listdir("./"):
        title = filename[6:-4]
        title_list.append(title)

    with open("/usr/share/nginx/html/bkmks_ilustrated/support_files/title_link_list.txt", "w") as f:
        f.write("[")

        try:
            conn = connect(host="localhost", user="mic", password="xxxx", database="bkmks")
            cur = conn.cursor()
            for title in title_list:
                args = [title]
                query = "SELECT link FROM bkmks WHERE title=%s"
                cur.execute(query, args)
                lnk = cur.fetchone()
                link = str(lnk)

                with open("/usr/share/nginx/html/bkmks_ilustrated/support_files/title_link_list.txt", "a") as f:
                    f.write(f"{title}, ")
                    f.write(f"{link},")
                    f.write("\n")
        except Error as e:
            print("Error while connecting to db", e)
        finally:
            if conn:
                conn.close()

    os.chdir("/usr/share/nginx/html/bkmks_ilustrated/support_files/")

    with open("/usr/share/nginx/html/bkmks_ilustrated/support_files/title_link_list.txt", "a") as f:
        f.write("]")

    cmd = "sed 's/...$//g' title_link_list.txt > noaspas.txt"
    subprocess.run(cmd, shell=True)
    cmd = "sed 's/, (/, /g' noaspas.txt > noaspas1.txt"
    subprocess.run(cmd, shell=True)
    cmd = "sed '/, No$/d' noaspas1.txt > no_null.txt"
    subprocess.run(cmd, shell=True)

    """
    Had to do the following command, "sed 's/.*/<apostrophe>&/g' title_link_list.txt > temp.txt", on the shell because I had to
    put apostrophe in the expression, but Vim deletes the quoting character that is needed for that. I'll leave the command here
    for documentation purposes.
    This produces the file 'sed_shell_cmd_1.txt'
    """
    cmd = "sed '1 s/^.*$/[/' temp.txt > temp1.txt"
    subprocess.run(cmd, shell=True)
    cmd = "sed '$s/^.*$/]/' temp1.txt > temp2.txt"
    subprocess.run(cmd, shell=True)

    """
    Same thing as before, now with this script, sed 's/, /<apostrophe>, /g'. This produces the file
    'sed_shell_cmd_2.txt'.
    Another one, sed 's/'//g' temp3.txt > sed_shell_cmd_3.txt.
    """

    os.remove("title_link_list.txt")
    os.remove("noaspas.txt")
    os.remove("noaspas1.txt")
    os.rename("no_null.txt", "title_link_list.txt")
    os.remove("temp1.txt")
    os.remove("temp2.txt")
    os.remove("title_link_list.txt")
    shutil.copyfile("temp4.txt", "clean_lst.txt")

    with open("/usr/share/nginx/html/bkmks_ilustrated/support_files/clean_lst.txt", "r") as f:
        titlnk = f.readlines()

    with open("final_list.txt", "a") as f:
        f.write("[\n")
    for i in range(1, len(titlnk)):
        spls = []
        line = titlnk[i]
        publication = line.split(",", 1)[0]
        try:
            url = line.split(",", 1)[1]
        except IndexError:
            pass
        lst = []
        lst.append(publication)
        lst.append(url.strip())
        tup = tuple(lst)
        with open("final_list.txt", "a") as f:
            f.write(f"{tup},\n")

    with open("final_list.txt", "a") as f:
        f.write("]")

    cmd = "sed '46d' final_list.txt > final_lst.txt"
    subprocess.run(cmd, shell=True)

    os.remove("final_list.txt")
    os.remove("clean_lst.txt")


if __name__ == "__main__":
    title_link_lst()
