berserk=5
archer=10
soldat=0
atk=200
#status='defend'
status='ataka'
if status=='ataka' and berserk>archer:
    atk=atk+(atk/100*(berserk-archer))
    print(atk)
elif status=='ataka' and berserk<archer:
    sum=(archer-berserk)
    if soldat<sum:
        atk=atk-(atk/100*(sum-soldat))
        print(atk)
    else:
        print(atk)
elif status=='defend' and berserk>archer:
    sum=(berserk-archer)
    if soldat<sum:
            atk=atk-(atk/100*(sum-soldat))
            print(atk)
    else:
        print(atk)
elif status=='defend' and berserk<archer:
    atk=atk+(atk/100*(archer-berserk))
    print(atk)