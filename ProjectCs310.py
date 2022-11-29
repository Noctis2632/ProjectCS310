user_list = []
product_list = []
calculate_list = []

def user_lists() : # เพิ่มข้อมูลสมาชิกลงlist
    with open("userdata.txt", "r") as file:
        data = file.read().splitlines()
        for line in data:
            item = line.split()
            user_list.append(item)

def product_lists() : # เพิ่มข้อมูลสินค้าลงlist
    with open("product.txt", "r") as file:
        data = file.read().splitlines()
        for line in data:
            item = line.split()
            product_list.append(item)

def register() :   # สมัครสมาชิก
    print("=" * 86)
    print("%s %s %s" % (" "*35,"REGISTER"," "*37))
    print("=" * 86)
    with open("userdata.txt", "a") as file:
        ch = "Y"
        while ch != "N" :
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

            file.write("%-18s %-21s %-30s %s\n" % (first_name,last_name,id_card,str((ord(first_name[0])+ord(last_name[1]))) + id_card[7] + id_card[3] + id_card[6] + id_card[8] + id_card[5] + id_card[12] + id_card[1]))
            print("Your ID Member is",str((ord(first_name[0])+ord(last_name[1]))) + id_card[7] + id_card[3] + id_card[6] + id_card[8] + id_card[5] + id_card[12] + id_card[1])

            ch = input("Do you want to register again ? [Y/N] : ").upper()

        print("Register Complete")

def delete_member() : # ลบสมาชิก
    print("=" * 86)
    print("%s %s %s" % (" "*35,"DELETE MEMBER"," "*35))
    print("=" * 86)
    ch = "Y"
    while ch != "N" :
        id_member = input("Enter ID Member : ")
        for i in range(len(user_list)):
            if id_member in user_list[i]:
                user_list.pop(i)
                print("Delete Member Complete")
                break
            else:
                print("ID Member not found")
                break
        with open("userdata.txt", "w") as file:
            for i in range(len(user_list)):
                file.write("%-18s %-21s %-30s %s\n" % (user_list[i][0],user_list[i][1],user_list[i][2],user_list[i][3]))
        ch = input("Do you want to delete again ? [Y/N] : ").upper()
    

def addstock_product() : # เพิ่มสินค้า
    print("=" * 86)
    print("%s %s %s" % (" "*35,"PRODUCT"," "*39))
    print("=" * 86)
    product_name = input("Enter Product Name : ")
    product_quantity = input("Enter Product Quantity : ")
    for i in range(len(product_list)):
        if product_name in product_list[i]:
            product_list[i][2] = int(product_list[i][2]) + int(product_quantity)
    with open("product.txt", "w") as file:
        for i in range(len(product_list)):
            file.write("%-13s %-23s %20s %27s\n" % (product_list[i][0],product_list[i][1],product_list[i][2],product_list[i][3]))
    print("Add Stock Product Complete")

def show_user() : # แสดงข้อมูลสมาชิก
    print("=" * 86)
    print("%s %s %s" % (" "*35,"USER"," "*41))
    print("=" * 86)
    with open("userdata.txt", "r") as file:
        for line in file:
            print(line)

def show_product() : # แสดงข้อมูลสินค้า
    print("=" * 86)
    print("%s %s %s" % (" "*35,"PRODUCT"," "*39))
    print("=" * 86)
    with open("product.txt", "r") as file:
        for line in file:
            print(line)

def calculate() : # คำนวณราคาสินค้า
    print("=" * 86)
    print("%s %s %s" % (" "*35,"CALCULATE"," "*36))
    print("=" * 86)
    ch = "Y"
    while ch != "N" :
        code_number = input("Enter Code Number : ")
        for i in range(len(product_list)):
            if code_number in product_list[i]:
                product_quantity = input("Enter Product Quantity : ")
                calculate_list.append([product_list[i][1],product_quantity,(int(product_list[i][3])*int(product_quantity))])
                product_list[i][2] = int(product_list[i][2]) - int(product_quantity)
            else:
                print("Code Number False !")
                break
            with open("product.txt", "w") as file:
                for i in range(len(product_list)):
                    file.write("%-13s %-23s %20s %27s\n" % (product_list[i][0],product_list[i][1],product_list[i][2],product_list[i][3]))
    
        ch = input("Do you want to calculate again ? [Y/N] : ").upper()

def dicount() : # คำนวณส่วนลด
    print("=" * 86)
    print("%s %s %s" % (" "*35,"DISCOUNT"," "*37))
    print("=" * 86)
    mem = input("Do you have ID Member ? [Y/N] : ").upper()
    if mem == "Y":
        id_member = input("Enter ID Member : ")
        for i in range(len(user_list)):
            if id_member in user_list[i]:
                for j in range(len(calculate_list)):
                    calculate_list[j][2] = int(calculate_list[j][2]) - int(calculate_list[j][2]) * 0.15
            else:
                print("ID Member False !")
                print("Please try again")
                    
def receipt() : # ใบเสร็จ
    print("=" * 86)
    print("%s %s %s" % (" "*35,"RECEIPT"," "*39))
    print("=" * 86)
    print("Product Name\t\t\tQuantity\t\t\tPrice")
    for i in range(len(calculate_list)):
        print("%-30s %20s %30s" % (calculate_list[i][0],calculate_list[i][1],calculate_list[i][2]))
    print("=" * 86)
    print("Total Price : %s" % (sum(int(calculate_list[i][2]) for i in range(len(calculate_list)))))
        
# สมัครสมาชิก
# ลบสมาชิก
# เพิ่มจำนวนสินค้า
# แสดงสินค้า
# แสดงสมาชิก
# ขายสินค้า
# คำนวณราคา

def main() :
    choice = 0
    while choice != "7" :
        print("=" * 86)
        print("%s %s %s" % (" "*35,"MAIN MENU"," "*37))
        print("=" * 86)
        print("1. Register")
        print("2. Delete Member")
        print("3. Add Stock Product")
        print("4. Show User")
        print("5. Show Product")
        print("6. Sell Product")
        print("7. Exit")
        print("=" * 86)
        user_lists()
        product_lists()
        choice = input("Enter your choice : ")
        if choice == "1":
            register()
        elif choice == "2":
            delete_member()
        elif choice == "3":
            addstock_product()
        elif choice == "4":
            show_user()
        elif choice == "5":
            show_product()
        elif choice == "6":
            show_product()
            calculate()
            dicount()
            receipt()
        elif choice == "7":
            print("Exit Program")
        else:
            print("Error")



main()