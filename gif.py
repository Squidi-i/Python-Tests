import imageio.v3 as iio

filenames = ['blue-smile.png', 'blue-hands.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('emoji.gif', images, duration = 500, loop = 0)
