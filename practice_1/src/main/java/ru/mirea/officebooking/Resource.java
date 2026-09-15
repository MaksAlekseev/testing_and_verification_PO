package ru.mirea.officebooking;

public class Resource {
    private final String name;
    private final String type;
    private final int capacity;

    public Resource(String name, String type, int capacity) {
        this.name = name;
        this.type = type;
        this.capacity = capacity;
    }

    public String getName() {
        return name;
    }

    public String getType() {
        return type;
    }

    public int getCapacity() {
        return capacity;
    }
}

