#!/usr/bin/env python
import glob
import sys
import os
import time

commonHTML = """
<html>
    <body>
        {}
    </body>
</html>
"""

def getModTimeStr(name):
    t = time.ctime(os.path.getmtime(name))
    return t

def getSizeStr(name):
    suffixes = [ "KB", "MB", "GB", "TB" ]
    sIdx = 0
    s = os.path.getsize(name)*1.0
    suffix = ""
    while s > 1024.0 and sIdx < len(suffixes):
        s /= 1024.0
        suffix = suffixes[sIdx]
        sIdx += 1

    return "{:.1f} {}".format(s, suffix)

def createIndexForDir():
    files = glob.glob("*")
    files = sorted([n for n in files if n != "index.html" ])

    t = "<table>\n"
    t += "<tr><th>File name</td><th>Modification time</th><th>Size</th></tr>\n"
    for name in files:
        modTime = getModTimeStr(name)
        s = getSizeStr(name)
        t += "<tr><td><a href='{}'>{}</a></td><td>{}</td><td>{}</td></tr>\n".format(name, name, modTime, s)

    t += "</table>\n"

    html = commonHTML.format(t)
    open("index.html", "wt").write(html)

def main():
    dirs = sorted(glob.glob("*.*.*"))
    curdir = os.getcwd()
    
    h = "<h3>Simpact Cyan binaries</h3>\nPlease choose a version:\n<ul>\n"
    for d in dirs:
        os.chdir(curdir)
        os.chdir(d)

        h += "<li><a href='{}'>{}</a></li>\n".format(d,d)
        createIndexForDir()

    os.chdir(curdir)

    h += "</ul>\n"
    html = commonHTML.format(h)
    open("index.html", "wt").write(html)

if __name__ == "__main__":
    main()
