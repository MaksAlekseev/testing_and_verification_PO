package ru.mirea.officebooking;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;
import javax.swing.table.DefaultTableModel;
import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.io.File;
import java.util.Arrays;

public class OfficeBookingApp extends JFrame {
    private final BookingStorage storage = new BookingStorage(new File("bookings.csv"));
    private final BookingService service;
    private final DefaultTableModel tableModel;
    private final JComboBox<String> resourceCombo;
    private final JTextField userField = new JTextField();
    private final JTextField dateField = new JTextField("2026-09-16");
    private final JTextField startField = new JTextField("9");
    private final JTextField endField = new JTextField("10");
    private final JTextField peopleField = new JTextField("1");
    private final JTextField purposeField = new JTextField();
    private final JTable table;

    public OfficeBookingApp() {
        super("Office Booking");
        service = new BookingService(Arrays.asList(
                new Resource("Переговорная A", "Переговорная", 6),
                new Resource("Переговорная B", "Переговорная", 10),
                new Resource("Кабинет фокусной работы", "Переговорная", 2),
                new Resource("Рабочее место 1", "Рабочее место", 1),
                new Resource("Рабочее место 2", "Рабочее место", 1)
        ), storage.load());

        resourceCombo = new JComboBox<String>();
        for (Resource resource : service.getResources()) {
            resourceCombo.addItem(resource.getName());
        }

        tableModel = new DefaultTableModel(new Object[]{
                "Ресурс", "Тип", "Сотрудник", "Дата", "Начало", "Конец", "Людей", "Цель"
        }, 0);
        table = new JTable(tableModel);

        setLayout(new BorderLayout(8, 8));
        add(createForm(), BorderLayout.NORTH);
        add(new JScrollPane(table), BorderLayout.CENTER);
        add(createButtons(), BorderLayout.SOUTH);

        refreshTable();
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(980, 520);
        setLocationRelativeTo(null);
    }

    private JPanel createForm() {
        JPanel panel = new JPanel(new GridLayout(4, 4, 8, 6));
        panel.add(new JLabel("Ресурс"));
        panel.add(resourceCombo);
        panel.add(new JLabel("Сотрудник"));
        panel.add(userField);
        panel.add(new JLabel("Дата"));
        panel.add(dateField);
        panel.add(new JLabel("Начало, час"));
        panel.add(startField);
        panel.add(new JLabel("Конец, час"));
        panel.add(endField);
        panel.add(new JLabel("Количество людей"));
        panel.add(peopleField);
        panel.add(new JLabel("Цель"));
        panel.add(purposeField);
        return panel;
    }

    private JPanel createButtons() {
        JPanel panel = new JPanel();
        JButton bookButton = new JButton("Забронировать");
        JButton cancelButton = new JButton("Отменить выбранную бронь");
        JButton saveButton = new JButton("Сохранить");

        bookButton.addActionListener(e -> createBooking());
        cancelButton.addActionListener(e -> cancelBooking());
        saveButton.addActionListener(e -> saveBookings());

        panel.add(bookButton);
        panel.add(cancelButton);
        panel.add(saveButton);
        return panel;
    }

    private void createBooking() {
        try {
            service.createBooking(
                    String.valueOf(resourceCombo.getSelectedItem()),
                    userField.getText(),
                    dateField.getText(),
                    Integer.parseInt(startField.getText()),
                    Integer.parseInt(endField.getText()),
                    Integer.parseInt(peopleField.getText()),
                    purposeField.getText()
            );
            refreshTable();
            JOptionPane.showMessageDialog(this, "Бронь добавлена");
        } catch (Exception exception) {
            JOptionPane.showMessageDialog(this, exception.getMessage(), "Ошибка", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void cancelBooking() {
        try {
            service.cancelBooking(table.getSelectedRow());
            refreshTable();
        } catch (Exception exception) {
            JOptionPane.showMessageDialog(this, exception.getMessage(), "Ошибка", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void saveBookings() {
        try {
            storage.save(service.getBookings());
            JOptionPane.showMessageDialog(this, "Брони сохранены в bookings.csv");
        } catch (Exception exception) {
            JOptionPane.showMessageDialog(this, exception.getMessage(), "Ошибка", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void refreshTable() {
        tableModel.setRowCount(0);
        for (Booking booking : service.getBookings()) {
            tableModel.addRow(new Object[]{
                    booking.getResourceName(), booking.getType(), booking.getUserName(),
                    booking.getDate(), booking.getStartHour(), booking.getEndHour(),
                    booking.getPeopleCount(), booking.getPurpose()
            });
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new OfficeBookingApp().setVisible(true);
            }
        });
    }
}

