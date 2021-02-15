#!/usr/bin/env python

# Write MailTags to Finder Tags
# Bryan Miller
# 2021-02-05

from __future__ import print_function
# import sys
import os
# import argparse
import subprocess
import json

home = os.environ['HOME']
# print(home)
mailroot = home + "/Library/Mail/"

if __name__ == "__main__":
    # Get list of recently modified Mail files
    process = subprocess.Popen([home + "/bin/findmails.sh"], encoding="UTF-8",
                               stdout=subprocess.PIPE)
    try:
        outs, errs = process.communicate(timeout=30)
    except subprocess.TimeoutExpired:
        process.kill()
        outs, errs = process.communicate()
        exit()
    files = outs.rstrip("\n").split("::")

    # Loop over files
    for file in files:
        # print(file)
        # f = open(mailroot + file, "r")
        # lastlines = f.readlines()[-29:]
        # f.close()
        # print(lastlines)

        mailfile = mailroot + "/V5/" + file
        process = subprocess.Popen(["/usr/bin/grep", "-A 1", "com.smallcubed", mailfile], encoding="UTF-8",
                                   stdout=subprocess.PIPE)
        try:
            outs, errs = process.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            outs, errs = process.communicate()
            continue
        # print(outs)
        splits = outs.strip("\n").split("/")
        tagdir = splits[-3][splits[-3].rfind('>')+1:]
        tagid = splits[-2][0:-1]
        # print(tagdir, tagid)

        process = subprocess.Popen(["/usr/local/bin/gfind", mailroot + "SmallCubed/TagData/", "-type", "f",
                                    "-path", "*" + tagdir + "*", "-name", "*" + tagid + "*"],
                                   encoding="UTF-8", stdout=subprocess.PIPE)
        try:
            outs, errs = process.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
            outs, errs = process.communicate()
            continue
        mktag = outs.rstrip("\n")
        # print(mktag)

        try:
            with open(mktag, "r") as f:
                tagdict = json.load(f)
        except Exception:
            continue

        # print(tagdict["TAGS"])
        if "kw" in tagdict["TAGS"].keys():
            tags = ""
            for tag in tagdict["TAGS"]["kw"]:
                tags += tag + ","
            # tags = tags.rstrip(",")
            # print(tags)

            process = subprocess.Popen(["/usr/local/bin/tag", "-s", tags, mailfile],
                                       encoding="UTF-8", stdout=subprocess.PIPE)
            try:
                outs, errs = process.communicate(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                outs, errs = process.communicate()

            # print()
