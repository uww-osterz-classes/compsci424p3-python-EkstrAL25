[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=14889548)
# UWW COMPSCI 424 Program 3 in Python
 
## Your notes for me

*If you have notes or messages for me, please put them here so I can see them.*

## About this repository

Use this template for Operating Systems Program 3 in Python. 

Write only Python 3 code. Python 2 code is deprecated and is not guaranteed to work.

I will use the command `python3 p3main.py` to run your code. To run correctly, your main file **must** be named `p3main.py`. You can use additional Python files, but make sure to import them into `p3main.py`. No specific project structure is needed.

This Python template repository does not include a virtual environment. You are welcome to add any virtual environment that you like and push it to your own repository. If you just want to keep it simple and run plain Python code, that's fine too.


### Starter code

To help you get started quickly, the starter code file includes code to process the two command-line arguments and begin processing the setup file. You have my permission to use, modify, or delete this code. There are also hints about other steps to complete in the main program.

### Testing

Setup files for the two provided test cases are included in the repository's top-level directory as `424-p3-test1.txt` and `424-p3-test2.txt`. 

If you are using GitHub Codespaces or Visual Studio Code, I have included predefined run configurations for these test cases using manual or automatic mode.

### Problems?

If you encounter problems, please commit and push your code, then [email me](osterz@uww.edu) with a description of what's happening. I will look at your repository on GitHub to try to help you debug.


## Advice for Python programmers

This advice is also posted on the Program 3 page on Canvas. Updates, if any, will be posted there.

Any Python 3 version will work. If you develop on **washington.uww.edu** or another Linux system, make sure your program works with `python3`.

Be aware that Python multithreading may not behave in ways that you expect, since the CPython interpreter's [Global Interpreter Lock](https://wiki.python.org/moin/GlobalInterpreterLock) allows only one thread in a process to execute Python bytecodes at a time.

Learn more about Python multithreading from these sites.

* [The official Python threading library documentation](https://docs.python.org/3/library/threading.html)
* [An Intro to Threading in Python](https://realpython.com/intro-to-python-threading) at [Real Python](https://realpython.com/), one of my favorite Python tutorial sites.

To earn full points, your program's automatic mode must be implemented using the multithreading facilities provided by the Python 3 [threading module](https://docs.python.org/3/library/threading.html). You can use other modules in addition to `threading`, but you must use the `threading` module. This is for consistency with Java and C++ developers.

Here's a link to information about [accepting command-line arguments in Python](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments).
