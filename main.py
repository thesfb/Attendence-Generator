from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.checkbox import CheckBox
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime


class AttendanceApp(MDApp):
    def build(self):
        return Builder.load_file("main.kv")

    def on_start(self):
        self.students = self.load_students_from_csv()
        self.load_students()

    def load_students_from_csv(self, csv_file=[STUDENT CSV FILE]):# Pass a csv file eg. data.csv
        students = []
        try:
            with open(csv_file, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file, fieldnames=["roll_no", "name", "attendance"])  
                for row in reader:
                    
                    row['attendance'] = False
                    students.append(row)
        except FileNotFoundError:
            print(f"CSV file '{csv_file}' not found.")
        except csv.Error as e:
            print(f"CSV file error: {e}")
        except Exception as e:
            print(f"Error reading CSV file: {e}")

        return students

    def load_students(self):
        student_grid = self.root.ids.student_grid
        student_grid.clear_widgets()

        for student in self.students:
            student_grid.add_widget(MDLabel(text=student['roll_no'], font_size="16sp", halign="center"))
            student_grid.add_widget(MDLabel(text=student['name'], font_size="16sp", halign="center"))
            toggle_button = MDRaisedButton(
                text='Present' if student['attendance'] else 'Mark Present',
                font_size="16sp",
                on_press=lambda btn, stu=student: self.toggle_attendance(btn, stu)
            )
            student_grid.add_widget(toggle_button)

    def toggle_attendance(self, button, student):
        student['attendance'] = not student['attendance']
        button.text = 'Present' if student['attendance'] else 'Mark Present'

    def clear_attendance(self):
        for student in self.students:
            student['attendance'] = False
        self.load_students()

    def make_attendance(self):
        for student in self.students:
            student['attendance'] = True
        self.load_students()

    def generate_pdf(self):
        present_students = [student for student in self.students if student['attendance']]
        time = datetime.now().strftime("%H.%M.%S")
        pdf_filename = f"attendance {time}.pdf"

        if present_students:
            pdf = canvas.Canvas(pdf_filename, pagesize=letter)
            pdf.setFont("Helvetica", 16)
            pdf.drawString(100, 800, 'Attendance Report')

            y_position = 780
            for student in present_students:
                y_position -= 30
                pdf.drawString(100, y_position, f"Roll No: {student['roll_no']}, Name: {student['name']}")

                # Check if the y_position goes below the margin
                if y_position < 100:
                    pdf.showPage()  # Start a new page
                    y_position = 780  # Reset y_position for the new page
                    pdf.drawString(100, 800, 'Attendance Report')  # Redraw the header  

            pdf.save()

            self.show_popup(f'Attendance PDF generated: {pdf_filename}')
        else:
            self.show_popup('No students marked as present. Generate attendance first.')

    def show_popup(self, text):
        dialog = MDDialog(
            title="Notification",
            text=text,
            size_hint=(0.8, 0.2),
            buttons=[
                MDRaisedButton(text="OK", on_release=lambda x: self.close_popup(dialog))
            ]
        )
        dialog.open()

    def close_popup(self, dialog):
        dialog.dismiss()


if __name__ == '__main__':
    AttendanceApp().run()
