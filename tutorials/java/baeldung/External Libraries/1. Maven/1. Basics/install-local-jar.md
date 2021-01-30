#### Install local jar with maven

    https://www.baeldung.com/install-local-jar-with-maven/

- Problem, we have a jar that does not exist in public repositories
    - Choices are, install repo management eg Nexus, try to get artifact uploaded on plublic repos, or install using maven plugin
- Installing maven plugin locally is the easierst

Install with Plugin
- Add maven-install-plugin to pom file with config including jar location and artifact coordinates

        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-install-plugin</artifactId>
            <version>2.5.1</version>
            <configuration>
                <groupId>org.example</groupId>
                ...
                <file>${basedir}/dependencies/myartifact.jar</file>
            </configuration>
            <executions><execution>
                <id>install-my-lib</id>
                <goals>
                    <goal>install-file</goal>
                </goals>
                <phase>validate</phase>
            ...

