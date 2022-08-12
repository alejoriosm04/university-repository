tipo_producto = int(input())
cantidad_productos = int(input())

if tipo_producto == 1:
    print(cantidad_productos * 5)
elif tipo_producto == 2:
    print(cantidad_productos * 10)
elif tipo_producto == 3:
    print(cantidad_productos * 15)


## Solution created by @Manuela Castaño Franco


# product_type = int(input())
# product_quantity = int(input())


# def type1(productq):
#     return productq * 5


# def type2(productq):
#     return productq * 10


# def type3(productq):
#     return productq * 15


# typesDict = {
#     1: type1(product_quantity),
#     2: type2(product_quantity),
#     3: type3(product_quantity)

# }


# def supertypes(ptype):
#     return typesDict.get(ptype)


# print(supertypes(product_type))