class StudentGradeCalculator:
    def __init__(self):
        self.students = []
        self.subjects = ['Math', 'Science', 'English', 'Social', 'Arts']
    
    def calculate_grade(self, average):
        """Calculate letter grade based on average marks"""
        if average >= 90:
            return 'A+'
        elif average >= 80:
            return 'A'
        elif average >= 70:
            return 'B'
        elif average >= 60:
            return 'C'
        elif average >= 50:
            return 'D'
        else:
            return 'F'
    
    def add_student(self, name, marks):
        """Add a new student with their marks"""
        if len(marks) != 5:
            print("Error: Please provide marks for all 5 subjects (Math, Science, English, Social, Arts)")
            return False
        
        # Validate marks are between 0-100
        for mark in marks:
            if not (0 <= mark <= 100):
                print("Error: Marks should be between 0 and 100")
                return False
        
        total = sum(marks)
        average = total / len(marks)
        grade = self.calculate_grade(average)
        
        student = {
            'name': name,
            'math': marks[0],
            'science': marks[1],
            'english': marks[2],
            'social': marks[3],
            'arts': marks[4],
            'total': total,
            'average': round(average, 2),
            'grade': grade
        }
        
        self.students.append(student)
        print(f"Student {name} added successfully!")
        return True
    
    def display_all_students(self):
        """Display all students in a formatted table"""
        if not self.students:
            print("No students found!")
            return
        
        print("\n" + "="*110)
        print("STUDENT MARKS & GRADES SUMMARY")
        print("="*110)
        
        # Header
        print(f"{'Student Name':<15} {'Math':<6} {'Science':<8} {'English':<8} {'Social':<7} {'Arts':<6} {'Total':<7} {'Average':<8} {'Grade':<5}")
        print("-"*110)
        
        # Student data
        for student in self.students:
            print(f"{student['name']:<15} {student['math']:<6} {student['science']:<8} {student['english']:<8} {student['social']:<7} {student['arts']:<6} {student['total']:<7} {student['average']:<8} {student['grade']:<5}")
        
        print("="*110)
    
    def get_class_statistics(self):
        """Calculate and display class statistics"""
        if not self.students:
            print("No students found!")
            return
        
        total_students = len(self.students)
        class_total = sum(student['total'] for student in self.students)
        class_average = class_total / (total_students * 5)  # 5 subjects
        
        # Grade distribution
        grade_count = {}
        for student in self.students:
            grade = student['grade']
            grade_count[grade] = grade_count.get(grade, 0) + 1
        
        print(f"\nCLASS STATISTICS:")
        print(f"Total Students: {total_students}")
        print(f"Class Average: {class_average:.2f}/100")
        print(f"Class Average Grade: {self.calculate_grade(class_average)}")
        
        print("\nGrade Distribution:")
        for grade, count in sorted(grade_count.items()):
            percentage = (count / total_students) * 100
            print(f"Grade {grade}: {count} students ({percentage:.1f}%)")
    
    def find_student(self, name):
        """Find and display a specific student's details"""
        for student in self.students:
            if student['name'].lower() == name.lower():
                print(f"\nStudent Details for {student['name']}:")
                print(f"Mathematics: {student['math']}")
                print(f"Science: {student['science']}")
                print(f"English: {student['english']}")
                print(f"Social Studies: {student['social']}")
                print(f"Arts: {student['arts']}")
                print(f"Total Marks: {student['total']}/500")
                print(f"Average: {student['average']}%")
                print(f"Grade: {student['grade']}")
                return student
        
        print(f"Student '{name}' not found!")
        return None
    
    def get_top_performers(self, n=3):
        """Get top N performing students"""
        if not self.students:
            print("No students found!")
            return
        
        sorted_students = sorted(self.students, key=lambda x: x['average'], reverse=True)
        top_students = sorted_students[:n]
        
        print(f"\nTOP {n} PERFORMERS:")
        print("-" * 50)
        for i, student in enumerate(top_students, 1):
            print(f"{i}. {student['name']} - {student['average']}% (Grade: {student['grade']})")

def main():
    calculator = StudentGradeCalculator()
    
    # Pre-populate with sample data (similar to the image)
    sample_students = [
        ("Alice Johnson", [95.5, 89.0, 92.2, 88.0, 87.5]),
        ("Bob Smith", [76.2, 82.5, 74.8, 79.0, 81.3]),
        ("Carol Davis", [95.0, 93.7, 97.5, 94.2, 96.0]),
        ("David Wilson", [61.3, 64.6, 58.5, 65.0, 63.2])
    ]
    
    for name, marks in sample_students:
        calculator.add_student(name, marks)
    
    while True:
        print("\n" + "="*50)
        print("STUDENT MARKS & GRADES CALCULATOR")
        print("="*50)
        print("1. Add New Student")
        print("2. Display All Students")
        print("3. Find Student")
        print("4. Class Statistics")
        print("5. Top Performers")
        print("6. Exit")
        print("-"*50)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            print("\nADD NEW STUDENT")
            name = input("Enter student name: ").strip()
            if not name:
                print("Name cannot be empty!")
                continue
            
            try:
                print("Enter marks for each subject (0-100):")
                math = float(input("Mathematics: "))
                science = float(input("Science: "))
                english = float(input("English: "))
                social = float(input("Social Studies: "))
                arts = float(input("Arts: "))
                
                marks = [math, science, english, social, arts]
                calculator.add_student(name, marks)
                
            except ValueError:
                print("Error: Please enter valid numbers for marks!")
        
        elif choice == '2':
            calculator.display_all_students()
        
        elif choice == '3':
            name = input("Enter student name to search: ").strip()
            calculator.find_student(name)
        
        elif choice == '4':
            calculator.get_class_statistics()
        
        elif choice == '5':
            try:
                n = int(input("Enter number of top performers to display (default 3): ") or "3")
                calculator.get_top_performers(n)
            except ValueError:
                calculator.get_top_performers()
        
        elif choice == '6':
            print("Thank you for using Student Marks & Grades Calculator!")
            break
        
        else:
            print("Invalid choice! Please select 1-6.")

if __name__ == "__main__":
    main()
