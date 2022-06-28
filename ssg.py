from markdown2 import markdown
from jinja2 import Environment, PackageLoader

def write_file():
    with open("content/post.md", 'r') as file:
        parsed_md = markdown(file.read(), extras=['metadata'])

    env = Environment(loader=PackageLoader('ssg', 'templates'))
    home_template = env.get_template('home.html')

    data = {
    'content': parsed_md,
    'title': parsed_md.metadata['title'],
    'date': parsed_md.metadata['date']
    }

    home_html = home_template.render(post=data)
    with open('home.html', 'w') as file:
        file.write(home_html)