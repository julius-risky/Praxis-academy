from jinja2 import Template

tmpl=Template(
"""
<h1>Hallo,{{nama}}</h1>
"""
)
nama = 'Budi'
print(tmpl.render(nama=nama))