# Scenario

Your task is to implement a simplified version of a file hosting service.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
press “Submit” often to run tests and receive partial credits for passed tests. Please check tests for requirements
and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, not all together, keeping in mind that you will need to refactor to support additional functionality.
Please, do not change the existing method signatures.

## Task

Example of file structure with various files:

```plaintext
[server34] - 24000 Bytes Limit
    Size
    +- file-1.zip 4321 Bytes
    +- dir-a
    |   +- dir-c
    |   |   +- file-2.txt 1100 Bytes
    |   |   +- file-3.csv 2122 Bytes
    +- dir-b
    |   +- file-4.mdx 3378 Bytes
```

## Level 1 – Initial Design & Basic Functions

- **FILE_UPLOAD(file_name, size)**
  - Upload the file to the remote storage server.
  - If a file with the same name already exists on the server, it throws a runtime exception.
- **FILE_GET(file_name)**
  - Returns the size of the file, or nothing if the file doesn’t exist.
- **FILE_COPY(source, dest)**
  - Copy the source file to a new location.
  - If the source file doesn’t exist, it throws a runtime exception.
  - If the destination file already exists, it overwrites the existing file.

## Level 2 – Data Structures & Data Processing

- **FILE_SEARCH(prefix)**
  - Find top 10 files starting with the provided prefix. Order results by their size in descending order, and in case of a tie by file name.
