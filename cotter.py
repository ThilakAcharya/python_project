import math
       
''' Case 1: if the thickness is unknown 1st find thickness then move on to other parameter'''
    
def case1(power,crushing_stress,tensile_stress,shear_stress):
    solid_dia = math.sqrt((power * 4) / (math.pi * tensile_stress))
    solid_dia = round(solid_dia, 4)
    print("\n diameter of solid rod " + str(solid_dia) + "mm")
    print("\n Design of rod: ")
    d_t = (power / crushing_stress)
    d_t = round(d_t)
    print("\t d*t value:" + str(d_t))

    inner_dia = math.sqrt(((power / tensile_stress) + d_t) * (4 / math.pi))
    inner_dia = round(inner_dia, 4)
    print(f'\t inner dia of the socket :{round(inner_dia, 4)} mm = {inner_dia} mm')

    print("\n Design of collar")
    d_2 = ((power / crushing_stress) * (4 / math.pi) + math.pow(inner_dia, 2))
    d_2 = math.sqrt(d_2)
    d_2 = round(d_2, 4)
    print(f' \t diameter of the collar is, d2:{d_2} mm = {round(d_2)} mm') 

    thickness_t_1 = power / (math.pi * inner_dia * shear_stress)
    thickness_t_1 = round(thickness_t_1, 4)
    print(f'\t Thickness of the collar is, t1: {thickness_t_1} mm')
    l_1 = power / (2 * inner_dia * shear_stress)
    l_1 = round(l_1, 4)
    print(f'\t length of the collar, l1: {l_1} mm = {round(l_1)} mm')
    
    print("\n Design of Cotter: ")
    t = d_t / inner_dia
    t = round(t, 4)
    print(f'\t Thickness of the joints, t: {t} mm = {round(t)} mm')

    b1 = power / (2 * shear_stress * t)
    print(f'\t width of the joints: {round(b1, 4)} mm = {round(b1)} mm')

    print("also we have width of joints ,b = 5t")

    b2 = round(5 * t, 4)
    print(f'\t width by 5*t is, b: {b2} mm ={round(b2)} mm')

    if b1 > b2:
        print(f'\t adopt the larger value, i.e b= {round(b1, 4)} mm')
        b = b1
    else:
        print(f'\t adopt the larger value, i.e b= {round(b2, 4)} mm')
        b = b2
    print("\n Design of Socket: ")
  # quadratic equation block
    x = round(math.pi / 4, 4)

    y = -(t)

    z = round(-(x * (inner_dia ** 2)) + (inner_dia * t) - (power / tensile_stress), 4)

    D1 = round((-y + math.sqrt((t ** 2) - 4 * x * z)) / (2 * x), 4)
    print(f'\t quadratic equation answers x: {x} y: {y} z: {z} \n \t then D1: {D1} mm')
    print(f'\t outer diameter of the socket end, D1: {D1} mm = {round(D1)} mm')

    D = (power / (crushing_stress * t)) + inner_dia
    D = round(D, 4)
    print(f'\t Diameter of the socket,D: {D} mm = {round(D)} mm')

    l = (power / (shear_stress * 2 * (D - inner_dia)))
    l = round(l, 4)
    print(f'\t length l:{l} mm = {round(l)} mm')

    t2 = round((power / (math.pi * solid_dia * shear_stress)))
    print(f'\t Thickness of the socket end, t2: {t2} mm = {round(t2)} mm')

    # for bending stress

    bending_stress = ((power * D*3) / (4 * t * (b ** 2)))
    bending_stress = round(bending_stress, 4)
    print(f'Bending Stress is: {bending_stress} mm = {round(bending_stress)}mm')

    if bending_stress < tensile_stress:
        print(f'\t\n bending stress is less than allowable tensile stress i.e,    {bending_stress} < {tensile_stress} design is safe')
    else:
        print(f'\t\n bending stress is greater than allowable tensile stress i.e, {bending_stress} > {tensile_stress} design is not safe')


def case2(power,crushing_stress,tensile_stress,shear_stress,thickness):
    solid_dia = math.sqrt((power * 4) / (math.pi * tensile_stress))
    solid_dia = round(solid_dia, 4)
    print("\ndiameter of solid rod " + str(solid_dia) + "mm")

    # inner diameter and design of the collar calculation
    
    print(f'thickness is{thickness} mm')
    thickness = float(thickness)
    inner_dia = power / (thickness * crushing_stress)
    inner_dia = round(inner_dia)
    print(f'\t inner dia of the socket :{round(inner_dia, 4)} mm = {inner_dia} mm')


    print("\n Design of collar")
    d_21 = ((power / crushing_stress) * (4 / math.pi) + math.pow(inner_dia, 2))
    d_2 = math.sqrt(d_21)
    d_2 = round(d_2, 4)

    print(f' \t diameter of the collar is, d2:{d_2} mm = {round(d_2)} mm')
    thickness_t_1 = power / (math.pi * inner_dia * shear_stress)
    thickness_t_1 = round(thickness_t_1, 4)

    print(f'\t Thickness of the collar is, t1: {thickness_t_1} mm')
    l_1 = power / (2 * inner_dia * shear_stress)
    l_1 = round(l_1, 4)
    print(f'\t length of the collar, l1: {l_1} mm = {round(l_1)} mm')

    print("\n Design of Cotter: ")
    t = thickness
    t = round(t, 4)
    print(f'\t Thickness of the joints, t: {t} mm = {round(t)} mm')

    b1 = power / (2 * shear_stress * t)
    print(f'\t width of the joints: {round(b1, 4)} mm = {round(b1)} mm')

    print("also we have width of joints ,b = 5t")

    b2 = round(5 * t, 4)
    print(f'\t width by 5*t is, b: {b2} mm ={round(b2)} mm')

    if b1 > b2:
        print(f'\t adopt the larger value, i.e b= {round(b, 4)} mm')
        b = b1
    else:
        print(f'\t adopt the larger value, i.e b= {round(b1, 4)} mm')
        b = b2
    print("\n Design of Socket: ")
    
    # quadratic equation block
    x = round(math.pi / 4, 4)

    y = -(t)

    z = round(-(x * (inner_dia ** 2)) + (inner_dia * t) - (power / tensile_stress), 4)

    D1 = round((-y + math.sqrt((t ** 2) - 4 * x * z)) / (2 * x), 4)
    print(f'\t quadratic equation answers x: {x} y: {y} z: {z} \n \t then D1: {D1} mm')
    print(f'\t outer diameter of the socket end, D1: {D1} mm = {round(D1)} mm')

    D = (power / (crushing_stress * t)) + inner_dia
    D = round(D, 4)
    print(f'\t Diameter of the socket,D: {D} mm = {round(D)} mm')

    l = (power / (shear_stress * 2 * (D - inner_dia)))
    l = round(l, 4)
    print(f'\t length l:{l} mm = {round(l)} mm')

    t2 = round((power / (math.pi * solid_dia * shear_stress)))
    print(f'\t Thickness of the socket end, t2: {t2} mm = {round(t2)} mm')

    # for bending stress

    bending_stress = ((power * D*3) / (4 * thickness * (b ** 2)))
    bending_stress = round(bending_stress, 4)
    print(f'Bending Stress is: {bending_stress} mm = {round(bending_stress)}mm')

    if bending_stress < tensile_stress:
        print(
            f'\t\n bending stress is less than allowable tensile stress i.e, {bending_stress} < {tensile_stress} design is safe')
    else:
        print(
            f'\t\n bending stress is greater than allowable tensile stress i.e, {bending_stress} > {tensile_stress} design is not safe')

