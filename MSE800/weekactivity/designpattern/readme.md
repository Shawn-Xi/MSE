## Week 7 Activity 1: Factory Design Pattern Analysis

Explain how the Factory Design Pattern is used in the sample code as follows. Is there any class and subclass in the sample code? Explain the outcome of the implementation.  Share your GitHub link with a readme file.
---

### 1. How is the Factory Design Pattern used in the sample code?

The Factory Design Pattern is used to decouple the client (the code that needs an object) from the concrete classes that are being instantiated. In this project, it works as follows:

*   **Abstract Factory (`Factory`)**: An abstract base class that defines a standard interface for creating objects (a method called `create_product`).
*   **Concrete Factory (`AnimalFactory`)**: This class inherits from `Factory` and provides the actual implementation. Its `create_product` method contains the core logic. It takes a `kind` string as input and decides which specific animal class (`Dog` or `Cat`) to create.
*   **Client Code**: The client no longer needs to know the specific class names of the animals. Instead of calling `Dog()` directly, it asks the `AnimalFactory` to create an animal of a certain `kind`.

---

### 2. Are there classes and subclasses in the sample code?

abstract class: Factory
subclass: AnimalFactory

abstract class: Product
subclass: Dog, Cat

---

### 3. What is the outcome of the implementation?


The final outcome is that the program prints the following message to the console:

```
dog is running
```

This successfully demonstrates that the client was able to create and use a `Dog` object without ever referencing the `Dog` class directly.


1.  An instance of `AnimalFactory` is created.
2.  This factory is asked to create a product of `kind="dog"`.
3.  The factory's internal logic instantiates and returns a `Dog` object.
4.  The `run()` method is called on this newly created `Dog` object.

