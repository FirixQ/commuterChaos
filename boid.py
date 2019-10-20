from math import sqrt

def moveallboids(allboids, map, mousepos = (-1,-1)):

    target = [400,400]

    for boid in allboids:
        vFlock = flock(allboids, boid)
        vSpace = personalSpace(allboids, boid)
        vSpeed = matchSpeed(allboids, boid)
        vConverge = converge(target, boid)
        vBound = boundry(boid)

        if mousepos != (-1,-1):
            vMouse = mouseScatter(mousepos,boid,allboids)
        else:
            vMouse = [0,0]

        boidVelocity = vectoradd(boid.velocity , vFlock, vSpace, vSpeed, vConverge, vBound,vMouse)
        boidVelocity = speedlimit(boidVelocity)
        boidVelocity = collision(boid, map, boidVelocity)
        boidPosition = vectoradd(boid.position,boid.velocity)
        boid.update(boidPosition,boidVelocity)



def vectoradd(*argv): #ronseal
    outv = [0,0] #adds an unlimited number of vectors together
    for arg in argv:
        outv = (outv[0]+arg[0],outv[1]+arg[1])
    return outv

def vectorsub(v1, v2): #ronseal
    return (v1[0]-v2[0],v1[1]-v2[1])

def vectormul(v, s): #ronseal
    return (v[0]*s,v[1]*s)

def vectordiv(v, s): #ronseal
    return (v[0]/s,v[1]/s)

def vectormag(v1): # find the magnitude of the vector
    return (sqrt(v1[0]**2 + v1[1]**2))



# flock together, boid rule1
def flock(allboids, thisboid):
    totalpos = [0,0]

    for boid in allboids:
        if boid !=thisboid:
            totalpos = vectoradd(boid.position, totalpos)

    totalpos = vectordiv(totalpos, (len(allboids)-1))

    return vectordiv(vectorsub(totalpos, thisboid.position),100)

# but not too close, boid rule2
def personalSpace(allboids, thisboid):
    c = [0,0]
    for boid in allboids:
        if boid != thisboid:
            if vectormag(vectorsub(boid.position, thisboid.position)) < 5:
                c = vectorsub(c, vectorsub(boid.position, thisboid.position))
    return c

# match nearby bird speed, boid rule3
def matchSpeed(allboids, thisboid):

    totalv = [0,0]
    for boid in allboids:
        if boid != thisboid:
            totalv = vectoradd(totalv, boid.velocity)
    totalv = vectordiv(totalv, len(allboids)-1)
    return vectordiv(vectorsub(totalv, thisboid.velocity), 8)

def converge(target, thisboid): # tend to place rule
    return vectordiv(vectorsub(target, thisboid.position),50)


def speedlimit(boidvelocity):#this takes the velocity vector and returns it limited to a certain magnitude
    vlim = 20 #this is the speed limit
    if vectormag(boidvelocity) > vlim:
        return vectordiv(boidvelocity,vectormag(boidvelocity))*vlim
    else:
        return boidvelocity

def boundry(boid):
    # bounds
    minX = 0
    maxX = 500
    minY = 0
    maxY = 500

    const = 1

    x = boid.position[0]
    y = boid.position[1]

    resultant = [0,0]

    if x < minX:
        resultant[0] = const
    elif x > maxX:
        resultant[0] = const * -1

    if y < minY:
        resultant[1] = const
    elif y > maxY:
        resultant[1] = const * -1

    return resultant

def collision(boid, map, velo):

    # honestly idk what is going here. it is teleporting stuff about and i dont
    # know why

    x = boid.position[0]
    y = boid.position[1]

    vY = velo[0]
    vX = velo[1]

    for building in map:
        if x >= building.left and (y >= building.top and y <= building.bottom):
            vX *= -1
            boid.position = (building.left - 3, y)
        if x <= building.right and (y >= building.top and y <= building.bottom):
            vX *= -1
            boid.position = (building.right + 3, y)

        if y >= building.top and (x >= building.left and x <= building.right):
            vY *= -1
            boid.position = (x, building.top + 3)
        if y <= building.bottom and (x >= building.left and x <= building.right):
            vY *= -1
            boid.position = (x, building.bottom - 3)

    return (vX,vY)

def scatter(allboids,thisboid):
    pushawaymul = -2
    return (0,0) #vectormul(flock(allboids,thisboid),2*pushawaymul)


def avoid(target,thisboid):
    pushawaymul = -0.75
    return vectormul(converge(target,thisboid),pushawaymul)



def mouseScatter(mousepos, thisboid,allboids):
    return(vectoradd(scatter(allboids,thisboid),avoid(mousepos,thisboid)))
