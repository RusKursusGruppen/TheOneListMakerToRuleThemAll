#!/usr/bin/python3
import os

# Change this parameter to change on what days the rustur will occur
days = ['Tuesday', 'Wednesday', 'Thursday']
# Write out the tjanser. Now, this is a dict, where each entry (i.e. tjanser) have an encoding
# made up of 0s and 1s, where 0 means that it will be blackouted and 1 means it will stay.
# Each entry should have as many "bits" as there are entries in "days".
tjanser = {'Anti-Kaos' : [0, 1, 1],
           'Morgenmad' : [0, 1, 1],
           'Oprydning (Morgenmad)' : [0, 1, 1],
           'Frokost' : [0, 1, 1],
           'Oprydning (Frokost)' : [0, 1, 1],
           'Aftensmad' : [1, 1, 1],
           'Oprydning (Aftensmad)' : [1, 1, 1]}

# Because I'm not a pythonian, you need to specify the order of the keys in a separate parameter...
key_order = ['Anti-Kaos', 'Morgenmad', 'Oprydning (Morgenmad)', 'Frokost', 'Oprydning (Frokost)',
             'Aftensmad', 'Oprydning (Aftensmad)']

# Latex

header = "".join(open('header.tex').readlines()[:-1])

table = ["\\begin{tabular}{|p{6cm}|p{6cm}|p{6cm}|p{6cm}|}"]
table_header = " ".join(["\\Huge{\\textbf{{" + d + "}}} &" for d in days])
table_header = "\\hline & " + table_header[:-1] + "\\\\\\hline"
table.append(table_header)

# This part is purposefully convoluted to avoid any youn  urs-vejleder messing with it
gray = True
for key in key_order:
    tablerow = "\\cellcolor{white} \\Huge{\\textbf{" + key + "}}" + " & "
    for e in tjanser[key]:
        tablerow += " & " if e else "\\cellcolor{black} " + " & "
    tablerow = tablerow[:-2] + "\\\\\\hline"
    if gray:
        tablerow = "\\rowcolor{lightgray} " + tablerow
    table.append(tablerow)
    gray = not gray
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
