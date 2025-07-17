#TF2 Ref Calculator
# Discord of Author: seryozniman

# ------------------------------------------------------------------


# ------------------------------------------------------------------
while True:
    ItemPrice = float(input("Enter Item Price: "))
    quantity = int(input("Enter Quantity: "))
# ------------------------------------------------------------------
    integers = int(ItemPrice // 1)
    decimal = int((round(ItemPrice % 1, 2)) * 100)
# ------------------------------------------------------------------
    ProductIntegers = integers * quantity
    ProductDecimals = decimal
    ProductDecimals11 = 0
    k = decimal // 11
    ProductDecimals05 = decimal - k * 11
    BoolSummand = True
# ------------------------------------------------------------------
    if decimal % 11 == 0:
        ProductDecimals = decimal * quantity
    else:
        for i in range(1, quantity):
            ProductDecimals += (k * 11)
            if BoolSummand == True:
                ProductDecimals += ProductDecimals05 + 1
                BoolSummand = False

            else:
                ProductDecimals += ProductDecimals05
                BoolSummand = True
# ------------------------------------------------------------------
    if ProductDecimals >= 99:
        ProductIntegers += ProductDecimals // 99
        ProductDecimals = ProductDecimals % 99
# -----------------------------------------------------------------
    if len(str(ProductDecimals)) == 1:
      ProductDecimals = "0" + str(ProductDecimals)
# -----------------------------------------------------------------
    print(f"Price: {ProductIntegers}.{str(ProductDecimals)}")
