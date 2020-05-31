def vec_len(vektor):
    output = 0
    for i in range(len(vektor)):
        output += vektor[i]**2
    output = output ** 0.5
    print(output)

vec_len([3,4])




