 courses = ['Maths', 'Physics', 'CompSci', 'Geography']
courses_2 = ['History', 'Finance']
num =  [1 , 2, 4, 7]
print(courses)
#prints the list of courses above
print(len(courses))
#prints the length of courses
print(courses[0])
#Accessing specific values of the list
print(courses[-1])
#-1 is always the last item on the list 
print(courses[0:2])
#printsfrom zero till two, not including two
print(courses.append('Art'))
#adds selected item to the list
print(courses.insert(1, 'Art'))
#allows you to edit what you want into the list and where you want it to be added
print(courses.extend(courses_2))
#Adds second list into the main list
print(courses.remove('Maths'))
#remove values from the list
print(courses.pop())
#removes the last on the list
print(courses.sort())
#sort courses Alphabetically, also sort numbers on list too
print(sorted(courses))
#sorted function sorts the list fromascending to descending
print(min(num))
#prints the minimum value of numbers in the list and max prints the maximum value of the list
print(sum(num))
#prints the sum of the numbers in the list
print(courses.index('Geography'))
#prints the index of thye item in the list
print(courses)

for course in courses:
    print(course)
#prints each course on a different line
    
course_str = '- '.join(courses)
print(course_str)


courses = ('Maths', 'Physics', 'CompSci', 'Geography')
#A TUPLE, its immutable cant relly edit it

courses = {'Maths', 'Physics', 'CompSci', 'Geography'}
#A set doesnt care avout arrangement but seives out duplicates 

courses = {'Maths', 'Physics', 'CompSci', 'Geography'}
art_courses = {'Maths', 'Design', 'Education', 'Geography'}
print(courses.intersection(art_courses))
#intersection basically
print(courses.difference(art_courses))
#does the oppodite of intersection
print(courses.union(art_courses))
#joins the two together without duplicates
