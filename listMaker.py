#!/usr/bin/python3
import os

header = "".join(open('header.tex').readlines()[:-1])

names = list(sorted(open('names.csv').readlines()))
names = [n[:-1] for n in names]

table = ["\\begin{tabular}{|p{6cm}|p{7cm}|p{4cm}|p{4cm}|p{2.5cm}|}"]
table.append("\\hline \\huge{\\textbf{Navn}} & \\huge{\\textbf{Øl}} & \\huge{\\textbf{Cider}} & \\huge{\\textbf{Sodavand}} & \\huge{\\textbf{Cocio}}\\\\\\hline")

gray = True
for n in names:
    if gray:
        table.append("\\rowcolor{lightgray} " + n + " & & & & \\\\\\hline")
    else:
        table.append(n + " & & & & \\\\\\hline")
    gray = not gray
table.append("\\end{tabular}")

f = open("output.tex", "w")
f.write(header)
f.write("\n".join(table))
f.write("\\end{document}")
f.close()

os.system("pdflatex output.tex")
os.remove("output.aux")
os.remove("output.log")
