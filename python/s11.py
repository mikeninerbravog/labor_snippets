import sys
from io import StringIO


def start_buffering():
    original_stdout = sys.stdout
    buffer = StringIO()
    sys.stdout = buffer
    return original_stdout, buffer


def end_buffering(original_stdout, buffer):
    sys.stdout = original_stdout
    return buffer.getvalue()


original_stdout, buffer = start_buffering()
print("This is captured.")
captured_output = end_buffering(original_stdout, buffer)

print("Back to the original stdout.")
print("Captured Output:", captured_output)

"""
This Python script demonstrates how to capture and restore the standard output (stdout) using the `sys` and `io` modules. 
It temporarily redirects the output to a `StringIO` buffer, allowing you to capture the printed content and later 
restore the original stdout. Here's a breakdown of the code:

1. **Importing Modules**:
   - `sys`: This module provides access to some variables used or maintained by the interpreter, such as `sys.stdout`.
   - `io.StringIO`: This module provides an in-memory text stream that can be used as a file-like object for reading and writing text.

2. **`start_buffering()` Function**:
   - This function starts the output buffering. It does the following:
     - Saves the original `sys.stdout` in the `original_stdout` variable.
     - Creates a `StringIO` buffer called `buffer`.
     - Redirects the standard output to the `buffer`.
     - Returns `original_stdout` and `buffer` so that you can later restore the original stdout.

3. **`end_buffering()` Function**:
   - This function ends the output buffering. It takes `original_stdout` and `buffer` as arguments.
   - Restores the original stdout by assigning `original_stdout` back to `sys.stdout`.
   - Returns the content of the `buffer` as a string using `buffer.getvalue()`.

4. **Capturing Output**:
   - The script starts output buffering by calling `start_buffering()`, which returns `original_stdout` and `buffer`.
   - It then prints "This is captured." while the output is redirected to the `buffer`.

5. **Restoring Output**:
   - After capturing the output, the script calls `end_buffering(original_stdout, buffer)` to restore the original stdout.
   - It prints "Back to the original stdout."
   - Finally, it prints the captured output using `captured_output`.

When you run this script, it temporarily captures the text that would have been printed and then restores 
the original stdout. This technique can be useful for various purposes, such as capturing and testing print statements or suppressing output in certain parts of your code.
"""