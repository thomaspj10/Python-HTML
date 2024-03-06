# Type safe HTML DSL for Python

## Installation
`pip install phtml5`

## Examples
```py
from phtml5 import *

html_template = html()(
    head()(

    ),
    body()(
        h1()("Hello World!")
    )
)

print(str(html_template))

```

```py
from sanic import Sanic, Request, HTTPResponse, html as html_response
from phtml5 import *

app = Sanic("Example")

def index_template(name: str):
    return html()(
        head()(

        ),
        body()(
            h1()(f"Hello {name}!")
        )
    )

@app.get("/")
async def index(request: Request) -> HTTPResponse:
    return html_response(str(index_template("Jane")))

if __name__ == "__main__":
    app.run(host="localhost", port=9999)

```
