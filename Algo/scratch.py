
input = [[69,78],[81,86],[80,87],[58,66],[40,46],[81,88],[40,47],[18,25],[52,59],[80,88],[58,63],[15,21],[79,87],[77,83],[9,14],[67,76],[39,44],[36,45],[11,20],[61,69],[51,60],[49,57],[48,53],[2,8],[8,15],[49,57],[8,16],[42,51],[94,100],[44,50],[1,9],[69,78],[47,53],[98,100],[56,62],[26,31],[3,9],[68,75],[85,92],[52,57],[51,59],[18,26],[60,65],[92,99],[90,98],[89,97],[39,44],[31,39],[90,96],[44,49],[44,49],[47,54],[24,32],[59,68],[29,34],[38,43],[3,8],[98,100],[48,57],[19,24],[65,71],[20,29],[18,23],[67,76],[78,86],[43,48],[30,39],[49,56],[48,56],[84,91],[13,18],[96,100],[31,36],[1,8],[90,97],[96,100],[20,28],[45,52],[1,6],[13,22]]


output = [True,True,True,True,True,False,True,True,True,False,False,True,False,False,True,True,False,False,False,True,False,True,False,True,True,False,False,False,True,False,False,False,False,True,False,True,True,False,False,False,False,False,False,False,True,False,False,True,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
expected = [True,True,True,True,True,False,True,True,True,False,False,True,False,False,True,True,False,False,False,True,False,True,False,True,True,False,False,False,True,False,True,False,False,True,False,True,False,False,False,False,False,False,False,False,True,False,False,True,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
for j, (i, o, e) in enumerate(zip(input, output, expected)):
    if o != e:
        print(j, i, o, e)
        break