
#ZED
import platform ,os , sys 
from time import sleep
def Clear():
    if platform.uname()[0] == "Windows":
        os.system("cls")
    else:
        os.system("clear")
def Banner():
    print("""\033[32m
  ()*|+&^+(&^%$#@!~+_)+(Z&ED#@+_)(*&^%$#@)()
  ()                                      ()
  ()                 None                 () 
  ()                                      ()
  ()@#_)!@Z$%^&*()_)Z_)(*&^%$@#Z%^&)#$%^&())
  \033[37m""")
def Menu():
    print("""  (1) Start building tools
  (2) Help 
  (3) Developer
  (4) Exit\n""")
def TVA():
    try:
        Clear()
        Banner()
        Menu()
        op = input("  A:\TVA> ")
        if op == "1":
            Clear()
            Banner()
            ToolCrate()
        elif op == "2":
            Clear()
            Banner()
            Help()
        elif op == "3":
            Clear()
            Banner()
            dev()
        elif op == "4":
            Clear()
            sys.exit()
        elif op == "":
            Clear()
            Banner()
            print("  Data Not Fouad !!")
            input("  Back To Menu (Press Enter...)")
    except KeyboardInterrupt:
        Clear()
        sys.exit() 
def ToolCrate():
    NameTool = input("  Enter Tool Name:")
    if NameTool == '':
        Clear()
        Banner()
        print("  Data Not Found Try again..!!")
        sys.exit()
    print("  Select Color Tool:")
    print("  1-Red    2-Green    3-Yellow    4-Blue  5-White")
    ColorTool = input("  Select Color Tool (Defult=White)")
    red = """print("\033[31m")"""
    green = """print("\033[32m")"""
    yellow = """print("\033[33m")"""
    blue = """print("\033[34m")"""
    white = """print("\033[37m")"""
    color = """"""
    if ColorTool == "1":
        color = red
    elif ColorTool == "":
        Clear()
        Banner()
        print("  Data Not Found Try again..!!")
        sys.exit()
    elif ColorTool == "2":
        color = green
    elif ColorTool == "3":
        color = yellow
    elif ColorTool == "4":
        color = blue
    elif ColorTool == "5":
        color = white
    elif ColorTool == "":
        color = white
    ClearMethod = input("  Do You Want To Add Screen Cleaner Method In Tool (yes/no defult=yes):")
    c_m = ""
    c_m_ = """#Function Clear Terminal
def Clear():
    if platform.uname()[0] == "Windows":
        os.system("cls")
    else:
        os.system("clear")"""
    c_M_c = """#Function Clear Terminal
def Clear():
    print("")"""
    if ClearMethod == 'yes' or 'YES' or 'Yes':
        c_m = c_m_
    elif ClearMethod == 'no' or 'NO' or 'No':
        c_m = c_M_c
    elif ClearMethod == '':
        c_m = c_m_
    BannerMethod = input("  Do You Want To Add Banner Tool Method In Tool (yes/no defult=yes):")
    ba = """#Function Banner Tool
def Banner():
    """+color+"""
    print("")
    print("  ############################################################")
    print("  |                                                          |")
    print("  |                                                          |")
    print("  |                        'Bannner'                         |")
    print("  |                                                          |")
    print("  |                                                          |")
    print("  ############################################################")
    print("")"""
    bb = """#Function Banner Tool
def Banner():
    print("")"""
    bc = """"""
    if BannerMethod == 'yes' or 'YES' or 'Yes':
        bc = ba
    elif BannerMethod == 'no' or 'NO' or 'No':
        bc = bb
    elif BannerMethod == '':
        bc = ba
    MenuTool = input("  Enter tools menu numbers (1 to 6):")
    sleep(1)
    Menu_1 = """
#Function Menu Tool
def Menu():
    print("  [1] Enter Method")
#Function Main Tool
def Main():
    try:
        Clear()
        Banner()
        Menu()
        print("")
        op = input("  Input> ")
        if op == "1":
            Clear()
            Banner()
            Method_1()
        elif op == "":
            Clear()
            Banner()
            print("  Data Not Fouad !!")
            input("  Back To Menu (Press Enter...)")
    except KeyboardInterrupt:
        Clear()
        sys.exit()
#Functions Methods
def Method_1():
    print("  Method (1)")
    input("  Back To Menu (Press Enter...)")
    # Write Mehtod 1
#Loop play Tools
while True:
    Main()
""" 
    Menu_2 = """
#Function Menu Tool
def Menu():
    print("  [1] Enter Method")
    print("  [2] Enter Method")
#Function Main Tool
def Main():
    try:
        Clear()
        Banner()
        Menu()
        print("")
        op = input("  Input> ")
        if op == "1":
            Clear()
            Banner()
            Method_1()
        elif op == "2":
            Clear()
            Banner()
            Method_2()
        elif op == "":
            Clear()
            Banner()
            print("  Data Not Fouad !!")
            input("  Back To Menu (Press Enter...)")
    except KeyboardInterrupt:
        Clear()
        sys.exit()
#Functions Methods
def Method_1():
    print("  Method (1)")
    input("  Back To Menu (Press Enter...)")
    # Write Mehtod 1
def Method_2():
    print("  Method (2)")
    input("  Back To Menu (Press Enter...)")
    # Write Mehtod 2
#Loop play Tools
while True:
    Main()"""
    Menu_3 = """
#Function Menu Tool
def Menu():
    print("  [1] Enter Method")
    print("  [2] Enter Method")
    print("  [3] Enter Method")
#Function Main Tool
def Main():
    try:
        Clear()
        Banner()
        Menu()
        print("")
        op = input("  Input> ")
        if op == "1":
            Clear()
            Banner()
            Method_1()
        elif op == "2":
            Clear()
            Banner()
            Method_2()
        elif op == "3":
            Clear()
            Banner()
            Method_3()
        elif op == "":
            Clear()
            Banner()
            print("  Data Not Fouad !!")
            input("  Back To Menu (Press Enter...)")
    except KeyboardInterrupt:
        Clear()
        sys.exit()
#Functions Methods
def Method_1():
    print("  Method (1)")
    input("  Back To Menu (Press Enter...)")
    # Write Mehtod 1
def Method_2():
    print("  Method (2)")
    input("  Back To Menu (Press Enter...)")
    # Write Mehtod 2
def Method_3():
    print("  Method (3)")
    input("  Back To Menu (Press Enter...)")
    # Write Mehtod 3
#Loop play Tools
while True:
    Main()"""
    Menu_4 = """
    #Function Menu Tool
def Menu():
    print("  [1] Enter Method")
    print("  [2] Enter Method")
    print("  [3] Enter Method")
    print("  [4] Enter Method")
#Function Main Tool
def Main():
    try:
        Clear()
        Banner()
        Menu()
        print("")
        op = input("  Input> ")
        if op == "1":
            Clear()
            Banner()
            Method_1()
        elif op == "2":
            Clear()
            Banner()
            Method_2()
        elif op == "3":
            Clear()
            Banner()
            Method_3()
        elif op == "4":
            Clear()
            Banner()
            Method_4()
        elif op == "":
            Clear()
            Banner()
            print("  Data Not Fouad !!")
            input("  Back To Menu (Press Enter...)")
    except KeyboardInterrupt:
        Clear()
        sys.exit()
#Functions Methods
def Method_1():
    print("  Method (1)")
    input("  Back To Menu (Press Enter...)")
    # Write Mehtod 1
def Method_2():
    print("  Method (2)")
    input("  Back To Menu (Press Enter...)")
    # Write Mehtod 2
def Method_3():
    print("  Method (3)")
    input("  Back To Menu (Press Enter...)")
    # Write Mehtod 3
def Method_4():
    print("  Method (4)")
    input("  Back To Menu (Press Enter...)")
    # Write Mehtod 4
#Loop play Tools
while True:
    Main()"""
    Menu_5 = """
#Function Menu Tool
def Menu():
    print("  [1] Enter Method")
    print("  [2] Enter Method")
    print("  [3] Enter Method")
    print("  [4] Enter Method")
    print("  [5] Enter Method")
#Function Main Tool
def Main():
    try:
        Clear()
        Banner()
        Menu()
        print("")
        op = input("  Input> ")
        if op == "1":
            Clear()
            Banner()
            Method_1()
        elif op == "2":
            Clear()
            Banner()
            Method_2()
        elif op == "3":
            Clear()
            Banner()
            Method_3()
        elif op == "4":
            Clear()
            Banner()
            Method_4()
        elif op == "5":
            Clear()
            Banner()
            Method_5()
        elif op == "":
            Clear()
            Banner()
            print("  Data Not Fouad !!")
            input("  Back To Menu (Press Enter...)")
    except KeyboardInterrupt:
        Clear()
        sys.exit()
#Functions Methods
def Method_1():
    print("  Method (1)")
    input("  Back To Menu (Press Enter...)")
    # Write Mehtod 1
def Method_2():
    print("  Method (2)")
    input("  Back To Menu (Press Enter...)")
    # Write Mehtod 2
def Method_3():
    print("  Method (3)")
    input("  Back To Menu (Press Enter...)")
    # Write Mehtod 3
def Method_4():
    print("  Method (4)")
    input("  Back To Menu (Press Enter...)")
    # Write Mehtod 4
def Method_5():
    print("  Method (5)")
    input("  Back To Menu (Press Enter...)")
    # Write Mehtod 5
#Loop play Tools
while True:
    Main()"""
    Menu_6 = """
#Function Menu Tool
def Menu():
    print("  [1] Enter Method")
    print("  [2] Enter Method")
    print("  [3] Enter Method")
    print("  [4] Enter Method")
    print("  [5] Enter Method")
    print("  [6] Enter Method")
#Function Main Tool
def Main():
    try:
        Clear()
        Banner()
        Menu()
        print("")
        op = input("  Input> ")
        if op == "1":
            Clear()
            Banner()
            Method_1()
        elif op == "2":
            Clear()
            Banner()
            Method_2()
        elif op == "3":
            Clear()
            Banner()
            Method_3()
        elif op == "4":
            Clear()
            Banner()
            Method_4()
        elif op == "5":
            Clear()
            Banner()
            Method_5()
        elif op == "6":
            Clear()
            Banner()
            Method_6()
        elif op == "":
            Clear()
            Banner()
            print("  Data Not Fouad !!")
            input("  Back To Menu (Press Enter...)")
    except KeyboardInterrupt:
        Clear()
        sys.exit()
#Functions Methods
def Method_1():
    print("  Method (1)")
    input("  Back To Menu (Press Enter...)")
    # Write Mehtod 1
def Method_2():
    print("  Method (2)")
    input("  Back To Menu (Press Enter...)")
    # Write Mehtod 2
def Method_3():
    print("  Method (3)")
    input("  Back To Menu (Press Enter...)")
    # Write Mehtod 3
def Method_4():
    print("  Method (4)")
    input("  Back To Menu (Press Enter...)")
    # Write Mehtod 4
def Method_5():
    print("  Method (5)")
    input("  Back To Menu (Press Enter...)")
    # Write Mehtod 5
def Method_6():
    print("  Method (6)")
    input("  Back To Menu (Press Enter...)")
    # Write Mehtod 6
#Loop play Tools
while True:
    Main()"""
    tooltext = """"""
    if MenuTool == "1":
        tooltext = Menu_1
    elif MenuTool == "2":
        tooltext = Menu_2
    elif MenuTool == "3":
        tooltext = Menu_3
    elif MenuTool == "4":
        tooltext = Menu_4
    elif MenuTool == "5":
        tooltext = Menu_5
    elif MenuTool == "6":
        tooltext = Menu_6
    elif MenuTool == "":
        Clear()
        Banner()
        print("  Data Not Found Try again..!!")
        sys.exit()
    tool = """# Codeed ZED Tools
#import libery 
import platform ,os , sys
"""+c_m+"""
"""+bc+"""
"""+tooltext+"""
"""
    print("  Please Wite(Loading..)")
    sleep(5)
    print("  Your Tool Created Succsesfully")
    input("  Back To Menu (Press Enter...)")
    Tool = open(NameTool+".py","w")
    Tool.write(tool)
def Help():
    try:
        print("""  Tool Developed With Python 3.9.5 Version
  Backup section : https://t.me/Deusnegro""")
        try:
            input("  Back To Menu (Press Enter...)") 
        except:
            print("")
            sys.exit()
    except KeyboardInterrupt:
        Clear()
        Banner()
        sys.exit()
def dev():
    try:
        print("""  Developer : OmidRanjbar(Zed)
  Contact Us : @Deusnegro
  My Team ;) : @Zedla_sec
  My Channel : @blackhatinfo 
  Web site : wwww.zelda_sec.ir""")
        try:
            input("  Back To Menu (Press Enter...)") 
        except:
            print("")
            sys.exit()
    except KeyboardInterrupt:
        Clear()
        Banner()
        sys.exit()
while True:
    TVA()
