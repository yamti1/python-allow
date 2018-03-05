# python-allow
A little Python recipe for simple exception handling

**UPDATE:** Python 3.4 introduced [`contextlib.suppress`](https://docs.python.org/dev/library/contextlib.html#contextlib.suppress), making this obsolete.

This makes you able to replace this:
```python
try:
    # code...
except AnError:
    pass
```
with this:
```python
with allow(AnError):
    # code...
```
