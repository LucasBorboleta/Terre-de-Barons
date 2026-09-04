# -*- coding: utf-8 -*-
"""
Simulations for tuning parameters of the boardgame "Les Marches : Escarmouche"
"""

import copy
import random
import statistics

    
print()
print("prepare data: ...")

hexagon_count = 9

hexagon_names = set([ hexagon_index + 1 for hexagon_index in range(hexagon_count)])

hexagon_adjacents = {}

hexagon_adjacents[1] = set([2])
hexagon_adjacents[2] = set([1, 3])
hexagon_adjacents[3] = set([2, 4])
hexagon_adjacents[4] = set([3, 5])
hexagon_adjacents[5] = set([4, 6])
hexagon_adjacents[6] = set([5, 7])
hexagon_adjacents[7] = set([6, 8])
hexagon_adjacents[8] = set([7, 9])
hexagon_adjacents[9] = set([8])

assert set(hexagon_adjacents.keys()) == hexagon_names

for (name1, adjacents1) in hexagon_adjacents.items():
    assert name1 not in adjacents1
    for name2 in adjacents1:
        assert name2 in hexagon_names
        assert name1 in hexagon_adjacents[name2]
        
print()
print(f"hexagon_names = {hexagon_names}")

print()
print(f"hexagon_adjacents = {hexagon_adjacents}")
    
print()
print("prepare data: done")


def compute_distance_occurrences(adjacents):
    
    adjacents_dict = compute_distances(adjacents)
                       
    distances = []
    points = adjacents.keys()
    for x in points:
        for y in points:
            if x > y:
                distances.append(adjacents_dict[(x, y)])
                
    return distances



def compute_distances(adjacents):
    
    # partition = compute_connex_partition(adjacents)
    # assert len(partition) == 1
    
    points = adjacents.keys()

    adjacents_dict = {}
    
    for x in points:
        for y in points:
            adjacents_dict[(x, y)] = None
    
    for x in points:
        adjacents_dict[(x, x)] = 0

    for x in points:
        for y in adjacents[x]:
            adjacents_dict[(x, y)] = 1
            adjacents_dict[(y, x)] = 1
            
    has_new_dxy = True
    while has_new_dxy:
        has_new_dxy = False
        for x in points:
            for y in points:
                if x > y:
                    if adjacents_dict[(x, y)] is None:
                        has_new_dxy = True
                        for z in points:
                            if z != x and z != y and adjacents_dict[(x, z)] is not None and adjacents_dict[(z, y)] is not None:
                                dxy = adjacents_dict[(x, z)] + adjacents_dict[(z, y)]
                                adjacents_dict[(x, y)] = dxy
                                adjacents_dict[(y, x)] = dxy
                                break
            
    has_new_dxy = True
    while has_new_dxy:
        has_new_dxy = False
        for x in points:
            for y in points:
                if x > y:
                    dxy = adjacents_dict[(x, y)]
                    for z in points:
                        if z != x and z != y:
                            new_dxy = adjacents_dict[(x, z)] + adjacents_dict[(z, y)]
                            if new_dxy < dxy:
                                has_new_dxy = True
                                dxy = new_dxy
                    adjacents_dict[(x, y)] = dxy
                    adjacents_dict[(y, x)] = dxy
                        
    return adjacents_dict


def compute_connex_partition(adjacents):
    partition = list()
    
    points = list(adjacents.keys())
    points.sort()
    
    minimal_points = {}
    for x in points:
        minimal_points[x] = min([x] + list(adjacents[x]))
        
    new_min_found = True
    while new_min_found: 
        new_min_found = False
        
        for x in points:
            min_x = minimal_points[x]
            
            new_min_x_found = False
            
            for y in adjacents[x]:
                if minimal_points[y] < min_x:
                    new_min_x_found = True
                    min_x = minimal_points[y]
                    
            if new_min_x_found:
                new_min_found = True
                minimal_points[x] = min_x
                for y in adjacents[x]:
                    minimal_points[y] = min_x               

    class_dict = {x:set() for x in minimal_points.values()}
    for x in points:
        class_dict[minimal_points[x]].add(x)
        
    for class_set in class_dict.values():
        if len(class_set) != 0:
            class_list = list(class_set)
            class_list.sort(key=int)
            partition.append(class_list)
    
    return partition


    
