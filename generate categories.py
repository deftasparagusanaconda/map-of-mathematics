import yaml

the_stuff = yaml.safe_load(open('the stuff.yaml'))

category_names = [next(iter(whatever.keys())) for whatever in iter(the_stuff)]
header_links = '\n'.join(f'\t\t\t\t<a href="../{category}">{category}</a>' for category in category_names)

def generate_table(category):
    category_name, entries = next(iter(category.items()))
    return '\t\t<table>' + ''.join(f'''\t\t\t<tr>
\t\t\t\t<td><a href="{entry['link']}" target="_blank">{entry['name']}</td>
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
