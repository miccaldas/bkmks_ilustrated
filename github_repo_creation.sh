#!/usr/bin/env sh

######################################################################
# @author      : mclds (mclds@protonmail.com)
# @file        : github_repo_creation
# @created     : Sunday Feb 13, 2022 20:19:23 UTC
#
# @description : Creates a Github repository from cli,
######################################################################

curl -i -v -H "Authorization: token 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" \
    -d '{ \
         "name": "bkmks_ilustrated", \
         "auto_init": true, \
         "private": false, \
          "gitignore_template": "python", \
         "accept": "application/vnd.github.v3+json", \
         "description": "Web project for bookmarks with pics of the sites", \
         "has_issues": "false", \
         "has_wiki": "false", \
     }' \
https://api.github.com/user/repos
