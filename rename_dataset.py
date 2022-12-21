import os
import glob

# 获取图片文件夹中的文件名列表
image_filenames = os.listdir('images')

# 按照图片文件名的字典序排序
image_filenames.sort()

# 遍历文件名列表，修改文件名
for i, filename in enumerate(image_filenames):
    # 获取图片文件的文件名（不包括扩展名）
    image_name, image_ext = os.path.splitext(filename)

    # 获取对应的 XML 文件名
    xml_filename = image_name + '.xml'

    # 修改图片文件名
    os.rename(os.path.join('images', filename), os.path.join('images', '{}{}'.format(i+1, image_ext)))

    # 修改对应的 XML 文件名
    os.rename(os.path.join('annotations', xml_filename), os.path.join('annotations', '{}{}'.format(i+1, '.xml')))
