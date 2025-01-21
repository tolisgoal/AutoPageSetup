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
    
    if front == True: #if this is a front page add range to front str
        front_str += str(n)
        front_str += "-"
        
        if n+pages_per_sheet-1>file_pages: #if n+pages > total pages, set end of range to total pages
            front_str += str(file_pages)
        else:
            #n+pages-1 to get the end of the range
            front_str += str(n + pages_per_sheet-1)
        
        front_str += ", "
        
    elif front == False: #elif this is a back page add range to back str
        back_str += str(n)
        back_str += "-"
        
        if n+pages_per_sheet-1>file_pages:
            back_str += str(file_pages)
        else:
            back_str += str(n + pages_per_sheet-1)

        back_str += ", "
    
    front = not front #alternate between front and back

print("Front pages: ", front_str[:len(front_str)-2])
print("Back pages: ", back_str[:len(back_str)-2])