def make_statistics_on_partition(mountain_count=0, test_count=100):

    print()
    print("make_statistics_on_partition: ...")
    
    partition_size_sample = []
    partition_multiparts_count = 0
    
    for test_index in range(test_count):
        
        free_set = set(hexagon_names)
        mountain_set = set(random.sample(list(free_set), mountain_count))
        free_set = free_set - mountain_set
        assert len(free_set) == len(hexagon_names) - mountain_count
        
        adjacents = {}
        for (x, x_set) in hexagon_adjacents.items():
            if x not in mountain_set:
                new_x_set = set()
                for y in x_set:
                    if y not in mountain_set:
                        new_x_set.add(y)
                
                adjacents[x] = new_x_set
        
        partition = compute_connex_partition(adjacents)
        partition_size_sample.append(len(partition)) 
        
        if len(partition) > 1:
            partition_multiparts_count += 1
            print()
            print(f"test_index = {test_index}") 
            print(f"mountain_set = {mountain_set}") 
            for (part_index, part) in enumerate(partition):
                print(f"part {part_index} of length {len(part)} = {part}")      
        
                
    print()
    print(f"--- mountain_count: {mountain_count} ---")
    print(f"    partition_multiparts_count = {partition_multiparts_count} ; {partition_multiparts_count/test_count*100:.1f}%")
    print(f"    count = {len(partition_size_sample)}")
    print(f"     mode = {statistics.mode(partition_size_sample)}")
    print(f"     mean = {statistics.mean(partition_size_sample):.1f}")
    print(f"quartiles = {statistics.quantiles(partition_size_sample, n=4)}")
    print(f"  deciles = {statistics.quantiles(partition_size_sample, n=10)}")
    print(f"      min = {min(partition_size_sample)}")
    print(f"      max = {max(partition_size_sample)}")
 
    
    print()
    print("make_statistics_on_partition: done")

    
def make_statistics_on_distances(mountain_count=0, test_count=100_000):

    print()
    print("make_statistics_on_distances: ...")
    
    distance_mean_sample = []
    distance_std_sample = []
    distance_q25_sample = []
    distance_q50_sample = []
    distance_q75_sample = []
    distance_q90_sample = []
    distance_max_sample = []

    
    for test_index in range(test_count):
        
        free_set = set(hexagon_names)
        mountain_set = set(random.sample(list(free_set), mountain_count))
        free_set = free_set - mountain_set
        assert len(free_set) == len(hexagon_names) - mountain_count
        
        adjacents = {}
        for (x, x_set) in hexagon_adjacents.items():
            if x not in mountain_set:
                new_x_set = set()
                for y in x_set:
                    if y not in mountain_set:
                        new_x_set.add(y)
                
                adjacents[x] = new_x_set
                
                    
        partition = compute_connex_partition(adjacents)
        if len(partition) > 1:
            continue
        
        distances = compute_distance_occurrences(adjacents)

        distance_max_sample.append(max(distances))     
        distance_mean_sample.append(statistics.mean(distances))       
        distance_std_sample.append(statistics.stdev(distances))      
        distance_q25_sample.append(statistics.quantiles(distances, n=4)[0])       
        distance_q50_sample.append(statistics.quantiles(distances, n=4)[1])       
        distance_q75_sample.append(statistics.quantiles(distances, n=4)[-1])       
        distance_q90_sample.append(statistics.quantiles(distances, n=10)[-1])       
                
    print()
    print(f"--- mountain_count: {mountain_count} ---")
    print(f"         count  = {len(distance_mean_sample)}")
    print(f"   mean of max  = {statistics.mean(distance_max_sample):.1f}")
    print(f"   mean of mean = {statistics.mean(distance_mean_sample):.1f}")
    print(f"   mean of std  = {statistics.mean(distance_std_sample):.1f}")
    print(f"   mean of q25  = {statistics.mean(distance_q25_sample):.1f}")
    print(f"   mean of q50  = {statistics.mean(distance_q50_sample):.1f}")
    print(f"   mean of q75  = {statistics.mean(distance_q75_sample):.1f}")
    print(f"   mean of q90  = {statistics.mean(distance_q90_sample):.1f}")
 
    print()
    print("make_statistics_on_distances: done")
       

