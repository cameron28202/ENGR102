# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Julie Henderson
#               Frank Rodriguez
#               Kareem Elias
#               Cameron Stone
# Section:      401
# Assignment:   Lab 
# Date:         11/14/2022
#

def validate_passport(passport_dict):
    num_valid = 0
    
    if "hcl" in passport_dict:
        if len(passport_dict) < 8:
            return False
    else:
        if len(passport_dict) < 7:
            return False
    
    
    byr = int(passport_dict["byr"])
    iyr = int(passport_dict["iyr"])
    eyr = int(passport_dict["eyr"])
    hgt = passport_dict["hgt"]
    ecl = passport_dict["ecl"]
    pid = passport_dict["pid"]
    cid = passport_dict["cid"]
    
    if byr >= 1920 and byr <= 2005:
        num_valid += 1
    if iyr >= 2012 and iyr <= 2022:
        num_valid += 1
    if eyr >= 2022 and eyr <= 2032:
        num_valid += 1
    if "in" in hgt:
        if int(hgt.replace("in", "")) >= 59 and int(hgt.replace("in", "")) <= 76:
            num_valid += 1
    elif "cm" in hgt:
        if int(hgt.replace("cm", "")) >= 150 and int(hgt.replace("cm", "")) <= 193:
            num_valid += 1
    if "amb" == ecl or "blu" == ecl or "brn" == ecl or "gry" == ecl or "grn" == ecl or "hzl" == ecl or "oth" == ecl:
        num_valid += 1
    if len(pid) == 9:
        num_valid += 1
    
    str = cid.lstrip('0')
    if len(str) == 3:
        num_valid += 1
    
    if num_valid == 7:
        return True
    return False
    

#input variable for name of file
inp = input("Enter the name of the file: ")
#open passports file to read
passports = open(inp, "r")
#open valid passports file to write
valid_passports2 = open("valid_passports2.txt", "w")
#establish count variable to track number of valid passports
count = 0
#establish fields variable to hold each passport
fields = ""


#loop through passports file
for next_line in passports:
    #if the line isn't empty, meaning it isnt the beginning of a new passport, add the line to fields
    if next_line != '\n':
        fields += next_line
    else:
        old_fields = fields
        fields = fields.replace(" ", ":")
        fields = fields.replace("\n", ":")
        arg_list = fields.split(":")
        arg_list.remove('')
        passport_dict = {}
        
        
        x = 0
        while x <= len(arg_list)-1:
            passport_dict[arg_list[x]] = arg_list[x+1]
            x += 2
        
        if validate_passport(passport_dict) == True:
            valid_passports2.write(old_fields)
            valid_passports2.write("\n")
            count += 1
        
        
        fields = ""
    
#print to user, close files
print(f'There are {count} valid passports')
passports.close()
valid_passports2.close()