#!/usr/bin/env python

def new_card(title="",date="",i=1):
    fstr = []
    if i == 1:
        k = " show"
    else:
        k = ""
    fstr += ["<div class='card'>\n"]
    fstr += [f"<h6 class='card-header' role='tab' id='headingtemp{i}'>\n"]
    fstr += [f"<a class='collapsed d-block' data-toggle='collapse' data-parent='#accordion' href='#collapsetemp{i}' aria-expanded='false' aria-controls='collapsetemp{i}'>\n"]
    fstr += [f"<i class='fa fa-chevron-down pull-right'></i> {date} - {title}\n"]
    fstr += ["</a>\n"]
    fstr += ["</h6>\n"]
    fstr += [f"<div id='collapsetemp{i}' class='collapse{k}' role='tabpanel' aria-labelledby='headingtemp{i}'>\n"]
    fstr += ["<div class='card-body'>\n"]
    return fstr

import glob,os,pendulum,re
fdir = "/home/dowewas2/github/derekyoungmath/lunches/"

fname = f"{fdir}templates/index_template.html"
with open(fname, "r") as f:
    temp_lines = f.readlines()
for i,line in enumerate(temp_lines):
    if "-- ALL-CARDS --" in line:
        t = i+1
        break

outlines = temp_lines[:t]

files = glob.glob(fdir+"pages/*", recursive=True)
files.sort(reverse=True)
for j,ff in enumerate(files):
    with open(ff, "r") as f:
        lines = f.readlines()
    for i,line in enumerate(lines):
        if "title:" in line:
            title = re.sub("title: ","",line[:-1])
        elif "-- email --" in line:
            c = i
            break
    f = os.path.splitext(ff)[0].split("/")
    stime=pendulum.from_format(f[-1],'MMDDYYYY').format("ddd MMM D, Y")
    outlines += [f"\n<!--card-- pages/{f[-1]}.html --{stime}-->\n\n"]
    outlines += new_card(title=title,date=stime,i=j+1)
    outlines += lines[c+1:] + ["\n\n</div>\n","</div>\n","</div>\n"]

outlines += temp_lines[t:]
with open(f"{fdir}index.html", "w+") as f:
    for line in outlines:
        f.write(line)