def make_statistics_on_donjon_count(mountain_count=0, test_count=100_000):
    
    print()
    print("make_statistics_on_donjon_count: ...")
    
    donjon_count_sample = []
        
    min_donjon_set = None
    max_donjon_set = None
    five_donjon_set = None

    for test_index in range(test_count):
        
        free_set = set(hexagon_names)
        donjon_set = set()

        mountain_set = set(random.sample(list(free_set), mountain_count))
        free_set = free_set - mountain_set
        assert len(free_set) == len(hexagon_names) - mountain_count
        
        while len(free_set) != 0:
            name = random.choice(list(free_set))
            donjon_set.add(name)
            free_set.remove(name)
            free_set = free_set - hexagon_adjacents[name]
            
        donjon_count_sample.append(len(donjon_set))
             
        if min_donjon_set is None:
            min_donjon_set = copy.copy(donjon_set)
            
        if max_donjon_set is None:
            max_donjon_set = copy.copy(donjon_set)
            
        if len(donjon_set) < len(min_donjon_set):
            min_donjon_set = copy.copy(donjon_set)
            
        if len(donjon_set) > len(max_donjon_set):
            max_donjon_set = copy.copy(donjon_set)
        
        if len(donjon_set) == 5 and five_donjon_set is None:
            five_donjon_set = copy.copy(donjon_set)
                
    print()
    print(f"--- mountain_count: {mountain_count} ---")
    print(f"    count = {len(donjon_count_sample)}")
    print(f"     mode = {statistics.mode(donjon_count_sample)}")
    print(f"     mean = {statistics.mean(donjon_count_sample):.1f}")
    print(f"quartiles = {statistics.quantiles(donjon_count_sample, n=4)}")
    print(f"  deciles = {statistics.quantiles(donjon_count_sample, n=10)}")
    print(f"      min = {min(donjon_count_sample)} ; donjons = {sorted(min_donjon_set)}")
    print(f"      max = {max(donjon_count_sample)} ; donjons = {sorted(max_donjon_set)}")
    print(f"        5 = donjons = {sorted(five_donjon_set)}")            
        
    print()
    print("make_statistics_on_donjon_count: done")

           

