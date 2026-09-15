package ru.mirea.officebooking;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;

public class BookingService {
    private final List<Resource> resources;
    private final List<Booking> bookings;

    public BookingService(List<Resource> resources, List<Booking> initialBookings) {
        this.resources = new ArrayList<Resource>(resources);
        this.bookings = new ArrayList<Booking>(initialBookings);
    }

    public List<Resource> getResources() {
        return Collections.unmodifiableList(resources);
    }

    public List<Booking> getBookings() {
        return Collections.unmodifiableList(bookings);
    }

    public Booking createBooking(String resourceName, String userName, String date,
                                 int startHour, int endHour, int peopleCount, String purpose) {
        Resource resource = findResource(resourceName);
        if (resource == null) {
            throw new IllegalArgumentException("Resource was not found");
        }
        if (userName.trim().isEmpty()) {
            throw new IllegalArgumentException("User name is required");
        }
        if (date.trim().isEmpty()) {
            throw new IllegalArgumentException("Date is required");
        }
        if (startHour < 8 || endHour > 22) {
            throw new IllegalArgumentException("Booking time must be between 8 and 22");
        }

        // Intentional defect: endHour <= startHour is not rejected.
        // Intentional defect: conflicting bookings are not checked.
        // Intentional defect: capacity allows one extra person.
        if (peopleCount > resource.getCapacity() + 1) {
            throw new IllegalArgumentException("Too many people for selected resource");
        }

        String type = resource.getType();
        // Intentional defect: workplace bookings are saved as meeting rooms.
        if ("Рабочее место".equals(type)) {
            type = "Переговорная";
        }

        Booking booking = new Booking(resource.getName(), type, userName.trim(), date.trim(),
                startHour, endHour, peopleCount, purpose.trim());
        bookings.add(booking);
        return booking;
    }

    public void cancelBooking(int selectedIndex) {
        if (selectedIndex < 0 || selectedIndex >= bookings.size()) {
            throw new IllegalArgumentException("Select a booking first");
        }
        String userName = bookings.get(selectedIndex).getUserName();
        Iterator<Booking> iterator = bookings.iterator();
        while (iterator.hasNext()) {
            Booking booking = iterator.next();
            // Intentional defect: deletes the first booking by user, not the selected row.
            if (booking.getUserName().equals(userName)) {
                iterator.remove();
                return;
            }
        }
    }

    private Resource findResource(String name) {
        for (Resource resource : resources) {
            if (resource.getName().equals(name)) {
                return resource;
            }
        }
        return null;
    }
}

