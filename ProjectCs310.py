user_list = []
product_list = []

def register() :
    print("=" * 86)
    print("%s %s %s" % (" "*35,"REGISTER"," "*37))
    print("=" * 86)
    with open("userdata.txt", "a") as file:
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

        file.write("%s %-20s %-20s %s\n" % (first_name,last_name,id_card,str((ord(first_name[0])+ord(last_name[1]))) + id_card[7] + id_card[3] + id_card[6] + id_card[8] + id_card[5] + id_card[12] + id_card[1]))

        print("Register Complete")

# def delete_user() :
#     print("=" * 86)
#     print("%s %s %s" % (" "*35,"DELETE USER"," "*35))
#     print("=" * 86)
#     id_card = input("Enter ID card : ")
#     with open("userdata.txt", "r") as file:
#         data = file.read().splitlines()
#         for line in data:
#             item = line.split()
#             # print(item)
#             user_list.append(item)
#     for i in range(len(user_list)):
#         if id_card in user_list[i]:
#             user_list.pop(i)
#             break
#     with open("userdata.txt", "w") as file:
#         for i in range(len(user_list)):
#             file.write("%s %-20s %-20s %s\n" % (user_list[i][0],user_list[i][1],user_list[i][2],user_list[i][3]))

def append_product_list() :
    with open("product.txt", "r") as file:
        data = file.read().splitlines()
        for line in data:
            item = line.split()
            # print(item)
            product_list.append(item)
 
def addstock_product() :
    print("=" * 86)
    print("%s %s %s" % (" "*35,"PRODUCT"," "*39))
    print("=" * 86)
    product_name = input("Enter Product Name : ")
    product_quantity = input("Enter Product Quantity : ")
    for i in range(len(product_list)):
        if product_name in product_list[i]:
            product_list[i][2] = int(product_list[i][2]) + int(product_quantity)
            # print(product_list[i])
    with open("product.txt", "w") as file:
        for i in range(len(product_list)):
            file.write("%-13s %-23s %20s %28s\n" % (product_list[i][0],product_list[i][1],product_list[i][2],product_list[i][3]))
    print("Add Stock Product Complete")

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
    with open("userdata.txt", "r") as file:
        for line in file:
            print(line)

def sale_product() :
    print("=" * 86)
    print("%s %s %s" % (" "*35,"SALE"," "*41))
    print("=" * 86)
    code_number = input("Enter Code Number : ")
    product_quantity = input("Enter Product Quantity : ")
    for i in range(len(product_list)):
        if code_number in product_list[i]:
            product_list[i][2] = int(product_list[i][2]) - int(product_quantity)
            # print(product_list[i])
    with open("product.txt", "w") as file:
        for i in range(len(product_list)):
            file.write("%-13s %-23s %20s %28s\n" % (product_list[i][0],product_list[i][1],product_list[i][2],product_list[i][3]))


# with open("product.txt", "a") as file:
#     codename = input("Enter Code Name : ")
#     product_name = input("Enter Product Name : ")
#     product_quantity = input("Enter Product Quantity : ")
#     product_price = input("Enter Product Price : ")
#     file.write("%-13s %-23s %20s %28s\n" % (codename,product_name,product_quantity,product_price))
