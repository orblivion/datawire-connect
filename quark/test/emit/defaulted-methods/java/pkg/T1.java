package pkg;

public class T1 implements A {
    public void foo() {
        System.out.println("T1 foo");
    }
    public void bar() {
        System.out.println("A bar");
        (this).foo();
    }
}