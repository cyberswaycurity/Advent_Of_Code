import sys
import re

file = sys.argv[1]

with open(file,"r") as f:

    file = f.read().strip()

sections = re.split(r"[a-z-\s]+:",file)
sections = [i.strip() for i in sections[1:]]

seeds = [ int(i) for i in sections[0].strip().split()]

maps = sections[1:]
maps = [ [ j.split() for j in i.split('\n')] for i in maps]

seed_ranges = []

for i in range(0,len(seeds),2):

    start = seeds[i]
    length = seeds[i + 1]
    (s,e) = (start, start + length)    

    seed_ranges.append((s,e))

location_ranges = []

for r in seed_ranges:

    ranges = [r]

    for m in maps:

        mapped_ranges = []

        while ranges:

            rr = ranges.pop()
            x,y = rr
            isInRanges = False
            
            for i in m:

                src_start = int(i[1])
                src_end = int(i[1]) + int(i[-1])
                src_range = (src_start,src_end)

                dst_start = int(i[0])
                dst_end = int(i[0]) + int(i[-1])
                dst_range = (dst_start,dst_end)

                if (src_start <= x < src_end) and (src_start <= y < src_end):

                    m1 = dst_start + (x - src_start)
                    m2 = dst_start + (y - src_start) + 1
                    mapped_ranges.append((m1,m2))
                    isInRanges = True

                    break

                if ( x < src_start ) and ( src_start <= y < src_end ):

                    m1 = x
                    m2 = src_start - 1
                    ranges.append((m1,m2))

                    m1 = dst_start
                    m2 = dst_start + ( y - src_start )
                    mapped_ranges.append((m1,m2))
                    isInRanges = True

                    break

                if ( src_start <= x < src_end ) and ( y >= src_end ):

                    m1 = dst_start + ( x - src_start )
                    m2 = dst_end
                    mapped_ranges.append((m1,m2))

                    m1 = src_end
                    m2 = src_end + ( y - src_end ) + 1
                    ranges.append((m1,m2))
                    isInRanges = True

                    break

                if ( x < src_start ) and ( y > src_end ):

                    m1 = x
                    m2 = src_start 
                    ranges.append((m1,m2))

                    m1 = dst_start
                    m2 = dst_end 
                    mapped_ranges.append((m1,m2))

                    m1 = src_end
                    m2 = src_end + ( y - src_end ) + 1
                    ranges.append((m1,m2))

                    isInRanges = True

                    break

            if not isInRanges:

                mapped_ranges.append(rr)

        ranges=mapped_ranges
        
    location_ranges.append(ranges)
        
ranges_minimums = [ [ min(i) for i in check ] for check in location_ranges ] 

print(min(min(ranges_minimums)))
