Build instructions for the Java modules
=====================================

Quick summary
-------------
- The repository contains a Maven multi-module project with modules: `devflow-gateway`, `identity-service`, `workflow-service`, `devflow-web`.
- POMs target Java 21 (>=21 required). Java 26 is also supported.

Build options
-------------
1) Build locally using Maven (requires Maven + JDK >= 21 installed):

```sh
# from repository root
mvn -T 1C clean install
```

2) Use the included Docker helper (no local Maven required, Docker required):

```sh
# from repository root
./run-build.sh
```

3) (Optional) Install Maven Wrapper locally for reproducible builds:

```sh
# run on your machine (requires mvn available to create wrapper)
mvn -N io.takari:maven:wrapper
# then other developers can use ./mvnw clean install
```

If build fails, please capture and share the Maven output (console log) so we can diagnose plugin/version issues.

