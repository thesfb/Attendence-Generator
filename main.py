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

    def load_students_from_csv(self, csv_file='csse.csv'):
        students = [{'roll_no': 'R23EK046', 'name': 'TANISHA JAVALKAR', 'attendance': False}, {'roll_no': 'R23EK041', 'name': 'SIMRAH SUHANA', 'attendance': False}, {'roll_no': 'R23EK060', 'name': 'VANGALA MANASA REDDY', 'attendance': False}, {'roll_no': 'R23EK049', 'name': 'UMAIZA FATHIMA', 'attendance': False}, {'roll_no': 'R23EK007', 'name': 'BHOOMIKA M S', 'attendance': False}, {'roll_no': 'R23EK003', 'name': 'ALLURISRIVARSHA SRIVARSHA', 'attendance': False}, {'roll_no': 'R23EK013', 'name': 'KEERTANA  S', 'attendance': False}, {'roll_no': 'R23EK047', 'name': 'Taqia Aiman', 'attendance': False}, {'roll_no': 'R23EK042', 'name': 'SUDHANSHU BHARDWAJ', 'attendance': False}, {'roll_no': 'R23EK022', 'name': 'MAYANK KAIRA', 'attendance': False}, {'roll_no': 'R23EK055', 'name': 'Shubham Kumar Pandey', 'attendance': False}, {'roll_no': 'R23EK052', 'name': 'Yuvraj Singh', 'attendance': False}, {'roll_no': 'R23EK008', 'name': 'DASHARATH CHOUDHARI', 'attendance': False}, {'roll_no': '5', 'name': 'ANVESH BIDDAPA AD', 'attendance': False}, {'roll_no': 'R23EK051', 'name': 'VINAY KUMAR V', 'attendance': False}, {'roll_no': '6', 'name': 'KUNUPUDI BALAJI BALAJI', 'attendance': False}, {'roll_no': 'R23EK001', 'name': 'AHEMAD RAJA VHORA', 'attendance': False}, {'roll_no': 'R23EK036', 'name': 'S Sai Sree Hari', 'attendance': False}, {'roll_no': 'R23EK053', 'name': 'G KAILASH KUMAR', 'attendance': False}, {'roll_no': 'R23EK048', 'name': 'TARUN P J', 'attendance': False}, {'roll_no': 'R23EK005', 'name': 'Arnav Jude Dsouza', 'attendance': False}, {'roll_no': 'R23EK023', 'name': 'Michael Muanthang Tunglut', 'attendance': False}, {'roll_no': 'R23EK028', 'name': 'PALAGIRI MOHAMMAD SAHIL', 'attendance': False}, {'roll_no': 'R23EK027', 'name': 'P Lohith', 'attendance': False}, {'roll_no': 'R23EK019', 'name': 'Mahalakshmi J', 'attendance': False}, {'roll_no': 'R23EK017', 'name': 'M S Vaishnavi', 'attendance': False}, {'roll_no': 'R23EK031', 'name': 'R SAI SHREYA', 'attendance': False}, {'roll_no': 'R23EK025', 'name': 'Niranjana B', 'attendance': False}, {'roll_no': 'R23EK057', 'name': 'NAMIRA CHOUDHARY', 'attendance': False}, {'roll_no': 'R23EK035', 'name': 'RIYA S', 'attendance': False}, {'roll_no': 'R23EK033', 'name': 'RICHA C', 'attendance': False}, {'roll_no': 'R23EK014', 'name': 'KEERTHI K', 'attendance': False}, {'roll_no': 'R23EK045', 'name': 'TALANKI VENKATA SRI DURGA AMBICA BALE', 'attendance': False}, {'roll_no': 'R23EK054', 'name': 'KALUGOTLA SURESH HARSHITHA', 'attendance': False}, {'roll_no': 'R23EK039', 'name': 'Sharanya U', 'attendance': False}, {'roll_no': 'R23EK011', 'name': 'HARSHITH  RAJ S', 'attendance': False}, {'roll_no': 'R23EK037', 'name': 'Santhosh C', 'attendance': False}, {'roll_no': 'R23EK024', 'name': 'MUHAMMAD NAYEEM', 'attendance': False}, {'roll_no': 'R23EK050', 'name': 'Veshank R', 'attendance': False}, {'roll_no': 'R23EK018', 'name': 'MADHAN A', 'attendance': False}, {'roll_no': 'R23EK021', 'name': 'Manoj Patil', 'attendance': False}, {'roll_no': 'R23EK012', 'name': 'Jagadeep H M', 'attendance': False}, {'roll_no': 'R23EK034', 'name': 'RITESH UDAY BETAGERI', 'attendance': False}, {'roll_no': 'R23EK038', 'name': 'SANTHOSH S', 'attendance': False}, {'roll_no': 'R23EK044', 'name': 'SURYA ANAND', 'attendance': False}, {'roll_no': 'R23EK020', 'name': 'Mallikarjun', 'attendance': False}, {'roll_no': 'R23EK043', 'name': 'SUHANI', 'attendance': False}, {'roll_no': 'R23EK026', 'name': 'Nisha Yadav', 'attendance': False}, {'roll_no': 'R23EK004', 'name': 'Amrutha', 'attendance': False}, {'roll_no': 'R23EK029', 'name': 'PALLAVI R', 'attendance': False}, {'roll_no': 'R23EK058', 'name': 'CHITTEPU SREE LATHA', 'attendance': False}, {'roll_no': 'R23EK016', 'name': 'LIKHITHA D V', 'attendance': False}, {'roll_no': 'R23EK059', 'name': 'NEELI SURENDRA', 'attendance': False}, {'roll_no': 'R23EK010', 'name': 'Harish Chawan A', 'attendance': False}, {'roll_no': '1', 'name': 'PONNAPUREDDY CHANDRAKANTH REDDY', 'attendance': False}, {'roll_no': '2', 'name': 'V G SAI PRAKASH', 'attendance': False}, {'roll_no': '3', 'name': 'MUTHYALA GURU NITHISH', 'attendance': False}, {'roll_no': '4', 'name': 'ABEL BIJU PAREL', 'attendance': False}, {'roll_no': 'R23EK009', 'name': 'FARHAAN PASHA', 'attendance': False}, {'roll_no': 'R23EK002', 'name': 'ALBIN JAYESH CHEMANOOR', 'attendance': False}, {'roll_no': 'R23EK015', 'name': 'KRISHANU BERA', 'attendance': False}, {'roll_no': 'R23EK032', 'name': 'RAHUL GOWDA S M', 'attendance': False}, {'roll_no': 'R23EK006', 'name': 'BAPUGOUDA HANAMAGOUDA BIRADAR', 'attendance': False}, {'roll_no': 'R23EK030', 'name': 'PAVAN A PISSAY', 'attendance': False}]
        

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
