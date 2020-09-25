"""
start 
get the numbers of sheets
sheet/5
round answer to next number
end
"""



def calculate(sheet):
    answer = sheet / 5
    rounded = round(answer, 1)
    print("sheet is : ", sheet)
    print("The answer is: ", answer)
    print("rounded is: ", rounded)
    print("===============================")
    return rounded

output = calculate(16)

print("the return statement is: ", output)

