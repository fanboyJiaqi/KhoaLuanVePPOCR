import json

# file_path = "/home/phuong/Documents/test/images/Label.txt"

def convert_points(points):
    # conver points from list to set
    new_p = []
    for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]
        new_p.append((x,y))
    return new_p

def read_convert_label_file(path):
    info =[]
    with open(path, 'r', encoding='utf-8') as f:
        content = f.readlines()
        f.close()
    sum=0
    for i in content:
        index  = i.find('[')

        name_img = i[:index]
        name_img = name_img.replace('\t','')
        # properties: properties of image ['transcription': ...., 'points':...]
        properties  = i[index:]
        properties = properties.strip()
        # num_trans: number transcription of image each image
        num_trans = properties.count('transcription')
        index_last = 0
        # find '{' and '}' to cut properties from '{' to '}' then covert it to dict and add by conver_properties
        convert_properties = []
        for i in range(num_trans):
            properties = properties[index_last:]
            index_first = properties.find('{')
            index_last = properties.find('}') + 1
            new_list = properties[index_first:index_last]
            mini_dict = json.loads(new_list)

        #     old_point = mini_dict['points']
        #     new_point = convert_points(old_point)
        #     mini_dict['points'] = new_point

            convert_properties.append(mini_dict)
        info.append([name_img,convert_properties])
        # break

    return info


# info = read_convert_label_file(file_path)
# print(len(info))