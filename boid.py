from math import sqrt,ceil

def moveallboids(allboids):

    target = [400,400]

    for boid in allboids:
        v1 = rule1(allboids, boid)
        v2 = rule2(allboids, boid)
        v3 = rule3(allboids, boid)
        v4 = rule4(target, boid)
        vBound = boundry(boid)

        boidVelocity = speedlimit(boidVelocity)
        boidPosition = vectoradd(boid.position,boid.velocity)
        boid.update(boidPosition,boidVelocity)



def vectoradd(v1, v2): #ronseal
    return (v1[0]+v2[0],v1[1]+v2[1])

def vectorsub(v1, v2): #ronseal
    return (v1[0]-v2[0],v1[1]-v2[1])

def vectormul(v, s): #ronseal
    return (v[0]*s,v[1]*s)

def vectordiv(v, s): #ronseal
    return (v[0]/s,v[1]/s)

def vectormag(v1): # find the magnitude of the vector
    return (sqrt(v1[0]**2 + v1[1]**2))

def vectorbigadd(*argv):
    outv = [0,0]
    for arg in argv:
        outv = vectoradd(outv, arg)
    return outv


# flock together
def rule1(allboids, thisboid):
    totalpos = [0,0]

    for boid in allboids:
        if boid !=thisboid:
            totalpos = vectoradd(boid.position, totalpos)

    totalpos = vectordiv(totalpos, (len(allboids)-1))

    return vectordiv(vectorsub(totalpos, thisboid.position),100)

def rule2(allboids, thisboid): # personal space rule
    c = [0,0]
    for boid in allboids:
        if boid != thisboid:
            if vectormag(vectorsub(boid.position, thisboid.position)) < 5:
                c = vectorsub(c, vectorsub(boid.position, thisboid.position))
    return c
# but not too close
def rule2(allboids, thisboid):
    c = [0,0]
    for boid in allboids:
        if boid != thisboid:
            if vectormag(vectorsub(boid.position, thisboid.position)) < 5:
                c = vectorsub(c, vectorsub(boid.position, thisboid.position))
    return c

# match nearby bird speed
def rule3(allboids, thisboid):

    totalv = [0,0]
    for boid in allboids:
        if boid != thisboid:
            totalv = vectoradd(totalv, boid.velocity)
    totalv = vectordiv(totalv, len(allboids)-1)
    return vectordiv(vectorsub(totalv, thisboid.velocity), 8)

def rule4(target, thisboid): # tend to place rule
    return vectordiv(vectorsub(target, thisboid.position),100)

def speedlimit(boidvelocity):#this takes the velocity vector and returns it limited to a certain magnitude
    vlim = 10 #this is the speed limit
    if vectormag(boidvelocity) > vlim:
        return vectordiv(boidvelocity,vectormag(boidvelocity))*vlim
    else:
        return boidvelocity

def tendtoplace(b, pos):
    return vectordiv(vectorsub(pos,b),10)

def tendfromplace(b,pos):
    return(vectormul(tendtoplace(b,pos),-0.1))

    if boid.position[1] < minY:
        resultant[1] = const
    elif boid.position[1] > maxY:
        resultant[1] = const * -1

    return resultant
