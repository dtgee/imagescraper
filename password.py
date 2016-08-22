def read_password():
    directory = "/home/terence/Desktop/projects/reddit_image_gallery"
    pw = None
    with open(directory + "/pw.txt") as f:
        pw = f.readline().rstrip('\n')
    return pw
