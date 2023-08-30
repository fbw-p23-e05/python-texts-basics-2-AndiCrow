#Task 1 
text = "Berlin is a world city of culture, politics, media and science."

text_count = len(text)

print(text_count)

#Task 2

text = "Berlin is a world city of culture, politics, media and science."

print(text[0], text[-1])

#Task 3

text = "Berlin is a world city of culture, politics, media and science."

print(text[0:3])


#Task 4

text = ("Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital")

text_count = text.count("b")


print("B appears:", text_count, "times")


#Task 5

text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."

print(text[-10:])

#Task 6

text = "---Python programming--- "

new_text = text.replace("-", "")

print(new_text)

#Task 7

Firstname = "Andi"
Lastname = "Rajchert"

print(F"Firstname: {Firstname}\nLastname: {Lastname}")