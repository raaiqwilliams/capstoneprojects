import java.sql.*;
import java.util.Scanner;

public class Bookstore {
    // Establishing variables to be passed to SQL functions
    private static int bookID, bookQty;
    private static String bookTitle, bookAuthor;

    public static void main(String[] args) {
        // Scanner object and printmenu function
        Scanner scan = new Scanner(System.in);
        printMenu();

        // Read user input
        int choice = scan.nextInt();

        // Switch-case to evaluate user's choice and perform appropiate function
        while (choice != 0) {
            switch (choice) {
            // Insert a new book
            case 1:
                bookInsert(scan);
                break;
            // Update a record
            case 2:
                bookUpdate(scan);
                break;
            // Delete a record with confirmation
            case 3:
                char confirm = bookDelete(scan).charAt(0);
                if (confirm == 'y') {
                    Delete(bookID);
                    break;
                } else if (confirm != 'y') {
                    System.out.println("Deletion cancelled! Returning to main menu...");
                    break;
                }
                // Search for a book
            case 4:
                System.out.println("Search books.");
                System.out.print("Please enter the id of the book you would like to find: ");
                bookID = scan.nextInt();
                Search(bookID);
                break;
            }
            // Print menu and allow input until 0 is entered to break while loop
            printMenu();
            choice = scan.nextInt();
        }
        // Closing resource and print closing statement
        System.out.println("Thank you for using Ebookstore!");
        scan.close();
    }

    // Function to display output if user selects option 1
    private static String bookDelete(Scanner scan) {
        printLine();
        System.out.println("3. Delete a book.");
        printLine();
        System.out.print("Enter ID of the book you would like to remove: ");
        bookID = scan.nextInt();
        System.out.println("Are you sure you want to remove book with id " + bookID + "? (Y/N)");
        String confirm = scan.next().toLowerCase();
        return confirm;
    }

    // Function to display output for option 2
    private static void bookUpdate(Scanner scan) {
        printLine();
        System.out.println("2. Update a book.");
        printLine();
        System.out.print("Enter book ID you would like to update: ");
        bookID = scan.nextInt();
        // Allows user to update a specific field in a record
        System.out.println("Which field would you like to update? (Title/Author/Qty)");
        String updateString = scan.next();
        // Requests updated value
        System.out.print("Enter updated value for field " + updateString.toLowerCase() + ": ");
        String updateValue = scan.next();
        // Calling function Update
        Update(bookID, updateString, updateValue);
    }

    // Function to display output for option 1
    private static void bookInsert(Scanner scan) {
        printLine();
        System.out.println("1. Enter a new book.");
        printLine();
        System.out.print("Enter book ID: ");
        bookID = scan.nextInt();
        System.out.print("\nEnter book title: ");
        bookTitle = scan.next();
        System.out.print("\nEnter book author: ");
        bookAuthor = scan.next();
        System.out.print("\nEnter book quantity: ");
        bookQty = scan.nextInt();
        Insert(bookID, bookTitle, bookAuthor, bookQty);
    }

    // Print main menu function
    private static void printMenu() {
        System.out.println("WELCOME TO EBOOKSTORE SQL CLIENT");
        printLine();
        System.out
                .print("1. Enter book\n" + "2. Update book\n" + "3. Delete book\n" + "4. Search books\n" + "0. Exit\n");
        printLine();
    }

    // Printing line function to improve readability
    private static void printLine() {
        System.out.println("---------------");
    }

    /* SQL FUNCTIONS INSERT, UPDATE, DELETE AND SEARCH */

    public static void Insert(int bookID, String bookTitle, String bookAuthor, int bookQty) {
        // Try-catch to establish connection and prepare statement.
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/ebookstore", "myuser",
                "xxxx"); Statement stmt = conn.createStatement();) {
            // Concatenation of sqlInsert to be pushed as an SQL query
            String sqlInsert = "insert into books " + "values (" + bookID + "," + bookTitle + "," + bookAuthor + ","
                    + bookQty + ")";
            System.out.println("The SQL query is: " + sqlInsert);
            // Count number of entries
            int countInserted = stmt.executeUpdate(sqlInsert);
            System.out.println(countInserted + " records inserted.\n");
            // Display all records including new addition
            String strSelect = "select * from books";
            System.out.println("The SQL query is: " + strSelect);
            // Retrieving table
            ResultSet rset = stmt.executeQuery(strSelect);
            while (rset.next()) {
                System.out.println(rset.getInt("id") + ", " + rset.getString("author") + ", " + rset.getString("title")
                        + ", " + rset.getInt("qty"));
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
    }

    // Update function is similar to Insert
    public static void Update(int bookID, String updateString, String updateValue) {
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/ebookstore", "myuser",
                "xxxx"); Statement stmt = conn.createStatement();) {
            // Concatenating strUpdate and using user values to determine field to be
            // updated along with new value
            String strUpdate = "update books set " + updateString + " = " + updateValue + " where id = " + bookID;
            System.out.println("The SQL query is: " + strUpdate);

            // Counting number of records affected
            int countUpdated = stmt.executeUpdate(strUpdate);
            System.out.println(countUpdated + " records affected.");
            // Retrieving updated list
            String strSelect = "select * from books where id = " + bookID;
            System.out.println("The SQL query is: " + strSelect);
            ResultSet rset = stmt.executeQuery(strSelect);
            while (rset.next()) {
                System.out.println(rset.getInt("id") + ", " + rset.getString("author") + ", " + rset.getString("title")
                        + ", " + rset.getInt("qty"));
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
    }

    // For the Delete function, I used a PreparedStatement and took the bookID
    // variable as a parameter
    public static void Delete(int bookID) {
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/ebookstore", "myuser",
                "xxxx"); PreparedStatement stmt = conn.prepareStatement("delete from books where id=?");) {
            // BookID is parameter for preparedstatement
            stmt.setInt(1, bookID);
            // Count deleted
            int countDeleted = stmt.executeUpdate();
            System.out.println(countDeleted + " record(s) deleted.");
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
    }

    // The search function only allows for selection using bookID
    public static void Search(int bookID) {
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/ebookstore", "myuser",
                "xxxx"); PreparedStatement stmt = conn.prepareStatement("select * from books where id=?");) {
            // Again I used preparedstatement with user supplied bookID as parameter
            stmt.setInt(1, bookID);
            // ResultSet to return the select query results
            ResultSet rset = stmt.executeQuery();
            while (rset.next()) {
                String title = rset.getString("title");
                String author = rset.getString("author");
                int qty = rset.getInt("qty");
                System.out.println("Book title: " + title + "\nBook author: " + author + "\nBook quantity: " + qty);
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
    }
}