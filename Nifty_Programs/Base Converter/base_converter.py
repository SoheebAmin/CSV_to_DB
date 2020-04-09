# This program can convert any number from any base up to 36 into decimal. 
# The number must be entered as a string given the possibility of alphabetical characters. The numbers can be upper or lower, as will be converted to lower and then ascii, and then decimal in the calculation. 
# For base 1, 1 is used as the symbol, not 0, to resemble tally marks. 

def convert_to_decimal(num_as_string, base):
  digit_list = []
  if base > 36:
    return "Base 36 is the program limit"

# iterates through the list of numbers and letters. If number, puts in list, if letter, converts to ascii and puts in list.
  for symbol in num_as_string:
    if symbol.isalpha() == False:
      if int(symbol) >= base and base > 1:
        return "Not a valid entry for this base"
      if base == 1 and int(symbol) != base:
        return "Not a valid entry for this base" 
      digit_list.append(int(symbol))
    else:
      if (ord(symbol.lower())-86) > base:
        return "Not a valid entry for this base"
      digit_list.append(ord(symbol.lower())-87)

# calculates the value of each place by applying formula for bases on the elements of the list containing digits of number.
  i=len(num_as_string)-1
  answer = 0
  for digit in digit_list:
    answer = (answer) + (digit*(base**i))
    i-=1
  return answer  


#conversion test
print (convert_to_decimal("zzzz", 36))



## This was my first version of the program, that could only convert for basis 10 and under:

def convert_to_decimal_if_smaller(num_as_string, base):
  if base > 10:
    return "Base 10 is the program limit"
  if num_as_string.isdigit() == False:
    return "Non-integers detected"
  answer = 0
  
  # returns the input (as string to stay consistent on return type) if 10 is the input base
  if base == 10:
    return int(num_as_string)

  # this would mean a number to convert has a digit not capitable in the requested output base.
  for element in num_as_string:
    if int(element) >= base:
      return "Not a valid entry for this base"

  # calculates the value of each place by applying formula for bases on the elements of the list containing digits of number.
  else:
    i=len(num_as_string)-1
    for digit in num_as_string:
      answer = (answer) + (int(digit)*(base**i))
      i-=1
    return answer


