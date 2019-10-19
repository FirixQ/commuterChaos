from math import sqrt

def moveallboids(allboids):
    

    for boid in allboids:
        v1 = rule1(allboids, boid)
        v2 = rule2(allboids, boid)
        v3 = rule3(allboids, boid)

        boid.velocity = vectoradd(vectoradd(boid.Velocity , v1),vectoradd(v2, v3))
        boid.position = boid.position + boid.velocity


def vectoradd(v1, v2): #ronseal
    return (v1[0]+v2[0],v1[1]+v2[1])

def vectorsub(v1, v2): #ronseal
    return (v1[0]-v2[0],v1[1]-v2[1])

def vectormul(v, s): #ronseal
    return (v[0]*s,v[1]*s)

def vectordiv(v, s): #ronseal
    return (v[0]/s,v[1]/s)

def vectormag(v1): # find the magnitude of the vector
    return (sqrt(v1[0]**2 + v1[0]**2))

def rule1(allboids, thisboid):
    totalpos = [0,0]

    for boid in allboids:
        if boid !=thisboid:
            totalpos = vectoradd(boid.position, totalpos)

    totalpos = vectordiv(totalpos, (len(allboids)-1))

    return vectordiv(vectorsub(totalpos, thisboid.position),100)


def rule2(allboids, thisboid):
    c = [0,0]
    for boid in allboids:
        if boid != thisboid:
            if vectormag(vectorsub(boid.position, thisboid.postition)) < 100:
                c = vectorsub(c, vectorsub(boid.position, thisboid.position))
    return c

def rule3(allboids, thisboid):
    totalv = [0,0]
    for boid in allboids:
        if boid != thisboid:
            totalv = vectoradd(totalv, boid.velocity)
    totalv = vectordiv(totalv, len(allboids)-1)
    return vectordiv(vectorsub(totalv, thisboid.velocity), 8) #cc