def make_statistics_on_points(mountain_count=0, player_count=2, with_diversity=False, diversity_shift=0, test_count=100_000, ranking=False):
    
    print()
    print("make_statistics_on_points: ...")

    if True:
        # Four almost equal flavors
        point_system = {}
        point_system["T1"]       = (1, 3)
        point_system["T2"]       = (2, 3)
        point_system["T3"]       = (3, 3)
        point_system["T4"]       = (4, 3)
    
    total_occurences = 0
    hexagon_points_list = []
    for (key, (points, occurences)) in point_system.items():
        print(f"{key}: #{occurences} times {points} points")
        total_occurences += occurences
        hexagon_points_list += [points for _ in range(occurences)]
        
    assert total_occurences > len(hexagon_names)
    assert len(hexagon_points_list) > len(hexagon_names)
    print()
    print(f"total points = {sum(hexagon_points_list)}")
    print(f"mean points = {statistics.mean(hexagon_points_list)}")

    
    points_sample = []
    player_points_sample = {player_index:[] for player_index in range(player_count)}

    for test_index in range(test_count):
        
        free_set = set(hexagon_names)
        donjon_set = set()

        mountain_set = set(random.sample(list(free_set), mountain_count))
        free_set = free_set - mountain_set
        assert len(free_set) == len(hexagon_names) - mountain_count
        
        random.shuffle(hexagon_points_list)
        points_map = {}
        for (name_index, name) in enumerate(sorted(list(hexagon_names))):
            points_map[name] = hexagon_points_list[name_index]
        
        player_points = [0 for player_index in range(player_count)]
        player_sorts = [set() for player_index in range(player_count)]

        points = 0
        player_index = 0
        while len(free_set) != 0:
            name = random.choice(list(free_set))
            donjon_set.add(name)
            free_set.remove(name)
            free_set = free_set - hexagon_adjacents[name]
            
            points += points_map[name]
            player_points[player_index] += points_map[name]
            player_sorts[player_index].add(points_map[name])
            player_index = (player_index + 1) % player_count

        if with_diversity:
            for player_index in range(player_count):
                diversity = 0
                if len(player_sorts[player_index]) >= 2:
                    diversity = len(player_sorts[player_index]) - diversity_shift
                    assert diversity > 0
                 
                player_points[player_index] += diversity
                points += diversity
                      
        points_sample.append(points)
        
        if ranking:
            player_points.sort(reverse=True)
            
        for player_index in range(player_count):
            player_points_sample[player_index].append(player_points[player_index])
            

    print()
    print(f"--- mountain_count: {mountain_count} --- with_diversity: {with_diversity} ; diversity_shift={diversity_shift}")
    print()
    print(f"    count = {len(points_sample)}")
    print(f"     mode = {statistics.mode(points_sample)}")
    print(f"     mean = {statistics.mean(points_sample):.1f}")
    print(f"quartiles = {statistics.quantiles(points_sample, n=4)}")
    print(f"  deciles = {statistics.quantiles(points_sample, n=10)}")
    print(f"      min = {min(points_sample)}")
    print(f"      max = {max(points_sample)}")
    print()
    
    
    print()
    print(f"--- points sorted by rank at each test ? : {ranking} ---")
    print()
    for player_index in range(player_count):
        print(f"player {player_index}     count = {len(player_points_sample[player_index])}")
        print(f"player {player_index}      mode = {statistics.mode(player_points_sample[player_index])}")
        print(f"player {player_index}      mean = {statistics.mean(player_points_sample[player_index]):.1f}")
        print(f"player {player_index} quartiles = {statistics.quantiles(player_points_sample[player_index], n=4)}")
        print(f"player {player_index}   deciles = {statistics.quantiles(player_points_sample[player_index], n=10)}")
        print(f"player {player_index}       min = {min(player_points_sample[player_index])}")
        print(f"player {player_index}       max = {max(player_points_sample[player_index])}")
        print()
       

    print()
    print("make_statistics_on_points: done")
  
    
if True:
    partition = compute_connex_partition(hexagon_adjacents)
    for (part_index, part) in enumerate(partition):
        print(f"part {part_index} of length {len(part)} = {part}")
     
if True:
    make_statistics_on_partition()
     
if True:
    make_statistics_on_distances(test_count=1)
        
if True:
    make_statistics_on_donjon_count()

if True:
    make_statistics_on_points(player_count=2, with_diversity=False, ranking=True)
    make_statistics_on_points(player_count=2, with_diversity=True, ranking=True)
    make_statistics_on_points(player_count=2, with_diversity=True, ranking=False)
    make_statistics_on_points(player_count=2, with_diversity=True, ranking=True, diversity_shift=1)
    make_statistics_on_points(player_count=2, with_diversity=True, ranking=False, diversity_shift=1)
    
print()
_ = input("main: done ; press enter to terminate")
