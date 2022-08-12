import re

def profesional(txt):
    text = txt
    x = re.search("<(.+)>([^<]+)</(.+)><(.+)>([^<]+)</(.+)>", text)
    print(x.group(2) + x.group(5))
    

def main():
    txt = "<div class='name'>NOMBRE</div><div class='lastname'>APELLIDO</div>"
    profesional(txt)


if __name__ == '__main__':
    main()