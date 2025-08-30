


# Hello Java Maven – Jenkins CI/CD Task

This repository contains a simple Java project built with Maven, used to demonstrate a **Jenkins Freestyle Job** build for Task 8 of the DevOps tasks.

---

## **HelloWorld.java**

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, Jenkins + Maven!");
    }
}
````

---

## **pom.xml Highlights**

* Java 1.8 compatibility
* Maven Compiler Plugin
* Maven Jar Plugin configured with `Main-Class` to make the JAR executable

---

## **Build Instructions**

### **Locally**

1. Navigate to project root:

```bash
cd hello-java-maven
```

2. Build with Maven:

```bash
mvn clean package
```

3. Run the generated JAR:

```bash
java -jar target/hello-1.0.jar
```

### **Jenkins**

1. Create a **Freestyle Project** in Jenkins.
2. Configure **Maven build step**:

   * Root POM: `hello-java-maven/pom.xml`
   * Goals: `clean package`
3. Build the project.
4. Verify console output shows:

```
[INFO] BUILD SUCCESS
```

5. (Optional) Archive artifacts:

```
target/*.jar
```

---

## **Deliverables**

* Java Maven project
* Jenkins Freestyle Job build configuration
* Screenshot of successful build in `screenshots/`
* Executable JAR: `target/hello-1.0.jar`

---

## **Output**

```
Hello, Jenkins + Maven!
```

when running the JAR file.

---

 

