from codes import morse_codes

str_input = input("Enter your string: \n").upper()

output_str = ""

for i in str_input:
    if i in morse_codes:
        output_str += morse_codes[i] + " "

print(output_str)
