from jinja2 import Template

def main():
    t = Template("Hello {{ something }}!")
    t.render(something="World")

    t = Template("My favorite numbers: {% for n in range(1,10) %}{{n}} " "{% endfor %}")
    t.render()

if __name__ == "__main__":
    main()