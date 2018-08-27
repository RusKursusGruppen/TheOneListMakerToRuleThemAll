#!/usr/bin/python3
import os

header = "".join(open('header.tex').readlines()[:-1])

number_of_vejledere = 11
# Format is expected to be [vejldere;rus]
names = open('names.csv').readlines()
rus = [n[:-1] for n in sorted(names[number_of_vejledere:])]
names = list(sorted(names[:number_of_vejledere])) + rus
# Add buffer of rus, that did not sign up in time
names += ["", "", "", "", "", ""]
names = map(lambda n: " ".join([nn.capitalize() for nn in n.split(" ")]), names)
# Format names to have large beginning letter


table = ["\\begin{tabular}{|p{6cm}|p{7cm}|p{4cm}|p{4cm}|p{2.5cm}|}"]
table.append("\\hline \\huge{\\textbf{Navn}} & \\huge{\\textbf{Øl}} & \\huge{\\textbf{Cider}} & \\huge{\\textbf{Sodavand}} & \\huge{\\textbf{Cocio}}\\\\\\hline")

gray = True
rows = 0
for n in names:
    if gray:
        table.append("\\rowcolor{lightgray} " + n + " & & & & \\\\\\hline")
    else:
        table.append(n + " & & & & \\\\\\hline")
    gray = not gray
    rows += 1
    if rows == 33:
        table.append("\\end{tabular}")
        table.append("\\newpage")
        table.append("\\begin{tabular}{|p{6cm}|p{7cm}|p{4cm}|p{4cm}|p{2.5cm}|}")
        table.append("\\hline \\huge{\\textbf{Navn}} & \\huge{\\textbf{Øl}} & \\huge{\\textbf{Cider}} & \\huge{\\textbf{Sodavand}} & \\huge{\\textbf{Cocio}}\\\\\\hline")
        rows = 0


if not (rows == 34):
    table.append("\\end{tabular}")

f = open("output.tex", "w")
f.write(header)
f.write("\n".join(table))
f.write("\\end{document}")
f.close()

os.system("pdflatex output.tex")
os.remove("output.tex")
os.remove("output.aux")
os.remove("output.log")
