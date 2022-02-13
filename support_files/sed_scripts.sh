#!/usr/bin/env sh

######################################################################
# @author      : mclds (mclds@protonmail.com)
# @file        : sed_scripts
# @created     : Saturday Feb 12, 2022 21:06:19 UTC
#
# @description : Collects all Sed scripts that I was unable to make
#                work through Python, and executes in sequence.
######################################################################

# 1 - Retira as aspas em volta tag title.
echo 'Starting Script1'
sed -re "s/'title=content\[i]\[0]'/title=content\[i]\[0]/g1" template_default.py > trans1.py

# 2 - Retira as apas em volta da tag description.
echo 'Starting Script2'
sed -re "s/'description=content\[i]\[1]'/description=content\[i]\[1]/g1" trans1.py > trans2.py

# 3 - Retira [] do environment article.
echo 'Starting Script3'
sed -re "s/\[description=content\[i]\[1], 'link=content\[i]\[2]']/description=content\[i]\[1], link=content[i][2]/g1" trans2.py > trans3.py

# 4 - Retira '' da tag page_url
echo 'Starting Script4'
sed -re "s/'page_url.*.php',/page_url='http:\/\/localhost\/{project_name}\/pages\/{content\[i]\[0]}.php',/g1" trans3.py > trans4.py

# Retira aspas na tag refresh.
echo 'Starting Script 5'
sed -re 's/\x27refresh.*$/refresh=1000,/g1' trans4.py > trans5.py

# Retira aspas da tag header_title.
echo 'Starting Script6'
sed -re "s/'header_title=BKMKS_ILUSTRATED',/header_title='BKMKS_ILUSTRATED',/g1" trans5.py > trans6.py

# Retira aspas da tag project.
echo 'Starting Script7'
sed -re "s/'project=bkmks_ilustrated'/project='bkmks_ilustrated'/g1" trans6.py > trans7.py

# Muda o nome de trans7.py, para template_launch.py.
echo 'Starting Script8'
mv trans7.py template_launch.py

