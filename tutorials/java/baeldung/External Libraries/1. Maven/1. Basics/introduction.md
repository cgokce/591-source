#### Apache Maven Tutorial

    https://www.baeldung.com/maven

- Building software project consists of different tasks eg.
    - Downloading dependencies, putting additional jars on a classpath, compiling source code into binary
    - Packaging compiled code into deployable artifacts such as JAR, WAR, and ZIP, deploying them to server
- Apache Maven automates tasks, minimizing the risk of humans making errors while building software manually
    - Seperating the work of compiling and packaging our code from that of code construction

Why Use Maven
- Simple project setup follows best practices: minimum configuration
- Dependency Management: Includes automatic updating downloading and validating the compatibility
- Isolation between project dependencies and plugins
    - Dependencies are from dependency repos and plugins are from plugin repos
- Central Repository System: Project dependencies can be loaded from the local file system or public repos eg. Maven Central

Project Object Model
- POM file describes project, manages dependencies and configures plugins
- Also defines replationships among modules of multi-module projects

Project Identifiers
- Uses a set of identifiers also called coordinates to uniquely identify a project and specify how the project artifact will be packaged   
- These three identifiers combined to form the unique identifier
    - groupId - unique base name of company or group generated the project
    - artifactId - unique name of the project
    - version - version of the project

Dependencies
- Uses less storage, makes checking out a project quicker, provides an effective platform for exchanging binary artifacts

Repositories
- Default local depository is in `home/.m2/repository` folder
- If artifact is in local repositroy Maven uses it otherwise downloaded from central repo, default is Maven Central
- You need to include repository to make maven download them

        <repositories>
            <repository>
                <id>JBoss repo</id>
                <url>http://....</url>
            </repository>
        </repositories>


Properties
- Key/value placeholders accessible anywhere within the pom xml file
- Also often used to define build path variables

        <properties>
            <spring.version>4.3.5.RELEASE</spring.version>
        </properties>

        // Later use it as
        ${spring.version}

Build
- Provides information about the maven goal

        <build>
            <defaultGoal>install</defaultGoal>
            <directory>${basedir}/target</directory>
            <finalName>${artifactId}-${version}</finalName>
            ...

        </build>

- Profile is set of configuration values for the builds, different environments and settings

        <profiles>
            <profile>
                <id>dev</id>
                <build><plugins><plugin>...
                </build></plugins></plugin>
            </profile>
        </profiles>

        // To run the desired profile
        mvn clean install -Pdev

---

Maven Build Lifecycle Phases
- validate - check the correctness of project
- compile - compiles source code into the binary artifacts
- test - execute unit tests
- package - package into archive file
- integration-test - executes additional tests requiring packagin
- verify - check if package is valid
- install - installs the package file into the local Maven repository
- deploy - deploy the package file to a remote server or repo

Plugins and Goals
- Maven plugin is a collection of one or more goals
- Rich list of plugins that are officially supported by Maven is available here
- Goals by plugins can be associated with different phase of the lifecycle

Building Maven Project
- Generate using maven generate or IDE
- Compile a project using `mvn compile`, maven will go through all the lifecycle process to compile
- Invoke the tests `mvn test`
- Invoke the package phase whill will produce the compiled archive jar file `mvn package`

Executing Maven Project
- We can execute our Java project with `exec-maven-plugin`
- To execute application, run the `mvn exec:java`

---


Multi-module projects
- Maven handles multi-module(aggregator) projects via Reactor
- Reactor collects all available modules to build, then sorts projects into the correct build order, then builds them one by one

Generate parent project
- Update tht packaging type inside the pom.xml file to indicate parent module

        <packaging>pom</packaging>

- We generate the submodules for the parent project using the parent pom files, then add the modules to main pom file

        <modules>
            <module> core </module>
            <module> service </module>
            <module> webapp </module>
        </modules>

- Also add the parent section to the submodules

        <parent>
            <groupId>org.baeldung</groupId>
            <artifactId>parent-project</artifactId>
            <version>1.0-SNAPSHOT</version>
        </parent>

- Enable Dependency Management in Parent Project
    - Dependency management is a mechanism for centralizing the dependency information for a muılti-module parent project and its children
    - This will simplify the references to the artifacts in the child POMs

            // Parent defines the dependency management section
            <dependencyManagement>
                <dependencies>
                    <dependency>
                        <groupId>org.springframework</groupId>
                        <artifactId>spring-core</artifactId>
                        <version>4.3.5.RELEASE</version>
                    </dependency>
                </dependencies>
            </dependencyManagement>

            // All submodules depend on a shared module can declare using only groupid and artifactId, version will be inherited
            <dependencies>
                <dependency>
                    <groupId>org.springframework</groupId>
                    <artifactId>spring-core</groupId>
                </dependency>
                ...
            </dependencies>

- You can provide exclusions for dependency management in parent's pom, so that specific libraries will not be inherited by child modules:
    
        <exclusions>
            <exclusion>
                <groupId>org.springframework</groupId>
                <artifactId>spring-context</artifactId>
            </exclusion>
        </exclusions>

        // If child want different version of the library then it can declare it
    
- Parent project does not necessarily to have modules that it aggregates, another setups also possible

---

Updating submodules and building a project
- We can change packaging type of each suvmodule
- Let's change the packaging of the webapp module to war, then build it, `mvn clean install`

        [INFO] Scanning for projects...
        [INFO] Reactor build order:
        [INFO]   parent-project
        [INFO]   core
        [INFO]   service
        [INFO]   webapp

