import os
import markdown
from jinja2 import Environment, PackageLoader

# Load all the correct directories and save them to a variable
content_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),"content")
post_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),"content/posts")
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),"templates")
site_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")

# Load the jinja2 templates out of /templates
env = Environment(loader=PackageLoader('ssg', 'templates'))
# Load the template to html_template
html_template = env.get_template('layout.html')

# Open the markdown file, save it to input_file and then read it using markdown, and save it to md_content and strip the metadata off.
with open(post_dir + "/post.md", "r", encoding="utf-8") as input_file:
    text = input_file.read()    
md_content = markdown.markdown(text, extensions=['meta'])

# Set the markdown data to data[content]
data = {
'content': md_content
}

# Render the html_output and save it to post
html_output = html_template.render(post=data)

# Using the markdown lib, open the html file and write it, using the html_output
with open(site_dir + "/home.html", 'w') as file:
    file.write(html_output)

############
### TODO ###
############

# Compile each markdown file on each run, create a html file for each markdown file in site folder
#build out jinja2 templates, start with simple layout, build header, footer, post and reiterate posts over homepage
