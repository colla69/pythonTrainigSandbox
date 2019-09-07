
import cProfile
import pstats

import re
from timeit import timeit
from collections import defaultdict
from testProj.nester import print_lol, print_tag, get_data_from_dir


cProfile.run("""from testProj.nester import get_data_from_dir
rootDir = '/media/cola/Data/Music/New/'

files_dict, f_count = get_data_from_dir(rootDir)

print( f_count )
""", "restats")

pstats.Stats('restats').sort_stats("tottime").print_stats()
# p.strip_dirs().sort_stats(-1).print_stats()


#
# rootDir = '/media/cola/Data/Music/New/Sing'
# d_count = 0
#
# print ( "start" )
#
# noM = defaultdict(list)
# timeit("""from testProj.nester import get_data_from_dir
# rootDir = '/media/cola/Data/Music/New/Singole/'
#
# files_dict, f_count = get_data_from_dir(rootDir)
#
# print( f_count )
# """)
#
# files_dict, f_count = get_data_from_dir(rootDir)
# print(f_count)

# for key in files_dict:
#    print( (key) +'/')
    #print (files_dict[key][0])

    # if files_dict[key][0] != "":
    #     file = key + '/' + files_dict[key][0]
    #     print_tag(file)
    # break

# print_lol(files_dict)


# for key in files_dict:
#     print(key+"\n")
#     print( files_dict[key] )

# print("\n dirs crawled: " + str(d_count))
# print("\n files crawled: " + str(f_count))
# print('\n discarded files : '+str(d_count))
# print_lol(noM)
# print('\n END discard ')
