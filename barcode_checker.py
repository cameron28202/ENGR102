# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cameron Stone
# Section:      401
# Assignment:   Lab 11.11.1
# Date:         11/13/2022


#count variable to track # of valid barcodes
count = 0

#user input to get name of file
inp = input("Enter the name of the file: ")

#call open method using arguments inp ( name of file ) and r ( read )
barcodes = open(inp, "r")
valid_barcodes = open("valid_barcodes.txt", "w")

#loop through barcodes file
for next_line in barcodes:
    
    #sum_odd and sum_even variables to get the sum of the even and odd #'s in the barcode
    sum_odd = 0
    sum_even = 0
    for x in range(len(next_line) - 2):
        if x % 2 == 0:
            sum_even += int(next_line[x])
        else:
            sum_odd += int(next_line[x])
    
    #get last digit of sum of evens and odds
    sum_sums = str(sum_even + sum_odd * 3)
    last_digit = sum_sums[len(sum_sums) - 1]
    
    #if 10-last_digit is equal to the last number of the barcode, the barcode is valid. increment count
    if 10 - int(last_digit) == int(next_line[len(next_line)-2]):
        count += 1
        valid_barcodes.write(next_line)

#close barcode
barcodes.close()
valid_barcodes.close()
#print number of valid barcodes
print(f'There are {count} valid barcodes')