import yaml

the_stuff = yaml.safe_load(open('the stuff.yaml'))

category_names = [next(iter(whatever.keys())) for whatever in iter(the_stuff)]
header_links = '\n'.join(f'\t\t\t\t<a href="../{category}">{category}</a>' for category in category_names)

def generate_table(category):
    category_name, entries = next(iter(category.items()))
    return '\t\t<table>' + ''.join(f'''\t\t\t<tr>
\t\t\t\t<td><button type="button" class="progress" data-key="progress {category_name} {entry['name']}">🤨</button></td>
\t\t\t\t<td><a href="{entry['link']}" target="_blank">{entry['name']}</a></td>
\t\t\t\t<td>{entry['desc']}</td>
\t\t\t</tr>
''' for entry in entries) + '\t\t</table>'

def generate_html(category_name, table): 
    return f'''<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1"> 
		<meta name="description" content="daa's map of mathematics">
        <link rel="icon" href="../favicon.svg" type="image/svg+xml">
		<title>{category_name} · daa's map of mathematics</title>
	</head>
	<body>
		<header>
			<h1 style="text-align: center;"><a href="https://github.com/deftasparagusanaconda" target="_blank">daa</a>'s <a href="../">map of mathematics</a></h1>
			<nav style="text-align: center;">
{header_links}
			</nav>
		</header>
		<main>
{table}
		</main>
        <script src="../progress.js"></script>
	</body>
</html>
'''

for category_name, category in zip(category_names, the_stuff):
    with open(f'{category_name}/index.html', 'w') as file:
        file.write(generate_html(category_name, generate_table(category)))

links = []
for dicty in the_stuff:
    for category_name, entries in dicty.items():
        for entry in entries:
            links.append(entry['link'])

if len(links) != len(set(links)):
    from collections import Counter
    print(f'a few repeated links:\n' + '\n'.join(str(link) for link, count in Counter(links).items() if count > 1))

for dicty in the_stuff:
    category_name, entries = next(iter(dicty.items()))

    if len(entries) != 24:
        print(f'{category_name} has {len(entries)} entries')






# ---
'''
def generate_summary_table():
    categories = {
        category_name: entries
        for category in the_stuff
        for category_name, entries in category.items()
    }

    html = '\t\t<table id="summary">\n'

    html += '\t\t\t<thead>\n'
    html += '\t\t\t\t<tr>\n'
    html += '\t\t\t\t\t<th></th>\n'

    # intentionally blank: no numbered score-like headings
    for _ in range(24):
        html += '\t\t\t\t\t<th></th>\n'

    html += '\t\t\t\t\t<th>mode</th>\n'
    html += '\t\t\t\t</tr>\n'
    html += '\t\t\t</thead>\n'

    html += '\t\t\t<tbody>\n'

    for category_name in category_names:
        entries = categories[category_name]

        html += (
            f'\t\t\t\t<tr data-category="{category_name}">\n'
            f'\t\t\t\t\t<th>{category_name}</th>\n'
        )

        for entry in entries:
            key = f"progress {category_name} {entry['name']}"

            html += (
                f'\t\t\t\t\t<td class="summary-progress" '
                f'data-key="{key}" '
                f'title="{entry["name"]}">🤨</td>\n'
            )

        html += '\t\t\t\t\t<td class="row-mode"></td>\n'
        html += '\t\t\t\t</tr>\n'

    html += '\t\t\t</tbody>\n'

    html += '\t\t\t<tfoot>\n'
    html += '\t\t\t\t<tr>\n'
    html += '\t\t\t\t\t<th>mode</th>\n'

    for position in range(24):
        html += (
            f'\t\t\t\t\t<td class="column-mode" '
            f'data-position="{position}"></td>\n'
        )

    html += '\t\t\t\t\t<td id="overall-mode"></td>\n'
    html += '\t\t\t\t</tr>\n'
    html += '\t\t\t</tfoot>\n'

    html += '\t\t</table>'

    return html

print(generate_summary_table())
'''
