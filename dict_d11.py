def student_details(students, student_id):
    if student_id not in students:
      return None                         
    student = students[student_id]                 
    return student["name"], student["score"]            

students = {
    "S1": {"name": "Noa", "score": 80},
    "S2": {"name": "Dan", "score": 0}
}
print(student_details(students, "S2"))
print(student_details(students, "S1"))
print(student_details(students, "S9"))
print(student_details({}, "S1"))