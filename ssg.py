import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from markdown2 import markdown
from jinja2 import Environment, PackageLoader

class Watcher:

    def __init__(self, directory=".", handler=FileSystemEventHandler()):
        self.observer = Observer()
        self.handler = handler
        self.directory = directory

    def run(self):
        self.observer.schedule(
            self.handler, self.directory, recursive=True)
        self.observer.start()
        print("\nWatcher Running in {}/\n".format(self.directory))
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
        self.observer.join()
        print("\nWatcher Terminated\n")


class MyHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        print(event) 
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

if __name__=="__main__":
    w = Watcher(".", MyHandler())
    w.run()