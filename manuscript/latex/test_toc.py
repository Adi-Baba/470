with open('erdos_paper.cls', 'r') as f:
    tex = f.read()

tex = tex.replace('\\pagestyle{plain}', '\\pagestyle{plain}\n\\setcounter{secnumdepth}{0}\n\\setcounter{tocdepth}{3}')

with open('erdos_paper.cls', 'w') as f:
    f.write(tex)
