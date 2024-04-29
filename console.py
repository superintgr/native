
stream:
- input/core
- core/output

core:
- channel/clock
- clock/channel

clock:
- global/local
- local/global


channel:
- address/voltage/current
- current/addeess/voltage


copies = Record()

with open(address[outer], frequency) as stereo:
    state = stereo.sample_points(k)
    expectation = calculate_value(last_state, state)
    preparation = forward(expectation)
    with open(address[inner], frequency) as mid:
        side = mid.feed_forward(preparation)
    master = stereo.pull_backward(side)
    copies.push(master)

    