course_name = 'Open System Automation'
course_code = 'OPS445'
course_number = 445


course_name = 'Open System Automation'
print(course_name[-10:])                            # Return the last ten characters
print(course_name[-10:-6])                          # Try and figure out what this is returning 
print(course_name[0:4] + course_name[-10:-6])       # Combine substrings together
substring = course_name[0:4] + course_name[-10:-6]  # Save the combined substring as a new string for later
print(substring)