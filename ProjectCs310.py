def register() :
    print("=" * 86)
    print("%s %s %s" % (" "*35,"REGISTER"," "*37))
    print("=" * 86)
    with open("data.txt", "a") as file:
        first_name, last_name = input("Enter Name Surname : ").split()
        while True:
            id_card = input("Enter ID card [13 digits] : ")
            while len(id_card) != 13:
                print("ID card must be 13 digits")
                id_card = input("Enter ID card [13 digits] : ")
            id_sum = ((int(id_card[0])*13) + (int(id_card[1])*12) + (int(id_card[2])*11) + (int(id_card[3])*10) + (int(id_card[4])*9) + (int(id_card[5])*8) + (int(id_card[6])*7) + (int(id_card[7])*6) + (int(id_card[8])*5) + (int(id_card[9])*4) + (int(id_card[10])*3) + (int(id_card[11])*2)) % 11
            id_true = (11 - id_sum) % 10
            if id_true == int(id_card[12]):
                break
            else:
                print("ID card False !")
                print("Please try again")

        file.write("%s %s %s\n" % (first_name,last_name,str((ord(first_name[0])+ord(last_name[1]))) + id_card[7] + id_card[3] + id_card[6] + id_card[8] + id_card[5] + id_card[12] + id_card[1]))

        print("Register Complete")

 
def add_product() :
    print("=" * 86)
    print("%s %s %s" % (" "*35,"PRODUCT"," "*39))
    print("=" * 86)
    with open("product.txt", "a") as file:
        product_name = input("Enter Product Name : ")
        product_price = input("Enter Product Price : ")
        product_quantity = input("Enter Product Quantity : ")
        file.write("%s %s %s\n" % (product_name,product_price,product_quantity))

def show_product() :
    print("=" * 86)
    print("%s %s %s" % (" "*35,"PRODUCT"," "*39))
    print("=" * 86)
    with open("product.txt", "r") as file:
        for line in file:
            print(line)
        
def show_user() :
    print("=" * 86)
    print("%s %s %s" % (" "*35,"USER"," "*41))
    print("=" * 86)
    with open("data.txt", "r") as file:
        for line in file:
            print(line)

def sale_product() :
    print("=" * 86)
    print("%s %s %s" % (" "*35,"SALE"," "*41))
    print("=" * 86)
    with open("product.txt", "r") as file:
        for line in file:
            print(line)
    with open("product.txt", "r") as file:
        product_name = input("Enter Product Name : ")
        product_quantity = input("Enter Product Quantity : ")
        for line in file:
            if product_name in line:
                print(line)
                print("Sale Complete")