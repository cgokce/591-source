#### Maven Directory Layout

    https://www.baeldung.com/maven-directory-structure

- Typical Maven Projet has a pom.xml file and a directory structure based on conventions
- It's possible to change project structure but not recommended

Root Directory
- pom.xml - project object model file, defines dependencies and modules
- LICENSE.txt - licensing information
- README.txt
- NOTICE.txt - information about third-party libraries used in project

Root Directory Src Folder
- src/main - contains source code and resources become part of artifact, most important directory
    - src/main/java - Java source code for the artifact
    - src/main/resources - Config files and others such as i18n files, per env configs, xml configs
    - src/main/webapp - For we applications resources like JS, CSS, HTML files, view templates, images
    - serc/main filters - Contains files that inject values into config properties in resources during build phase

Root Directory Test Folder
- src/test - holds all test code and resources
    - /src/test/java - Java source code for tests
    - /src/test/resources - config files and others used by tests
    - /src/test/filters - contains files inject values into config properties in the resources forlder during that phase

Root Directory Other Folders
- src/it - reserved for integration tests used by Maven Failsafe Plugin
- src/site - site documentation generated using Maven Site Plugin
- src/assembly - assembly configuration for packaging binaries