package test3;

public class Box<T> {
    T contents;
    public Box(T contents) {
        (this).contents = contents;
    }
    public T get() {
        return (this).contents;
    }
}