from pyscript import document, display

name = "Elise" #string 
age = 15 #integer
height123 = 164.0 #float
favorite_countries = ["Japan", "Korea", "Australie"] #list
student_type = False #boolean
about_me = {
    "color" : "Pink",
    "car_brand" : "Mazda",
    "shoe_size" : "7.5",
    "best_friend" : "Cheree"
} #dictionary

good_fruits = {"Mango", "Banana", "Strawberry", "Apple","Pineapple"} #set
days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday") #tuple

display(type(name), target="div1")
display(type(age), target="div1")
display(type(height123), target="div1")
display(type(favorite_countries), target="div1")
display(type(student_type), target="div1")
display(type(about_me), target="div1")
display(type(good_fruits), target="div1")
display(type(days_of_the_week), target="div1")

def add_numbers(e):
    document.getElementById("output1").innerHTML=""
    num1 = float(document.getElementById('input1').value)
    num2 = float(document.getElementById('input2').value)
    result = num1 + num2
    display(result, target = "output1") 

def subtract_numbers(e):
    document.getElementById("output1").innerHTML=""
    num1 = float(document.getElementById('input1').value)
    num2 = float(document.getElementById('input2').value)
    result = num1 - num2
    display(result, target = "output1")