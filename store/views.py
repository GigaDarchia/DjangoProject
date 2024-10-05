from django.http import HttpResponse
def store(request):
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
        #cart {
            background-color: #23bf11;
            color: white;
            transition-duration: .5s;
            border: 1px black solid;
            padding: 10px;
            border-radius: 5px;
        }
        #cart:hover {
            background-color: #2be715;
        }
        main a {
            text-decoration: none;
        }
        </style>
        <title>Store</title>
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
            <p>This is the store page.</p>
            <div class="products">
                <p>Product 1</p>
                <button id="cart"><a href="/store/product">Add to cart</a></button>
            </div>
        </main>
      </body>
    </html>
        """
    return HttpResponse(html)
def product(request):
    return HttpResponse("Added to cart successfully.")