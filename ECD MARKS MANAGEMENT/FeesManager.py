from tkinter import *
from tkinter import ttk, messagebox, filedialog
import sqlite3
from datetime import datetime

class ClassFees:
    def __init__(self, root, ls, frame_old):
        self.ls = ls
        self.root = root
        self.frame_old = frame_old
        self.Roll_No_var = StringVar()
        self.fees_paid_var = IntVar()
        self.receipt_no_var = StringVar()  # Variable for receipt_no
        self.term_var = StringVar()  # Variable for new term
        self.number_work_var = StringVar()
        self.language_var = StringVar()
        self.environment_var = StringVar()
        self.psychomotor_var = StringVar()
        self.religious_var = StringVar()
        self.literacy_var = StringVar()

        # Initialize current term
        self.current_term = self.get_current_term()

        # Creating the main frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating a back button.
        exit_btn = Button(self.frame, text="Back", relief=RAISED, bg='#fbf8e6', command=self.exiting)
        exit_btn.place(x=10, y=10, width=100, height=40)
        
        # Labeling the title
        title = Label(self.frame, text='Manage Student Marks', font=('Algerian', 25, 'bold'), bg='lightgreen')
        title.pack(side=TOP, pady=10)

        # Display current term
        self.current_term = self.get_current_term()
        term_label = Label(self.frame, text=f"Current Term: {self.current_term}", font=("Arial", 14), bg='lightgreen')
        term_label.pack(side=TOP, pady=5)

        # Creating a frame for student list.
        Student_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg='LightBlue')
        Student_Frame.place(x=10, y=100, width=ls[0] - 20, height=ls[1] // 3)

        # Table for displaying student list.
        self.Student_table = ttk.Treeview(Student_Frame, columns=("Roll", "Name", "Class", "Number Work", "Language", "Environment", "Psychomotor", "Religious", "Literacy"))
        self.Student_table.heading("Roll", text="Roll No.")
        self.Student_table.heading("Name", text="Name")
        self.Student_table.heading("Class", text="Class")  # Added Class column
        self.Student_table.heading("Number Work", text="Number Work")
        self.Student_table.heading("Language", text="Language")
        self.Student_table.heading("Environment", text="Environment")
        self.Student_table.heading("Psychomotor", text="Psychomotor")
        self.Student_table.heading("Religious", text="Religious")
        self.Student_table.heading("Literacy", text="Literacy")
        self.Student_table['show'] = 'headings'
        self.Student_table.column("Roll", width=100)
        self.Student_table.column("Name", width=150)
        self.Student_table.column("Class", width=100)  # Column for class
        self.Student_table.column("Number Work", width=100)  # Adjust width as needed
        self.Student_table.column("Language", width=100)  # Adjust width as needed
        self.Student_table.column("Environment", width=100)  # Adjust width as needed
        self.Student_table.column("Psychomotor", width=100)  # Adjust width as needed
        self.Student_table.column("Religious", width=100)  # Adjust width as needed
        self.Student_table.column("Literacy", width=100)  # Adjust width as needed
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)


        # Creating a frame for fee management.
        Manage_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg="cornsilk")
        Manage_Frame.place(x=10, y=(ls[1] // 2) + 50, width=ls[0] - 20, height=(ls[1] // 4) + 50)

        # Label and Entry for Number work
        lbl_number_work = Label(Manage_Frame, text="Number work:", bg="cornsilk", fg="blue", font=("times new roman", 16, "bold"))
        lbl_number_work.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        txt_number_work = Entry(Manage_Frame, textvariable=self.number_work_var, font=("times new roman", 14), bd=5, relief=GROOVE)
        txt_number_work.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        # Label and Entry for Language
        lbl_language = Label(Manage_Frame, text="Language:", bg="cornsilk", fg="blue", font=("times new roman", 16, "bold"))
        lbl_language.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        txt_language = Entry(Manage_Frame, textvariable=self.language_var, font=("times new roman", 14), bd=5, relief=GROOVE)
        txt_language.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        # Label and Entry for Environment.
        lbl_environment = Label(Manage_Frame, text="Environment:", bg="cornsilk", fg="blue", font=("times new roman", 16, "bold"))
        lbl_environment.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        txt_environment = Entry(Manage_Frame, textvariable=self.environment_var, font=("times new roman", 14), bd=5, relief=GROOVE)
        txt_environment.grid(row=2, column=1, pady=10, padx=20, sticky="w")


        # Label and Entry for Psychomotor.
        lbl_psychomotor = Label(Manage_Frame, text="Psychomotor:", bg="cornsilk", fg="blue", font=("times new roman", 16, "bold"))
        lbl_psychomotor.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        txt_psychomotor = Entry(Manage_Frame, textvariable=self.psychomotor_var, font=("times new roman", 14), bd=5, relief=GROOVE)
        txt_psychomotor.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        # Label and Entry for Religious (move to row 0 and 1)
        lbl_religious = Label(Manage_Frame, text="Religious:", bg="cornsilk", fg="blue", font=("times new roman", 16, "bold"))
        lbl_religious.grid(row=0, column=2, padx=20, pady=10, sticky="w")

        txt_religious = Entry(Manage_Frame, textvariable=self.religious_var, font=("times new roman", 14), bd=5, relief=GROOVE)
        txt_religious.grid(row=0, column=3, pady=10, padx=20, sticky="w")

        # Label and Entry for Literacy (move to row 2 and 3)
        lbl_literacy = Label(Manage_Frame, text="Literacy:", bg="cornsilk", fg="blue", font=("times new roman", 16, "bold"))
        lbl_literacy.grid(row=1, column=2, padx=20, pady=10, sticky="w")

        txt_literacy = Entry(Manage_Frame, textvariable=self.literacy_var, font=("times new roman", 14), bd=5, relief=GROOVE)
        txt_literacy.grid(row=1, column=3, pady=10, padx=20, sticky="w")
        

        # Submit Payment Button
        submit_btn = Button(Manage_Frame, text="Add results", bg='black', fg='white', width=20, command=self.add_payment)
        submit_btn.grid(row=2, column=2, pady=10, padx=10, sticky="w")

        # View Payment History Button
        view_history_btn = Button(Manage_Frame, text="View results", bg='blue', fg='white', width=20, command=self.view_payment_history)
        view_history_btn.grid(row=2, column=3, pady=10, padx=10, sticky="w")

        # Print Payment History Button
        print_history_btn = Button(Manage_Frame, text="Print STUDENT RESULT SLIP", bg='green', fg='white', width=25, command=self.print_payment_history)
        print_history_btn.grid(row=3, column=2, pady=10, padx=10, sticky="w")

        # Print Fee Balances Button
        print_fee_balances_btn = Button(Manage_Frame, text="Print/Save Results", bg='orange', fg='white', width=25, command=self.print_fee_balances)
        print_fee_balances_btn.grid(row=3, column=3, pady=10, padx=10, sticky="w")

        # Label and Entry for new term
        lbl_term = Label(Manage_Frame, text="Enter New Term:", bg="cornsilk", fg="blue", font=("times new roman", 16, "bold"))
        lbl_term.grid(row=0, column=4, padx=20, pady=20, sticky="w")

        txt_term = Entry(Manage_Frame, textvariable=self.term_var, font=("times new roman", 14), bd=5, relief=GROOVE)
        txt_term.grid(row=0, column=5, pady=20, padx=20, sticky="w")

        # Set New Term Button
        set_term_btn = Button(Manage_Frame, text="Set New Term", bg='purple', fg='white', width=20, command=self.set_new_term)
        set_term_btn.grid(row=2, column=5, pady=10, padx=10, sticky="w")

        # Fetch and display students.
        self.fetch_students()

    def exiting(self):
        """Handle exiting the current frame and showing the previous one."""
        self.frame.destroy()
        self.frame_old.deiconify()

    def get_current_term(self):
        """Retrieve the current term from the database."""
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("SELECT term_name FROM current_term LIMIT 1")
        result = cur.fetchone()
        conn.close()
        if result:
            return result[0]
        else:
            return 'Term1'  # Default term if not set

    def fetch_students(self):
        """Fetch and display the list of students and their fees for the current term."""
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()

        # Dynamically generate the table name for the current term
        table_name = f"student_fees_{self.current_term.replace(' ', '_')}"
        print(f"Fetching data from table: {table_name}")  # Debugging line

        try:
            cur.execute(f"""
                SELECT sd.Roll_No, sd.Name, sd.email, 
                       IFNULL(sf.number_work, '') AS number_work,
                       IFNULL(sf.language, '') AS language,
                       IFNULL(sf.environment, '') AS environment,
                       IFNULL(sf.psychomotor, '') AS psychomotor,
                       IFNULL(sf.religious, '') AS religious,
                       IFNULL(sf.literacy, '') AS literacy,
                       IFNULL(sf.fees_paid, NULL) AS fees_paid, 
                       IFNULL(sf.fees_rem, NULL) AS fees_rem
                FROM student_data sd 
                LEFT JOIN {table_name} sf 
                     ON sd.Roll_No = sf.Roll_No
                ORDER BY sd.Name ASC
            """)
            rows = cur.fetchall()
            print("Fetched rows:", rows)  # Debugging line
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
        except Exception as e:
            print(f"Error fetching students: {e}")  # Error handling
        finally:
             conn.close()


    def get_cursor(self, ev):
        """Handle the event when a student is selected from the list."""
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        if row:
            self.Roll_No_var.set(row[0])

    def validate_marks(self, marks):
        """Validate the marks input to check if it follows the X/Y format."""
        try:
            # Split the marks by '/'
            parts = marks.split('/')
            if len(parts) != 2:
                return False
            
            # Convert both parts to integers
            obtained, total = int(parts[0]), int(parts[1])
            
            # Ensure obtained marks are not greater than total
            if obtained < 0 or total <= 0 or obtained > total:
                return False

            return True
        except ValueError:
            return False

    def add_payment(self):
        """Adds marks to the student database, both to the term table and payments history."""
        roll_no = self.Roll_No_var.get()
        number_work = self.number_work_var.get()
        language = self.language_var.get()
        environment = self.environment_var.get()
        psychomotor = self.psychomotor_var.get()
        religious = self.religious_var.get()
        literacy = self.literacy_var.get()
        term = self.current_term

        # Save to the term-specific table
        table_name = f"student_fees_{term.replace(' ', '_')}"
        try:
            conn = sqlite3.connect('employee.db')
            cur = conn.cursor()

            # Insert or update the marks in the term table
            cur.execute(f"""
                INSERT INTO {table_name} (Roll_No, number_work, language, environment, psychomotor, religious, literacy)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(Roll_No) DO UPDATE SET
                    number_work = excluded.number_work,
                    language = excluded.language,
                    environment = excluded.environment,
                    psychomotor = excluded.psychomotor,
                    religious = excluded.religious,
                    literacy = excluded.literacy
            """, (roll_no, number_work, language, environment, psychomotor, religious, literacy))

            # Insert to payments table for history
            cur.execute("""
                INSERT INTO payments (Roll_No, term, number_work, language, environment, psychomotor, religious, literacy, payment_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (roll_no, term, number_work, language, environment, psychomotor, religious, literacy, datetime.now()))

            conn.commit()
            messagebox.showinfo("Success", "Marks added successfully.")
        except Exception as e:
            messagebox.showerror("Database Error", f"Error occurred: {e}")
            print(f"Error adding payment: {e}")  # Debugging print statement
        finally:
            conn.close()
            self.fetch_students()  # Refresh student list with updated marks

    def reset_fields(self):
        """Reset the input fields after recording payment."""
        self.fees_paid_var.set(0)
        self.receipt_no_var.set('')
        self.Roll_No_var.set('')
        self.number_work_var.set('')  # Reset number_work field
        self.language_var.set('')  # Reset language field
        self.environment_var.set('')  # Reset environment field
        self.psychomotor_var.set('')  # Reset psychomotor field
        self.religious_var.set('')  # Reset religious field
        self.literacy_var.set('')

    def view_payment_history(self):
        """View the payment history of the selected student."""
        if not self.Roll_No_var.get():
            messagebox.showerror("Error", "Please select a student to view results history.")
            return

        roll_no = self.Roll_No_var.get()
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
    
        # Modify the query to exclude Receipt No and Amount
        cur.execute("""
            SELECT number_work, language, 
                   environment, psychomotor, 
                   religious, literacy,
                   payment_date, term
            FROM payments 
            WHERE Roll_No = ? 
            ORDER BY payment_date DESC
        """, (roll_no,))
        history = cur.fetchall()
        conn.close()

        # Create a new window to display payment history
        history_window = Toplevel(self.root)
        history_window.title(f"Results History for {roll_no}")
        history_window.geometry("500x400")  # Adjusted for fewer columns

        # Define the Treeview with the updated columns
        history_tree = ttk.Treeview(history_window, columns=("Number Work", 
                                                               "Language", 
                                                               "Environment", 
                                                               "Psychomotor", 
                                                               "Religious", 
                                                               "Literacy", 
                                                               "Date", 
                                                               "Term"))
        # Set headings for all columns
        history_tree.heading("Number Work", text="Number Work")
        history_tree.heading("Language", text="Language")
        history_tree.heading("Environment", text="Environment")
        history_tree.heading("Psychomotor", text="Psychomotor")
        history_tree.heading("Religious", text="Religious")
        history_tree.heading("Literacy", text="Literacy")
        history_tree.heading("Date", text="Date")
        history_tree.heading("Term", text="Term")

        history_tree['show'] = 'headings'  # Show only the headings
        # Set column widths
        history_tree.column("Number Work", width=100)
        history_tree.column("Language", width=100)
        history_tree.column("Environment", width=100)
        history_tree.column("Psychomotor", width=100)
        history_tree.column("Religious", width=100)
        history_tree.column("Literacy", width=100)
        history_tree.column("Date", width=150)
        history_tree.column("Term", width=100)

        history_tree.pack(fill=BOTH, expand=1)

        # Insert each row of the payment history into the Treeview
        for row in history:
            history_tree.insert('', END, values=row)

    def print_payment_history(self):
        """Print the result slip for the selected student."""
        if not self.Roll_No_var.get():
            messagebox.showerror("Error", "Please select a student to print Results Slip.")
            return

        roll_no = self.Roll_No_var.get()
        current_term = self.get_current_term()  # Replace with dynamic term if needed

        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
    
        # Fetch the student's name and class using the roll number
        cur.execute("SELECT Name, email FROM student_data WHERE Roll_No = ?", (roll_no,))
        student_data = cur.fetchone()
        if student_data:
            student_name, student_class = student_data
        else:
             messagebox.showerror("Error", "Student name not found.")
             return

        # Fetch the subject marks from the term-specific table
        cur.execute(f"""
            SELECT number_work, language, environment, psychomotor, religious, literacy 
            FROM student_fees_{self.current_term.replace(' ', '_')} 
            WHERE Roll_No = ?
        """, (roll_no,))
        subject_marks = cur.fetchone()

        conn.close()

        # Ask for the file path to save the result slip
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                # Heading
                file.write("RESULT SLIP\n")
                file.write("MATENDENI PRE-SCHOOL\n")
                file.write("P.O BOX 205\n")
                file.write("EMBU\n\n")
            
                # Student Details
                file.write(f"{'Name:':<15} {student_name}\n")
                file.write(f"{'Term:':<15} {current_term}\n")
                file.write(f"{'Class:':<15} {student_class}\n\n")

                # Subjects and Marks
                file.write(f"{'SUBJECT':<20} {'RUBRICS':<10} {'KEY':<30}\n")
                file.write("=" * 30 + "\n")

                if subject_marks:
                    number_work, language, environment, psychomotor, religious, literacy = subject_marks

                    # Function to extract the numeric part of the marks and the total
                    def extract_numeric(mark):
                        if mark is not None:
                            return int(mark.split('/')[0]), int(mark.split('/')[1])  # Return both scored and total
                        return 0, 0  # If None, return (0, 0)

                    # Initialize totals
                    total_scored = 0
                    total_possible = 0

                    subjects = ["Number Work", "Language", "Environment", "Psychomotor", "Religious", "Literacy"]
                    for subject, mark in zip(subjects, subject_marks):
                        scored, possible = extract_numeric(mark)
                        total_scored += scored
                        total_possible += possible
                        file.write(f"{subject:<20} {mark if mark is not None else 'N/A':<10}\n")
                    # Display total marks at the end
                    file.write("="*30 + "\n")
                    file.write(f"{'TOTAL MARKS':<20} {total_scored}/{total_possible:<10}\n")
                    # Add KEY section
                    file.write("="*30 + "\n")
                    file.write(f"{'KEY':<20}\n")
                    file.write("="*30 + "\n")
                    file.write(f"{'4 - Exceeds Expectations':<30}\n")
                    file.write(f"{'3 - Meets Expectations':<30}\n")
                    file.write(f"{'2 - Approaches Expectations':<30}\n")
                    file.write(f"{'1 - Below Expectations':<30}\n")
                    file.write("="*30 + "\n")
                    file.write(f"{'Conduct':<30}\n")
                    file.write(f"{'TR. REMARKS:':<30} {'-' * 40}\n")
                    file.write(f"{'FEES BALANCE:':<30} {'-' * 40}\n")
                    file.write(f"{'Opening date:':<30} {'_' * 15} - {'Closing date:':<15} {'_' * 15}\n")
                    file.write(f"{'ACCOUNT NO: 01129407576700':<30}\n")
                else:
                     file.write("No subject marks available.\n")

        messagebox.showinfo("Success", "Result slip saved successfully!")

    def print_fee_balances(self): 
        """Print or save the subject marks of all students with fees remaining greater than 1, arranged by class."""
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()

        # Dynamically generate the table name for the current term
        term_table = f"student_fees_{self.current_term.replace(' ', '_')}"

        # Fetch students with fees remaining greater than 1, including their class and subject marks
        cur.execute(f"""
            SELECT sd.Roll_No, sd.Name, sd.email, 
                   sf.number_work, sf.language, sf.environment, sf.psychomotor, sf.religious, sf.literacy
            FROM student_data sd 
            LEFT JOIN {term_table} sf ON sd.Roll_No = sf.Roll_No
            WHERE sf.fees_rem > 1
            ORDER BY sd.email ASC, sd.Name ASC
        """)
        balances = cur.fetchall()
        conn.close()

        # Ask for the file path to save the subject marks
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write("MATENDENI E.C.D\n")
                file.write("P.O BOX 205\n")
                file.write("EMBU\n\n")
                file.write(f"{'Roll No':<20} {'Name':<35} {'Class':<20} {'Number Work':<10} {'Language':<10} {'Environment':<10} {'Psychomotor':<10} {'Religious':<10} {'Literacy':<10}\n")
                file.write("=" * 150 + "\n")

                for row in balances:
                    # Format each subject mark properly
                    number_work = f"{row[3]}" if row[3] is not None else "N/A"
                    language = f"{row[4]}" if row[4] is not None else "N/A"
                    environment = f"{row[5]}" if row[5] is not None else "N/A"
                    psychomotor = f"{row[6]}" if row[6] is not None else "N/A"
                    religious = f"{row[7]}" if row[7] is not None else "N/A"
                    literacy = f"{row[8]}" if row[8] is not None else "N/A"
                    
                    file.write(f"{row[0]:<20} {row[1]:<35} {row[2]:<20} {number_work:<15} {language:<15} {environment:<15} {psychomotor:<15} {religious:<15} {literacy:<15}\n")
                
        messagebox.showinfo("Success", "Student marks saved successfully!")

    def set_new_term(self):
        """Set up a new term, carrying over balances for students with remaining fees."""
        new_term = self.term_var.get()

        if not new_term:
            messagebox.showerror("Error", "Please enter a term name.")
            return

        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()

        # Define table names for current and new terms
        current_term_table = f"student_fees_{self.current_term.replace(' ', '_')}"
        new_term_table = f"student_fees_{new_term.replace(' ', '_')}"

        try:
            # Step 1: Create a new table for the new term with additional subject columns
            cur.execute(f"""
                CREATE TABLE IF NOT EXISTS {new_term_table} (
                    Roll_No TEXT PRIMARY KEY,
                    fees_paid INTEGER DEFAULT 0,
                    fees_rem INTEGER DEFAULT 3500,
                    number_work TEXT DEFAULT NULL,
                    language TEXT DEFAULT NULL,
                    environment TEXT DEFAULT NULL,
                    psychomotor TEXT DEFAULT NULL,
                    religious TEXT DEFAULT NULL,
                    literacy TEXT DEFAULT NULL
                )
            """)
    
            # Step 2: Carry forward remaining balances from the current term
            cur.execute(f"""
                INSERT OR REPLACE INTO {new_term_table} (Roll_No, fees_paid, fees_rem, number_work, language, environment, psychomotor, religious, literacy)
                SELECT Roll_No, 0, fees_rem + 3500, NULL, NULL, NULL, NULL, NULL, NULL
                FROM {current_term_table}
            """)

            # Update the current term in the system
            self.current_term = new_term
            cur.execute("UPDATE current_term SET term_name = ? WHERE rowid = 1", (new_term,))
            conn.commit()

            messagebox.showinfo("Success", f"New term '{new_term}' set successfully!")
            self.fetch_students()  # Refresh the displayed list of students for the new term

        except Exception as e:
            messagebox.showerror("Error", f"Failed to set new term: {e}")
        finally:
             conn.close()

        # Update the current term display
        self.current_term = new_term
        messagebox.showinfo("Success", f"New term '{new_term}' created successfully!")
        self.fetch_students()  # Refresh the student list
        self.reset_fields()  # Reset input fields


    def exiting(self):
        """Handle the action when the 'Back' button is clicked."""
        self.frame.destroy()
        self.frame_old.pack()

def login(root, ls):
    frame = Frame(root, bg='#163148')
    frame.place(x=0, y=0, width=ls[0], height=ls[1])

    Label(frame, text="Login", font=("Arial", 24), bg='#163148', fg='white').pack(pady=50)

    username_var = StringVar()
    password_var = StringVar()

    Label(frame, text="Username:", font=("Arial", 14), bg='#163148', fg='white').pack(pady=10)
    Entry(frame, textvariable=username_var, font=("Arial", 14)).pack(pady=10)

    Label(frame, text="Password:", font=("Arial", 14), bg='#163148', fg='white').pack(pady=10)
    Entry(frame, textvariable=password_var, font=("Arial", 14), show="*").pack(pady=10)

    def attempt_login():
        # In a real application, replace this with actual login validation
        if username_var.get() == "admin" and password_var.get() == "password":
            frame.destroy()
            ClassFees(root, ls, frame)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    Button(frame, text="Login", font=("Arial", 14), command=attempt_login).pack(pady=20)

if __name__ == "__main__":
    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f"{width}x{height}")
    root.title("Marks Management System")

    login(root, (width, height))

    root.mainloop()
