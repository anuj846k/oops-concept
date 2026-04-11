spots = list(
    map(
        int,
        input(
            "ENTER THE SPOTS (0 for free, 1 for occupied, separated by spaces): "
        ).split(),
    )
)

# import sys


# def max_cons_free_spot(spots):
#     max_count = 0
#     free_spot_count = 0


# # for line in sys.stdin:
#     for spot in spots:
#         if spot == 0:
#             free_spot_count += 1
#             max_count = max(max_count, free_spot_count)
#         else:
#             free_spot_count = 0

#     return max_count


# print(max_cons_free_spot(spots))


def max_circular(spots):
    arr = spots + spots
    max_count = 0
    free_spot_count = 0

    for i in arr:
        if i == 0:
            free_spot_count += 1
            max_count = max(max_count, free_spot_count)
        else:
            free_spot_count = 0

    return min(max_count, len(spots))


print(max_circular(spots))
