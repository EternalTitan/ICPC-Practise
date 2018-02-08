def countX(steps):
    RC_MAXIMUM = 1000000
    edge_r = edge_c = RC_MAXIMUM
    for each_step in steps:
        r, c = map(int, each_step.split())
        if r < edge_r:
            edge_r = r
        if c < edge_c:
            edge_c = c
    return edge_r * edge_c
