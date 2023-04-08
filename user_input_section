import threading, math
from cotter import case1, case2


a, b = input("Enter the power value and 10 rise value separated by space: ").split()
power1 = float(a) * float(math.pow(10, int(b)))
power = round(power1, 4)
shear_stress = float(input("Enter the shear stress value in N/mm^2: "))
tensile_stress = float(input("Enter the tensile stress value in N/mm^2: "))
crushing_stress = float(input("Enter the crushing stress in N/mm^2: "))

print("to find inner dia of socket, we need thickness t")
thickness = input("enter thickness value in mm, otherwise put 'NO': ")
    

def main(thickness):
    if thickness.upper() == 'NO':
        th1 = threading.Thread(target=case1(power, crushing_stress, tensile_stress, shear_stress))
        th1.start()
    else:
        th2 = threading.Thread(target=case2(power, crushing_stress, tensile_stress, shear_stress, thickness))
        th2.start()


if __name__ == '__main__':
    main(thickness)
