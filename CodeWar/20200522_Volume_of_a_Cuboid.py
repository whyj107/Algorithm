# 문제
# Volume of a Cuboid
# Bob needs a fast way to calculate the volume of a cuboid with three values:
# length, width and the height of the cuboid.
# Write a function to help Bob with this calculation.

# My Code
def getVolumeOfCubiod(length, width, height):
    return length * width * height

if __name__ == '__main__':
    print(getVolumeOfCubiod(1, 2, 2), 4)
    print(getVolumeOfCubiod(6.3, 2, 5), 63)