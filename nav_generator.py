import json

with open('nav.json') as data_file:
    data = json.load(data_file)

css = data['css']

nav = css[0]['nav']
li = css[1]['li']
a = css[2]['a']
selected = css[3]['aS']

html = ''

for i, d in enumerate(data['menu']):
    html += "<ul style={}>".format(nav)
    for e in data['menu']:
        
        if d['slug'] == e['slug']:
            html += "<li style='{0}'><a href='/{1}' style='{2}'>{3}...</a></li>".format(li, e['slug'], selected, e['title'])

        else:
            html += "<li style='{0}'><a href='/{1}' style='{2}'>{3}.</a></li>".format(li, e['slug'], a, e['title'])
            
    html += "</ul>"

    if i == 3:
        with open("menu.html", "w") as text_file:
            text_file.write(html)


    


