import os

rightdir = "C:\\Users\\ahamz\\Desktop\\University\\Semester 5\\DevOps"
rightimages = []
for subdir, dirs, files in os.walk(rightdir):
    for file in files:
        rightimages.append(os.path.join(subdir, file))

wrongdir = "C:\\Users\\ahamz\\Desktop\\University\\Semester 5\\DevOps"
wrongimages = []
for subdir, dirs, files in os.walk(wrongdir):
    for file in files:
        wrongimages.append(os.path.join(subdir, file))

print(rightimages)
print(wrongimages)

for i in range(len(rightimages)):
    right_image_dir = rightimages[i]
    wrong_image_dir = wrongimages[i]

    # Do your processing and concatination here