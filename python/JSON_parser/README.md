
# JSON parser

Create a Python (3.6 or later) script which uses Requests library to get information from https://jsonplaceholder.typicode.com/todos. The purpose of the script is to sort all TODOs into completed or uncompleted list for each user.

Create a ToDo class which has two lists, one for `"completed": true` and one for `"completed": false`. The script returns a list populated by ToDo objects, where each object represents one user and contains information about all completed and uncompleted tasks of that user.

## Test

Create at least one test and bazelize the package. You can use local installation of Requests library while developing your script but try to use Bazel for handling of such dependencies. 