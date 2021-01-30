#### Maven Local Repository Location

    https://www.baeldung.com/maven-local-repository

- Where Maven Stores all the local dependencies locally - which is in the Maven local repository   
    - When we run local a Maven build all dependencies eg jars, plugin jars, other artifacts are all stored locally for later use
- Maven supports 3 types of repos:
    - Local -> Folder location the local Dev machine
    - Central -> Repo provided by Maven community
    - Remote -> Organization owned custom repository

The Local Repository
- Location on developers machine, usually named as m2
- Can be changed by configuration

        Linux&Mac: ~/.m2 
        Windows: C:\Users\User_Name\.m2

