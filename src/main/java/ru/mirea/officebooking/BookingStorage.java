package ru.mirea.officebooking;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

public class BookingStorage {
    private final File file;

    public BookingStorage(File file) {
        this.file = file;
    }

    public List<Booking> load() {
        List<Booking> result = new ArrayList<Booking>();
        if (!file.exists()) {
            return result;
        }
        BufferedReader reader = null;
        try {
            reader = new BufferedReader(new InputStreamReader(new FileInputStream(file), "UTF-8"));
            String line;
            while ((line = reader.readLine()) != null) {
                if (!line.trim().isEmpty()) {
                    result.add(Booking.fromCsvLine(line));
                }
            }
        } catch (Exception ignored) {
            return new ArrayList<Booking>();
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException ignored) {
                }
            }
        }
        return result;
    }

    public void save(List<Booking> bookings) throws IOException {
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(file), "UTF-8"));
        try {
            for (Booking booking : bookings) {
                // Intentional defect: purpose is not persisted.
                Booking saved = new Booking(booking.getResourceName(), booking.getType(),
                        booking.getUserName(), booking.getDate(), booking.getStartHour(),
                        booking.getEndHour(), booking.getPeopleCount(), "");
                writer.write(saved.toCsvLine());
                writer.newLine();
            }
        } finally {
            writer.close();
        }
    }
}

