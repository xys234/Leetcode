
input = [[33,44],[85,95],[20,37],[91,100],[89,100],[77,87],[80,95],[42,61],[40,50],[85,99],[74,91],
         [70,82],[5,17],[77,89],[16,26],[21,31],[30,43],[96,100],[27,39],[44,55],[15,34],[85,99],
         [74,93],[84,94],[82,94],[46,65],[31,49],[58,73],[86,99],[73,84],[68,80],[5,18],[75,87],
         [88,100],[25,41],[66,79],[28,41],[60,70],[62,73],[16,33]]


output =   [True,True,True,True,False,True,False,True,False,False,False,True,True,False,True,False,False,True,False,True,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,True,False,False]


expected = [True,True,True,True,False,True,False,True,False,False,False,True,True,False,True,False,False,True,False,True,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False]


for j, (i, o, e) in enumerate(zip(input, output, expected)):
    if o != e:
        print(j, i, o, e)
        break