def student_details(students, student_id):
    if student_id not in students:
      return None                         # à toi : return None
    student = students[student_id]                  # à toi : la fiche de student_id
    return student["name"], student["score"]                # à toi : le nom et la note, séparés par une virgule

students = {
    "S1": {"name": "Noa", "score": 80},
    "S2": {"name": "Dan", "score": 0}
}
print(student_details(students, "S2"))
print(student_details(students, "S1"))
print(student_details(students, "S9"))
print(student_details({}, "S1"))