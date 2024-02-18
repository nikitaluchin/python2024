from warnings import filterwarnings
filterwarnings("ignore")
import cgi
import html

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "None")
text2 = form.getfirst("TEXT_2", "None")
# экранирование опасных символов
text1 = html.escape(text1)
text2 = html.escape(text2)


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Hospital</title>
        </head>
        <body>""")

print("<h1>Jorik!</h1>")
print(f"<p>TEXT_1: {text1}</p>")
print(f"<p>TEXT_2: {text2}</p>")

print("""</body>
        </html>""")