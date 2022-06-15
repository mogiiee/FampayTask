from .config import app
from . import ops


#invoking the inserter function
@app.task(name="youtube")
def worker():
    ops.Inserter()