from django.http import HttpResponse
def home(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <style>
            nav li {
            display: inline-block;
            text-decoration: none;
            padding: 10px;
            margin: 20px;
        }
        nav h1 {
            display: inline-block;
            margin: 0;
            color: #23bf11;
        }
        nav ul {
            display: inline-block;
            padding: 0;
            margin: 0;
            list-style: none;
        }
        nav a {
        text-decoration: none;
        color: black;
        transition-duration: .5s;
        }
        nav a:hover {
            color: #23bf11;
        }
        nav a:clicked {
            color: #2be715;
        }
        </style>
        <title>Home</title>
      </head>
      <body>
        <header>
          <nav>
            <h1>Django Project</h1>
            <ul>
              <li><a href="/">Home</a></li>
              <li><a href="/store/">Store</a></li>
              <li><a href="/order/">Order</a></li>
            </ul>
          </nav>
        </header>
        <main>
            <p>This is the home page.</p>
        </main>
      </body>
    </html>
    """
    return HttpResponse(html)