# Flask

To install Flask C9 you must:

1. Run the install command:
```sudo easy_install Flask```

2. Create a file, (```app.py```). Do not use flask.py, it can generate conflicts with the flask application.

3. Paste this code into ```app.py```:

```python
import os
from flask import Flask
  
app = Flask(__name__)
  
@app.route('/')
def hello():
    return 'Hello World'
  
  
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
```

4. Click ```run```, C9 top bar. Remember to have the file opened.

5. *voilá*, backend server running.