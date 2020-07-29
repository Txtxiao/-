ques = input()
questNum = int(ques)

for quest in range(questNum):
    inp = input()
    ns = inp.split(' ')
    t = ns[0]
    n = int(t)
    start = ns[1]
    s2 = input()
    s = s2.split(' ')

    graph = []
    for i in range(n):
        s3 = input()
        s1 = s3.split(' ')
        start1 = s1[0]
        for k in range(1, n + 1):
            if s1[k] == '1':
                if not (start1, s[k - 1]) in graph:
                    graph.append((start1, s[k - 1]))

    nex = start
    while len(graph) > 0:
        for i in range(len(graph)):
            if graph[i][0] == nex:
                print(graph[i][0], end=' ')
                nex = graph[i][1]
                del graph[i]
                break

    print()
