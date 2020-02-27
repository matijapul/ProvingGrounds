# Proving grounds

Like the name says, this repository will be your proving ground. You will have to populate this repository by solving multiple tasks aimed to get you familiar and check your expertise in **C++**, **Python**, **Bazel** and **Zuul**.

This project is separated into four categories:
 1. Solve C++ and Python tasks
 2. Bazelize proving-grounds repository
 3. Create build-and-test job
 4. Parse job log file

**Note:** Read the descriptions of all categories below before you start working on the project. First category requires a lot of work and it would be better for you if you solved one C++ and one Python task and then move on to the next category. After completing second and third categories you should return and finish remaining tasks with the help of your fully functioning project-gating system. This way you would get a better insight in how it feels to work with such systems.

## 1.  Solve C++ and Python tasks

There are two folders in this repository **cpp** and **python** which contain C++ and Python tasks, respectively. Each task is located within its own folder and contains a README with an explanation of the task.

Make sure you use **C++17 or later**.

**Hint:** It would best if you start bazelization as soon as you finish your first task instead of finishing all tasks first and then bazelizing them.

## 2. Bazelize proving-grounds repository

Each task you solved in the first section is a single package which needs to be bazelized. In order for the repository to be considered as bazelized, the following must be true:
* Executing `bazel build //...` command in the proving-grounds main folder needs to build all packages successfully. 
* Executing `bazel test //...` command in the proving-grounds main folder needs to run test for each package in the repository. All tests need to execute and pass successfully. 

**Useful link:** https://docs.bazel.build/versions/master/be/overview.html

## 3. Create build-and-test job

Create a job called `bazel-build-and-test` which will build and test your proving-grounds repository using bazel.

**Hint:** Zuul will clone your repository to `/root/src/gerrit/proving-grounds/` node location.
 
Add your newly created job to **check** and **gate** pipelines.

## 4. Parse job log file

Create a playbook which will parse the output of `bazel-build-and-test` job and extract the information on how many tests were executed and how many of them have passed. 

Collected information can be displayed in the node terminal output **(good)** or you can write to a file and store it at the same location where the logs are being stored **(impressive)**.
