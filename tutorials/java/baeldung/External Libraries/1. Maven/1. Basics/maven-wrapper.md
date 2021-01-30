#### Maven Wrapper 

    https://www.baeldung.com/maven-wrapper

- Used in projects that need a specific version of Maven, we can use project-specific wrapper script

Plugin
- Maven wrapper plugin is used to auto installation, to generate files
    - mvnw: execcutable Unix shell script
    - mvnw.cmd: batch script
    - mvn/: hidden folder holds Maven Wrapper java library and properties file

            mvn -N io.takari:maven:wrapper -Dmaven=version

Usage
- After install we can run our goals similarly

        ./mvnw clean install