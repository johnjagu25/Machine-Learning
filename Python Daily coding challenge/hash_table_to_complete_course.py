# You are given a hash table where the key is a course code, 
# and the value is a list of all the course codes that are prerequisites for the key. 
# Return a valid ordering in which we can complete the courses. If no such ordering exists, 
# return NULL.

# Example:
# {
#   'CSC300': ['CSC100', 'CSC200'], 
#   'CSC200': ['CSC100'], 
#   'CSC100': []
# }

# This input should return the order that we need to take these courses:
#  ['CSC100', 'CSC200', 'CSCS300']

# Here's your starting point:
org = []
def courses_to_take(course_to_prereqs):
    global org
    temp = []
    temp1 = []
    def course(course_to_prereqs,temp,temp1):
       
        for course_code in course_to_prereqs:
            temp.append(course_code)
            temp1.append(course_code)
            for code in course_to_prereqs[course_code]:
                if code in course_to_prereqs:
                    temp1.append(code)
                    if len(course_to_prereqs[code]):
                        course({code : course_to_prereqs[code]},temp,temp1)   
    course(course_to_prereqs,temp,temp1)
    return org

courses = {
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}
print(courses_to_take(courses))