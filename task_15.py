import local_ru as r

centimeter = float(input(r.LENGTH))
inch = centimeter / 2.54
foot = inch / 12
yard = foot / 3
mile = yard / 1760
print(str(yard) + r.YARD, str(mile) + r.MILE, str(foot) + r.FOOT, str(inch) + r.INCH, sep='\n')
