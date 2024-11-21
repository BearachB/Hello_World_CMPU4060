def add_fractions(tuple1, tuple2):
    denominator = tuple1[1] * tuple2[1]
    numerator = (denominator / tuple1[1]) * tuple1[0] + (denominator / tuple2[1]) * tuple2[0]

    return (numerator,denominator)

print(add_fractions([1,2],[1,2]))
