#import itertools
line_no = 0
(sp, ep) = (0, 0)
(total_road, total_junc) = (0, 0)
#junc_time = []
road_info = []
sum_of_all_wt = 10**5


def index_min(t):
    return min(range(len(t)), key=t.__getitem__)


def index_unfinished_min(foo, bar):
    #temp = min(x[1] for x in itertools.izip_longest(foo,bar) if x[0] > 0)
    # return bar.index(temp)
    least = sum_of_all_wt
    least_index = sum_of_all_wt

    for i in range(len(foo)):
        if foo[i] == 0:
            continue
        if least > bar[i]:
            least = bar[i]
            least_index = i

    return least_index


def junc_wait(junc, clock):
    jt = junc_time[junc]
    t = jt-(clock % jt)
    # print 'wait at junc %d arriving at %d is %d' %(junc,clock,t)
    if t == jt:
        return 0
    else:
        return t


# read input
(sp, ep) = map(int, input().rstrip().split(' '))
sp = sp-1
ep = ep-1

(total_junc, total_road) = map(int, input().rstrip().split(' '))
a_matrix = [[None for x in range(total_junc)] for y in range(total_junc)]
a_list = [[] for x in range(total_junc)]

junc_time = list(map(int, input().rstrip().split(' ')))
for i in range(1, total_road+1):
    t1 = list(map(int, input().rstrip().split(' ')))
    (e, f, g) = map((lambda x: x-1), t1)
    a_matrix[e][f] = g+1
    a_matrix[f][e] = g+1
    a_list[e].append(f)
    a_list[f].append(e)

# print road_info, total_junc, total_road
# initialize all finished junc as false and shortest time to be infinity
finished_junc = [1 for x in range(total_junc)]
min_time = [sum_of_all_wt for x in range(total_junc)]
# initialize start point to 0
min_time[sp] = 0
clock = 0
clock_time_junc = [0 for x in range(total_junc)]
clock_time_junc[sp] = 0
# run the process until all junc get finished
roads_travelled = 0
juncs_travelled = 0
while (finished_junc.count(1) != 0):
    u = index_unfinished_min(finished_junc, min_time)
    # print '#############################\nmarking %d as finished\n#############################' %(u)
    finished_junc[u] = 0
    juncs_travelled = juncs_travelled + 1
    if (u == ep):
        continue
    # if (u == 5):
        # break
    for i in a_list[u]:
        if (i == sp):
            continue
        clock_time_junc[i] = clock_time_junc[u] + a_matrix[u][i]
        #junc_wait_time = junc_wait(i,clock_time_junc[i])
        if(i == ep):
            junc_wait_time = 0
        else:
            junc_wait_time = junc_wait(i, min_time[u] + a_matrix[u][i])
        clock_time_junc[i] = clock_time_junc[i] + junc_wait_time
        # print 'travelling on road between %d & %d having delay %d & clock_time %d' %(u,i,a_matrix[u][i],clock_time_junc[i])
        if min_time[i] > min_time[u] + a_matrix[u][i] + junc_wait_time:
            min_time[i] = min_time[u] + a_matrix[u][i] + junc_wait_time
        # print 'min_time is %d & junc wait at %d is %d' %(min_time[i],i,junc_wait_time)
        roads_travelled = roads_travelled + 1
print(min_time[ep])
