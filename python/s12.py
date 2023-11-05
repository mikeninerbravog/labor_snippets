import sys
from contextlib import contextmanager
from io import StringIO


@contextmanager
def capture_output():
    buffer = StringIO()
    original_stdout = sys.stdout
    sys.stdout = buffer
    yield buffer
    sys.stdout = original_stdout


with capture_output() as buffer:
    print("This is captured.")
captured_output = buffer.getvalue()
print("Back to the original stdout.")
print("Captured Output:", captured_output)

"""
This Python script demonstrates how to capture and restore the standard output (stdout) using a context manager, 
the `sys` and `io` modules. It temporarily redirects the output to a `StringIO` buffer, 
allowing you to capture the printed content and later restore the original stdout. Here's a breakdown of the code:

1. Importing Modules:
   - `sys`: This module provides access to some variables used or maintained by the interpreter, such as `sys.stdout`.
   - `contextlib.contextmanager`: This module provides a decorator for creating context managers.
   - `io.StringIO`: This module provides an in-memory text stream that can be used as a file-like object for reading and writing text.

2. `capture_output()` Function Using `@contextmanager`:
   - This function is a generator that serves as a context manager, allowing you to capture output within a specific block of code.
   - It starts the output buffering. It does the following:
     - Creates a `StringIO` buffer called `buffer`.
     - Saves the original `sys.stdout` in the `original_stdout` variable.
     - Redirects the standard output to the `buffer`.
     - Yields the `buffer`, allowing code within the context manager to run.
     - Restores the original stdout after the block is exited.

3. Using the Context Manager:
   - The `with capture_output() as buffer:` statement creates a context in which the standard output is redirected to the `buffer`.
   - Within this context, `print("This is captured.")` is executed, and the output is captured in the `buffer`.

4. Restoring Output and Accessing Captured Output:
   - After the `with` block, the original stdout is automatically restored.
   - The `captured_output` variable is set to the content of the `buffer` using `buffer.getvalue()`, allowing you to access the captured output.

5. Printing Captured Output:
   - The script prints "Back to the original stdout."
   - It also prints "Captured Output:", followed by the content captured in the `buffer`.

When you run this script, it temporarily captures the text that would have been printed within the `with` 
block and then restores the original stdout. 
This technique can be useful for various purposes, such as capturing and testing print statements 
or suppressing output in certain parts of your code. 
Using a context manager provides a cleaner and more automated way to handle the redirection 
and restoration of standard output.

"""
