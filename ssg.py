import markdown
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('ssg', 'templates'))
layout_template = env.get_template('layout.html')

with open("post.md", "r", encoding="utf-8") as input_file:
    text = input_file.read()    
md_content = markdown.markdown(text, extensions=['meta'])

data = {
'content': md_content
}

home_html = layout_template.render(post=data)
with open('home.html', 'w') as file:
    file.write(home_html)