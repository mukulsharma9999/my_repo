student = {
    "name" : "Mukul",
    "courses" : "btech",
    "domain" : "cloud computjing"
}
print('name:',student["name"])
print('course :', student["courses"])
 #adding a new element
student["grade"]  = "A"
print("updated lisst", student)
 # removing aa  elemnt
del student["courses"]
print("updated list:", student)