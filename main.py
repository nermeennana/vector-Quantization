from PIL import Image
import numpy as np


# Divide the image into multiple pieces

def divideImage(height, width, blockSize, img):
    blockNum = 28 / blockSize
    pTRow = 0
    pTCol = 0
    XDash = 0
    YDash = 0
    featureVector = []
    for i in range(1, int(blockSize / 2) + 1):
        for j in range(1, int(blockSize / 2) + 1):
            for pTRow in range(i * blockSize):
                print("\n")
                for pTCol in range(j * blockSize):
                    print(img[pTRow][pTCol])
                    print(" ")
            pTCol = j * blockSize
            pTRow = 0
            # featureVector.append(XDash)
            # featureVector.append(YDash)
    # return featureVector


x_Axis = [0, -1, -1, -1, 0, 1, 1, 1]
y_Axis = [1, 1, 0, -1, -1, -1, 0, 1]

total = 0


def valid(x, y):
    return 0 <= x <= 28 and 0 <= y <= 28


def modifyFay(f):
    if f == 360:
        f = 0
    elif f == 45:
        f = 2
    elif f == 90:
        f = 3
    elif f == 135:
        f = 4
    elif f == 180:
        f = 5
    elif f == 225:
        f = 6
    if f == 270:
        f = 7
    return f


def GLCM(fay, img, n, step=0):
    matrix = [[0 for k in range(n)] for m in range(n)]
    fay = modifyFay(fay)
    for i in range(n):
        for j in range(n):
            for k in range(28):
                for m in range(27):
                    k = k + x_Axis[fay]
                    m = m + y_Axis[fay]
                    if valid(k, m) and img[k][m] == i and img[k][m + 1] == j:
                        matrix[i][j] += 1

    return matrix


vectorsList = []
imgPath = 'flower.jpg'
img = Image.open(imgPath).convert("L")
print(type(img))
# converts image to numpy array
imgArr = np.asarray(img)
print(type(imgArr), imgArr.shape)
print(np.min(imgArr), np.max(imgArr))  # 0 to 255 uint8
savePath = 'myFlower.png'
decodedImg = Image.fromarray(imgArr)
decodedImg.save(savePath)  # will save it as gray image

imgWidth = img.width
imgLen = img.height

m = GLCM(0, imgArr, np.max(imgArr))
print(m)
