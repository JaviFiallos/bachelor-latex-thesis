import re

with open('tex/Methodology/instrument3-data-collection.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change bar chart rotation and wrap text for Item 1
content = content.replace(r'x tick label style={rotate=25, anchor=east, font=\small},', r'x tick label style={align=center, text width=1.5cm, font=\small},')
content = content.replace(r'symbolic x coords={1 Tot.\ desac., 2 En desac., 3 Neutral, 4 De acuerdo, 5 Tot.\ acuerdo},', r'symbolic x coords={1 Tot.\\desac., 2 En\\desac., 3 Neutral, 4 De\\acuerdo, 5 Tot.\\acuerdo},')
content = content.replace(r'(1 Tot.\ desac.,', r'(1 Tot.\\desac.,')
content = content.replace(r'(2 En desac.,', r'(2 En\\desac.,')
content = content.replace(r'(4 De acuerdo,', r'(4 De\\acuerdo,')
content = content.replace(r'(5 Tot.\ acuerdo,', r'(5 Tot.\\acuerdo,')

# Function to generate table
def make_table(data_counts, data_pcts):
    labels = ["Totalmente en desacuerdo", "En desacuerdo", "Neutral", "De acuerdo", "Totalmente de acuerdo"]
    lines = [
        r"\begin{center}",
        r"\renewcommand{\arraystretch}{1.25}",
        r"\begin{tabular}{|l|c|c|}",
        r"\hline",
        r"\textbf{Opción} & \textbf{Frecuencia} & \textbf{Porcentaje} \\ \hline"
    ]
    for lbl, count, pct in zip(labels, data_counts, data_pcts):
        pct_str = pct.replace('.', '{,}')
        lines.append(f"{lbl} & {count} & {pct_str}\\,\\% \\\\ \\hline")
    lines.append(r"\textbf{Total} & \textbf{105} & \textbf{100{,}0\,\%} \\ \hline")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{center}")
    return "\n".join(lines)

# Regex to match the chart block and the stats line
pattern = re.compile(
    r'(\\begin\{center\}\n\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}\n\\end\{center\}\n)'
    r'\\textit\{TD=(\d+)\s*\(([\d,\{\}]+)\\,\\%\);\s*D=(\d+)\s*\(([\d,\{\}]+)\\,\\%\);\s*N=(\d+)\s*\(([\d,\{\}]+)\\,\\%\);\s*A=(\d+)\s*\(([\d,\{\}]+)\\,\\%\);\s*TA=(\d+)\s*\(([\d,\{\}]+)\\,\\%\)\.\n'
    r'Total: 105\.\s*Media\\,\$\\approx\$([\d,\{\}]+)\.\}',
    re.DOTALL
)

item_idx = 0
def replacer(match):
    global item_idx
    item_idx += 1
    
    orig_chart = match.group(1)
    
    counts = [match.group(i) for i in (2, 4, 6, 8, 10)]
    pcts_raw = [match.group(i) for i in (3, 5, 7, 9, 11)]
    # Convert {2,}5 to 2.5
    pcts = [p.replace('{,}', '.').replace(',', '.') for p in pcts_raw]
    media = match.group(12)
    
    table_str = make_table(counts, pcts)
    
    stat_str = f"\\textit{{TD={counts[0]} ({pcts_raw[0]}\\,\\%); D={counts[1]} ({pcts_raw[1]}\\,\\%); N={counts[2]} ({pcts_raw[2]}\\,\\%); A={counts[3]} ({pcts_raw[3]}\\,\\%); TA={counts[4]} ({pcts_raw[4]}\\,\\%).\nTotal: 105. Media\\,$\\approx${media}.}}"
    
    if item_idx == 1:
        # Keep original chart
        return f"{orig_chart}{stat_str}\n\n{table_str}"
    else:
        # Replace with pie chart
        pie_data = []
        labels = ["Tot. desac.", "En desac.", "Neutral", "De acuerdo", "Tot. acuerdo"]
        for p, lbl in zip(pcts, labels):
            if float(p) > 0:
                pie_data.append(f"{p}/{lbl}")
        
        pie_str = "\\begin{center}\n\\begin{tikzpicture}\n"
        pie_str += "\\pie[text=legend, radius=2, color={gray!20, gray!40, gray!60, gray!80, gray!100}]{"
        pie_str += ", ".join(pie_data)
        pie_str += "}\n\\end{tikzpicture}\n\\end{center}\n"
        
        return f"{pie_str}{stat_str}\n\n{table_str}"

content = pattern.sub(replacer, content)

with open('tex/Methodology/instrument3-data-collection.tex', 'w', encoding='utf-8') as f:
    f.write(content)
