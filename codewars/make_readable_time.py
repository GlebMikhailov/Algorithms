def make_readable(seconds):
    h = int(seconds / 3600)
    m = int((seconds - (h * 3600)) / 60)
    s = int((seconds - (h * 3600)) - (m * 60))
    return "{:0>2}:{:0>2}:{:0>2}".format(h, m, s)