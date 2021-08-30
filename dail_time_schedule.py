day=input("enter day:")
time=input("enter time:")
if day=="monday":
    if time=="breakfast":
        print("poha")
    elif time=="lunch":
        print("rajma chawal")
    else:
        print("pulav")
elif day=="tuesday":
    if time=="breakfast":
        print("alu puri")
    elif time=="lunch":
        print("chicken chawal")
    else:
        print("roti sabji")
elif day=="wednesday":
    if time=="breakfast":
        print("pasta")
    elif time=="lunch":
        print("gawar roti")
    else:
        print("dal chawal")
elif day=="thursday":
    if time=="breakfast":
        print("shabudana usal")
    elif time=="lunch":
        print("panir")
    else:
        print("special pulav")
elif day=="friday":
    if time=="breakfast":
        print("mataki chiwada")
    elif time=="lunch":
        print("shimla mirch")
    else:
        print("palak varan")
elif day=="saturday":
    if time=="breakfast":
        print("paratha")
    elif time=="lunch":
        print("kobi")
    else:
        print("baigan roti")
else:
    print("kadi bhat")