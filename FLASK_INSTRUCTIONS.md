# Flask

To install Flask C9 you must:

0. Make sure you're using Python 3.6.6 of newer:
```pyenv install 3.6.6``` This could take a while
```pyenv global 3.6.6```

1. Run the install command:
```sudo pip install Flask```

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
