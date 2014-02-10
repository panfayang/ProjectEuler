num = "onetwothreefourfivesixseveneightnine"
num10 = "teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen"
num20 = "twentythirtyfortyfiftysixtyseventyeightyninety"
num100 = "hundred"

def count(n):
    c = 0
    for i in n:
        c += 1
    return c

count99 = count(num)*9 + count(num10) + count(num20)*10

count100 = count(num)*100 +count(num100)*900 + count("and")*99*9 + count99*10

print count100+count("onethousand")
