from .. import []

center = calibrate(speakers, microphones)
left = push(sources, speakers)
right = pull(microphones, sinks)

# what to send? from a possible candidates and most recent center, send that which brings control points back
# what to listen? from a possible locations and most recent stereo, listen to that which brings control points back
# how to control? from stereo centers, the most possible and most impossible sides via new expectations and filters

