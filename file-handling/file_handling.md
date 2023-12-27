# File Handling in Programming

* File handling  is a fundamental aspect of programming, allowing developers to interact with files, read and write data, and perform various operations.
* The process of file handling enables us to update, create, open, read, write, and ultimately delete the file/content
that exists in the file.
* It is essential for tasks such as data storage, configuration management, and more.

## Basic File Operations

1. [Checking File Existence](#1-checking-file-existence)
1. [Opening a File](#2-opening-a-file)
1. [Reading from a File](#3-reading-from-a-file)
1. [Writing to a File](#4-writing-to-a-file)
1. [Appending to a File](#5-appending-to-a-file)
1. [Reading and Writing(r+)](#6-reading-and-writingr)
1. [Writing and Reading(w+)](#7-writing-and-readingw)
1. [Loading JSON Data](#8-loading-json-data)
1. [Deleting a File](#9-deleting-a-file)
1. [Closing a File](#10-closing-a-file)

## 1. Checking File Existence

* Before performing operations on a file, it's often useful to check whether the file exists. 
* This can be done using the `os.path.exists` function.

Here's a simple example:
```py
import os

file_name = "new_file"
if os.path.exists(file_name):
    print(f"The file {file_name} exists.")
else:
    print(f"The file {file_name} does not exist.")
```

## 2. Opening a File

* To perform operations on a file, it must first be opened.
* If there is no existing file, it automatically creates a new file.

Here's a simple example of opening a file:
```py
file = open("new_file", "r")
          or
with open("new_file", "r" ) as file
```

## 3. Reading from a File

* Once a file is open, we can read its contents.
* This may involve reading the entire file, specific lines, or a certain number of bytes.

Here's a simple example:
```py
file = open("new_file", "r")
content = file.read()
print(content)
```

## 4. Writing to a File
* Data can be written to a file, either by appending to existing content or by overwriting it. 
* This is useful for creating or updating files.

Here's a simple example:
```py
file = open("new_file", "w")
file.write("Hello, this is a sample text.")
file.close()
```

## 5. Appending to a File

* To add data to the end of an existing file without overwriting its content, we can use the append (a) mode.

Here's a simple examle:
```py
file = open("new_file", "a")
file.write("\nAppended text.")
file.close()
```

## 6. Reading and Writing(r+)

* Files can be opened for both reading and writing using the `r+` mode.

Here's a simple example:
```py
file = open("new_file", "r+")
content = file.read()
print(content)
file.write("Additional text")
file.close()
```

## 7. Writing and Reading(w+)

* Files can be opened for both writing and reading using the `w+` mode.

Here's a simple example:
```py
file = open("new_file", "w+")
file.write("New content")
file.seek(0)  # Moves the file pointer to the beginning
content = file.read()
print(content)
file.close()
```

## 8. Loading JSON Data

* To load JSON data from a file, we can use the `json.loads` function.

Here's a simple example:
```py
import simplejson as json
import os

if os.path.exists("ages_json"):
    old_file = open("ages_json", "r+")
    data = json.loads(old_file.read())
    print("Current age is", data["age"])
else:
    print("The file doesn't exists.")
```

## 9. Deleting a File

* To delete a file, we can use the `os.remove` function.

Here's a simple example:
```py
file_name = "new_file"
if os.path.exists(file_name):
    os.remove(file_name)
    print(f"The file {file_name} has been deleted.")
else:
    print(f"The file {file_name} does not exist.")
```

## 10. Closing a File

* It's important to close a file after finishing operations to release associated resources.
* "release associated resources," it refers to the cleanup process that occurs when a file is closed after being opened and used within a program.
* To close a file, we use `file.close()`.

Here's a simple example:
```py
file = open("new_file", "w")
file.write("Hello, this is a sample text.")
file.close()
```


