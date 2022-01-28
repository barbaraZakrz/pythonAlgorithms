import sys, time
def zig():
    indent = 0
    indentUpDown =True

    try:

        while True:
            print(' '*indent, end='')
            print("*****")
            time.sleep(0.1)
            if indentUpDown:
                indent = indent + 1
                if indent == 5:
                    indentUpDown = False
            else:
                indent = indent - 1;
                if indent == 0:
                    indentUpDown = True
    except KeyboardInterrupt:
        sys.exit()

print("Hello,", end=' ')
a = input("do you want zigzag?\ntype:")
if a == "yes":
    zig()
else:
    print("ok, bye")