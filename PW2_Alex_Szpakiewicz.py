import numpy as np
import matplotlib.pyplot as plt

def Exercice1() :
    mainArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(mainArray.ndim)
    print(mainArray.dtype)

    narrayd1 = np.array([0,0,0,0,0,0,0,0,0])
    narrayd2 = np.array([[0,0,0],[0,0,0],[0,0,0]])
    print(narrayd2.size, narrayd2.ndim, narrayd2.dtype)

    zeroArray = np.zeros_like(mainArray)
    #return an array of zeros with the same shape and type as a given array
    print(zeroArray)
    narray = np.empty([3,3], dtype = int)
    #return a new array of given shape and type, without initializing entries
    print(narray)

    lineArray = np.linspace(1,10,10)
    #return evenly spaced numbers over a specified interval, we controle the number of samples
    print(lineArray)

    arrArray = np.arange(1,10,2)
    #return evenly spaced values within a given interval, we control the step
    print(arrArray)

    randArray = np.random.rand(4)
    randArray1 = np.random.rand(3,3)
    #return random values in a given shape
    print(randArray, randArray.ndim)
    print(randArray1, randArray1.ndim)

def Exercice2():
    mainArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
    sinArray = np.sin(mainArray)
    cosArray = np.cos(mainArray)
    logArray = np.log(mainArray)

    print(mainArray)
    print(sinArray, cosArray, logArray)

    f1 = [sinArray + cosArray]
    print("f1 :", f1)
    f2 = [np.power(cosArray,2)-np.power(sinArray,2)]
    print("f2 :", f2)
    f3 = [np.power(sinArray,2)+ np.power(cosArray,2)]
    print("f3 :", f3)

    nsinArray = [x+1.5 for x in sinArray]
    print("nsinArray :", nsinArray)

    scalar = np.dot(sinArray, cosArray)
    print("scalar :", scalar)
    #return the dot product of two arrays

    vector = np.cross(sinArray, cosArray)
    print("vector :", vector)
    #return the cross product of two arrays


def Exercice3():
    mainArray = np.random.rand(3,3)
    np.savetxt('mainArray.txt', mainArray)
    #save an array to a text file
    np.save('mainArray.npy', mainArray)
    #save an array to a binary file in .npy format
    f0 = open('mainArray.txt', 'r')
    f0bis = np.loadtxt('mainArray.txt')
    f1 = open('mainArray.npy', 'rb')
    f1bis = np.load('mainArray.npy')
    print(f0.read(), f0bis)
    print(f1.read(), f1bis)
    #open is to open the file and loadtxt is to load the data from the file

def Exercice4():
    mainArray = np.loadtxt('monalisa.txt')
    print(mainArray.ndim, mainArray.shape, mainArray.dtype)
    plt.imshow(mainArray)
    plt.show()
    plt.imshow(mainArray, cmap='gray', vmin=0, vmax=255)
    plt.show()

    nmainArray = np.load('monalisa.npy')
    print(nmainArray.ndim, nmainArray.shape, nmainArray.dtype)
    plt.imshow(nmainArray)
    plt.show()

    slcarray = nmainArray[100:500, 200:600]
    plt.imshow(slcarray)
    plt.show()

    pixelatedarray = nmainArray[::10, ::10]
    plt.imshow(pixelatedarray)
    plt.show()
    pixelatedarray = nmainArray[::20, ::20]
    plt.imshow(pixelatedarray)
    plt.show()
    pixelatedarray = nmainArray[::70, ::70]
    plt.imshow(pixelatedarray)
    plt.show()

    rotatearray = np.rot90(nmainArray)
    plt.imshow(rotatearray)
    plt.show()

    mirrorarray = np.fliplr(nmainArray)
    plt.imshow(mirrorarray)
    plt.show()

    modifiedarray = np.load('monalisa.npy')
    modifiedarray[100:500, 200:600] = 255
    plt.imshow(modifiedarray)
    plt.show()
    modifiedarray[100:500, 200:600] = np.random.uniform(0, 255, (400, 400, 3))
    plt.imshow(modifiedarray)
    plt.show()

Exercice4()