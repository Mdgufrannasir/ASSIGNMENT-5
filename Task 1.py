dist = {'Rooman': 80, 'Faisal':70, 'Zaif':75,}
name = input("Enter the student's name: ")
if name in dist:
    print(f"{name}'s marks: {dist[name]} ")
else:
    print('Student not found')