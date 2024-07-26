# from math import pi

# r = int(input())


# def circle_width(r):

#     return int(r)**2*round(pi, 6), round(2*int(r)**2, 6)


# uclid, taxi = circle_width(r)

# print(uclid)
# print(taxi)

# from math import pi

# r = int(input())


# def circle_width(r):

#     return int(r)**2*round(pi, 6), round(2*int(r)**2, 6)


# uclid, taxi = circle_width(r)

# print("%.6lf\n%.6lf", uclid, taxi)

from math import pi

r = int(input())

uclid = round(r**2*pi, 6)
taxi = 2*r**2

print("%10.6f" % uclid)  # "%10.nf"%변수 >> 소수점 아래 n자리 만큼 빈자리 소수점 채워주기
print("%10.6f" % taxi)
