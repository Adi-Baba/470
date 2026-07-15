import re

with open('main.tex', 'r') as f:
    text = f.read()

# Extract body
body_match = re.search(r'\\vspace\{3em\}\s+(.*)\\end\{document\}', text, re.DOTALL)
body = body_match.group(1).strip() if body_match else ""

# Remove the redundant title and abstract headers that Pandoc generated inside the body
body = re.sub(r'\\hypertarget\{paper-9.*?\\section\{Paper 9:.*?\}\\label\{.*?\}', '', body, flags=re.DOTALL)
body = re.sub(r'\\hypertarget\{abstract\}.*?\\subsection\{Abstract\}\\label\{abstract\}', '', body, flags=re.DOTALL)

title = "Paper 9: c-Exceptional Numbers and Structural Constraints on Odd Weird Numbers (Erdős Problem \\#470)"
abstract = "Erdős Problem \\#470 asks whether any odd weird numbers exist. This paper achieves a massive conditional reduction of the problem, systematically narrowing the search space into an extremely tight mathematical corner. The core results prove that any potential odd weird number must possess at least 4 distinct prime factors ($k \\ge 4$) and adhere to strict \"near-perfect\" abundancy constraints governed by the $M$-core framework. The $c$-exceptional structure allows us to unconditionally eliminate broad classes of integers where the minimum consecutive divisor ratio is bounded by $c^* = 17/11$."

new_tex = f"""\\documentclass{{erdos_paper}}

\\title{{{title}}}
\\author{{Aditya Kumar}}

\\begin{{document}}

\\maketitle

\\begin{{abstract}}
{abstract}
\\end{{abstract}}

\\tableofcontents
\\newpage

{body}

\\end{{document}}
"""

with open('main.tex', 'w') as f:
    f.write(new_tex)
