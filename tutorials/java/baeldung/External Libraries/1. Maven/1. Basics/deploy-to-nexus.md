#### Maven Release to Nexus

    https://www.baeldung.com/maven-release-nexus

- Sonatype is maintainer of Maven Central Repo, which is instance of Nexus
        
        https://stackoverflow.com/questions/23082621/what-is-the-difference-between-nexus-and-maven

Release Process with Maven
- Define the repo information 

        <distributionManagement><repositroy>
            <id>nexus-releases</id>
            <url>http.../nexus/repositories/releases</url>
        ...
- Define the Scm element in the pom

        <scm>
            <connection>scm:git:github.com/user.project.git</connection>
            <url>...</url>
            <developerConnection>...</developerConnection>
        </scm>
- Add the maven release plugin
- Add the nexus-staging-maven-plugin to deploy nexus-releases to Nexus repo
- In the maven settings file, update Nexus server settings via servers.server tag

Release Steps
- release:clean: delete the desctipyor and any backup POMs
- release:prepeare: perform checks, run the test suites, commit and push, increase the version of project, commit and push
- release:perform: checkout release tag from SCM, build and deploy released code

Release with Jenkins
- Can use its own plugin or with maven plugin, release:Clean, release:prepare, release:Perform

#### Maven Deploy to Nexus

    https://www.baeldung.com/maven-deploy-nexus

Deploy Projets to Nexus with Maven
- Add distributionManagement tag including snapshotw to the maven
- Maven-deploy-plugin can be used to handle deploying artifacts
    - Nexus has nexus-staging-maven-plugin that also supports staging etc, add both 
- Add nexus snapshot server in the maven settings, to make sure maven can connect nexus securely
- Then use `mvn clean deploy` to start deployment, can also used in Jenkins stage