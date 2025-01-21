while True:
    try:
        file_pages = int(input("Number of pages in file:"))
        if file_pages<2:
            print("Pages cannot be less than 2")
            continue
        #print(type(file_pages))
        break
    except ValueError:
        print("Invalid input")

while 1:
    try:
        pages_per_sheet = int(input("How many pages to print per sheet:"))
        if pages_per_sheet<2:
            print("Pages per sheet cannot be less than 2")
            continue
        break
    except ValueError:
        print("Invalid input")

front_str = ""
back_str = ""
front = True

for n in range(1, file_pages, pages_per_sheet): #first loop 1(1-4) 5 (5-8)
    
    if front: #if this is a front page add range to front str
        front_str += str(n)
        front_str += "-"
        
        if n+pages_per_sheet-1>file_pages: #if n+pages > total pages, set end of range to total pages
            front_str += str(file_pages)
        else:
            #n+pages-1 to get the end of the range
            front_str += str(n + pages_per_sheet-1)
        
        front_str += ", "
        
    else: #elif this is a back page add range to back str
        back_str += str(n)
        back_str += "-"
        
        if n+pages_per_sheet-1>file_pages:
            back_str += str(file_pages)
        else:
            back_str += str(n + pages_per_sheet-1)

        back_str += ", "
    
    front = not front #alternate between front and back

#Remove extra ", " at the end of each str
front_str = front_str[:len(front_str)-2]
back_str = back_str[:len(back_str)-2]

#if filepages%sheets==1 the last page gets skipped so added this to fix the issue
if file_pages%pages_per_sheet == 1:
    if front:
        front_str += ", "
        front_str += str(file_pages)
    else:
        if back_str!="": #if back str is not empty also add separator
            back_str += ", "
        back_str += str(file_pages)

'''
#split strings into lists of each range (ex: '1-2', '3-4', '5-6' etc)
front_str = (front_str.split(", "))
front_output = ""

#create new output strings with all ranges in reverse order, for easier front and back printing
for i in reversed(front_str):
    front_output += i
    front_output += ", "


#Remove extra ", " at the end of each str
front_output = front_output[:len(front_output)-2]
'''

print("WARNING: Make sure to select 'Reverse Order' in print options during front page printing.")
print()
print("Front pages: ", front_str)
print("Back pages: ", back_str)