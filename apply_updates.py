import re

with open('tex/Methodology/instrument3-data-collection.tex', 'r', encoding='utf-8') as f:
    content = f.read()

updates = {
    "Pregunta 1": [14, 39, 16, 25, 11],
    "Pregunta 3": [14, 24, 18, 37, 12],
    "Pregunta 4": [8, 13, 28, 48, 8],
    "Pregunta 5": [8, 29, 7, 48, 13],
    "Pregunta 7": [9, 15, 16, 47, 18],
}

def get_pcts(counts):
    total = sum(counts)
    pcts = [round((c / total) * 100, 1) for c in counts]
    # adjust largest to make sum exactly 100.0
    diff = round(100.0 - sum(pcts), 1)
    if diff != 0:
        idx = pcts.index(max(pcts))
        pcts[idx] = round(pcts[idx] + diff, 1)
    return pcts

def make_pie(pcts):
    labels = ["Tot. desac.", "En desac.", "Neutral", "De acuerdo", "Tot. acuerdo"]
    pieces = []
    for p, l in zip(pcts, labels):
        if p > 0:
            pieces.append(f"{p}/{l}")
    return "\\pie[text=legend, radius=2, color={gray!20, gray!40, gray!60, gray!80, gray!100}]{" + ", ".join(pieces) + "}"

def make_table(counts, pcts):
    labels = ["Totalmente en desacuerdo", "En desacuerdo", "Neutral", "De acuerdo", "Totalmente de acuerdo"]
    lines = []
    for l, c, p in zip(labels, counts, pcts):
        p_str = f"{p:.1f}".replace('.', '{,}')
        lines.append(f"{l} & {c} & {p_str}\\,\\% \\\\ \\hline")
    return "\n".join(lines)

# Process Question 1 (convert bar to pie + update table)
p1_counts = updates["Pregunta 1"]
p1_pcts = get_pcts(p1_counts)
content = re.sub(
    r'\\begin\{tikzpicture\}\n\\begin\{axis\}.*?\\end\{axis\}\n\\end\{tikzpicture\}\n\\caption\{Percepción de los pacientes sobre la facilidad para agendar citas\}\n\\label\{fig:p1_barras\}',
    f'\\begin{{tikzpicture}}\n{make_pie(p1_pcts)}\n\\end{{tikzpicture}}\n\\caption{{Percepción de los pacientes sobre la facilidad para agendar citas}}\n\\label{{fig:p1_torta}}',
    content, flags=re.DOTALL
)

# Replace table rows for Question 1
content = re.sub(
    r'Totalmente en desacuerdo & 23 & 21\{,\}9\\,\\% \\\\ \\hline\nEn desacuerdo & 48 & 45\{,\}7\\,\\% \\\\ \\hline\nNeutral & 16 & 15\{,\}2\\,\\% \\\\ \\hline\nDe acuerdo & 13 & 12\{,\}4\\,\\% \\\\ \\hline\nTotalmente de acuerdo & 5 & 4\{,\}8\\,\\% \\\\ \\hline',
    make_table(p1_counts, p1_pcts),
    content
)

# Function to replace pie and table for a given question
def update_question(q_num, old_pie_regex, old_table_regex):
    global content
    counts = updates[f"Pregunta {q_num}"]
    pcts = get_pcts(counts)
    
    # replace pie
    content = re.sub(
        old_pie_regex,
        make_pie(pcts),
        content
    )
    
    # replace table
    content = re.sub(
        old_table_regex,
        make_table(counts, pcts),
        content
    )

# Q3
update_question(3,
    r'\\pie\[.*?\]\{7\.6/Tot\. desac\., 6\.7/En desac\., 17\.1/Neutral, 53\.3/De acuerdo, 15\.2/Tot\. acuerdo\}',
    r'Totalmente en desacuerdo & 8 & 7\{,\}6\\,\\% \\\\ \\hline\nEn desacuerdo & 7 & 6\{,\}7\\,\\% \\\\ \\hline\nNeutral & 18 & 17\{,\}1\\,\\% \\\\ \\hline\nDe acuerdo & 56 & 53\{,\}3\\,\\% \\\\ \\hline\nTotalmente de acuerdo & 16 & 15\{,\}2\\,\\% \\\\ \\hline'
)

# Q4
update_question(4,
    r'\\pie\[.*?\]\{9\.5/En desac\., 26\.7/Neutral, 56\.2/De acuerdo, 7\.6/Tot\. acuerdo\}',
    r'Totalmente en desacuerdo & 0 & 0\{,\}0\\,\\% \\\\ \\hline\nEn desacuerdo & 10 & 9\{,\}5\\,\\% \\\\ \\hline\nNeutral & 28 & 26\{,\}7\\,\\% \\\\ \\hline\nDe acuerdo & 59 & 56\{,\}2\\,\\% \\\\ \\hline\nTotalmente de acuerdo & 8 & 7\{,\}6\\,\\% \\\\ \\hline'
)

# Q5
update_question(5,
    r'\\pie\[.*?\]\{7\.6/Tot\. desac\., 14\.3/En desac\., 15\.2/Neutral, 50\.5/De acuerdo, 12\.4/Tot\. acuerdo\}',
    r'Totalmente en desacuerdo & 8 & 7\{,\}6\\,\\% \\\\ \\hline\nEn desacuerdo & 15 & 14\{,\}3\\,\\% \\\\ \\hline\nNeutral & 16 & 15\{,\}2\\,\\% \\\\ \\hline\nDe acuerdo & 53 & 50\{,\}5\\,\\% \\\\ \\hline\nTotalmente de acuerdo & 13 & 12\{,\}4\\,\\% \\\\ \\hline'
)

# Q7
update_question(7,
    r'\\pie\[.*?\]\{6\.7/Tot\. desac\., 9\.5/En desac\., 15\.2/Neutral, 51\.4/De acuerdo, 17\.1/Tot\. acuerdo\}',
    r'Totalmente en desacuerdo & 7 & 6\{,\}7\\,\\% \\\\ \\hline\nEn desacuerdo & 10 & 9\{,\}5\\,\\% \\\\ \\hline\nNeutral & 16 & 15\{,\}2\\,\\% \\\\ \\hline\nDe acuerdo & 54 & 51\{,\}4\\,\\% \\\\ \\hline\nTotalmente de acuerdo & 18 & 17\{,\}1\\,\\% \\\\ \\hline'
)

with open('tex/Methodology/instrument3-data-collection.tex', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully")
