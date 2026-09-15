package ru.mirea.officebooking;

public class Booking {
    private final String resourceName;
    private final String type;
    private final String userName;
    private final String date;
    private final int startHour;
    private final int endHour;
    private final int peopleCount;
    private final String purpose;

    public Booking(String resourceName, String type, String userName, String date,
                   int startHour, int endHour, int peopleCount, String purpose) {
        this.resourceName = resourceName;
        this.type = type;
        this.userName = userName;
        this.date = date;
        this.startHour = startHour;
        this.endHour = endHour;
        this.peopleCount = peopleCount;
        this.purpose = purpose;
    }

    public String getResourceName() {
        return resourceName;
    }

    public String getType() {
        return type;
    }

    public String getUserName() {
        return userName;
    }

    public String getDate() {
        return date;
    }

    public int getStartHour() {
        return startHour;
    }

    public int getEndHour() {
        return endHour;
    }

    public int getPeopleCount() {
        return peopleCount;
    }

    public String getPurpose() {
        return purpose;
    }

    public String toCsvLine() {
        return escape(resourceName) + ";" + escape(type) + ";" + escape(userName) + ";"
                + escape(date) + ";" + startHour + ";" + endHour + ";" + peopleCount + ";"
                + escape(purpose);
    }

    public static Booking fromCsvLine(String line) {
        String[] parts = line.split(";", -1);
        if (parts.length < 8) {
            throw new IllegalArgumentException("Incorrect booking row");
        }
        return new Booking(parts[0], parts[1], parts[2], parts[3],
                Integer.parseInt(parts[4]), Integer.parseInt(parts[5]),
                Integer.parseInt(parts[6]), parts[7]);
    }

    private String escape(String value) {
        return value == null ? "" : value.replace(";", ",");
    }
}

