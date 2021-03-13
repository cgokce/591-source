#### Spring with Maven BOM

    https://www.baeldung.com/spring-maven-bom

Dependency Management Concepts
- Maven POM: XML file that contains information and configurations (about the project) used by Maven to import dependencies
- Maven BOM: (Bill of materials). Special kind of POM that is used to control versions of a project's dependencies and provide a central place to define and update versions
    - Provides the fexibility to add a dependency to our module without worrying about version we should depend on

Transitive Dependencies
- Maven can discover the libraries that are needed by our own dependencies in our pom.xml and includes them automatically
- Conflict happens when 2 dependencies refer to different versions of specific artifcat
- Closest one is used
    - A->B->C->D 1.4   and A->E->D 1.0
    - Since D 1.0 is close, it will be used
    - We can always guarantee the version by declaring explicity

Dependency Management
- Mechanism to centralize the dependency information
- When we have set of projects inherit a common parent, we can put all dependency information in a shared pom file called bom
    - Normal file with a dependencyManagement section

Using a BOM Files
- We can inherit the bom from parent using `<parent>` tag
- Or we can use dependency manager to import pom file

Overwriting BOM Dependency
- Order of predence
    - Version of the artifact's direct decleration in our project pom
    - Version of the artifact in the parent project
    - Version in the imported pom
    - Dependency meditation

Spring BOM
- We may find that a third party library might pull a dependency for older release, we can use bom dependency
- Then we do not specify the version attribute when we use the Spring artifacts