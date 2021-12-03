import sys
with open(sys.argv[1]) as data: data_dict, dataList = {}, [x.split(":") for x in data.read().splitlines()]
for archive in dataList: data_dict[archive[0]] = str(archive[1])
for i in sys.argv[2].split(","):
    try: print("{},University: {}".format(i, data_dict[i]))
    except: print("No record '{}' was found".format(i))
