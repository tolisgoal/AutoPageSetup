# AutoPageSetup

### Usage:

Enter the total number of pages of your pdf/word/whatever file you want to print

Enter how many pages you want to be printed on each side of each sheet of paper

Get the ranges you will need to enter in the print interface to make this print happen, separated
in front and back pages (meaning you will print the front pages, reorder them and feed them back
to the printer on the opposite side so you can print both sides of each sheet)

### Example:
I have a pdf with 63 pages, that I want to print with 4 pages per sheet, front and back

I enter Total pages: 63, Pages per sheet: 4

I get: 
Front pages: 1-8, 17-24, 33-40, 49-56
Back pages: 9-16, 25-32, 41-48, 57-63

Then simply copy the first range into the print interface (1-8, 17-24, 33-40, 49-56),
let it print, making sure to have the pages in the correct order and fed to the printer
then print again using the second range

### NOTE: If your printing interface has the 'Reverse Order' option you can reverse the order of printing
### on the front pages, so that you don't have to reorder them first to last for the back print
