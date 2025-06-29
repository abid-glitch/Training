total_days = int(input("Total working days: "))
days_missed = int(input("Days absent: "))

attendance = ((total_days - days_missed) / total_days) * 100
print("Attendance percentage:", attendance)

if attendance < 75:
    print("Not allowed for exams")
else:
    print("Allowed to appear in exams")
