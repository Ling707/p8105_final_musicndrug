# with open("./data/other_illicit_raw.csv","r") as f_in, open("./data/words/other_illicit_sorted.csv","w") as f_out:
with open("./data/words/marijuana.csv","r") as f_in, open("./data/words/marijuana_sorted.csv","w") as f_out:

    words = set()
    for line in f_in:
        words.add(line.strip())
    words = list(words)
    words.sort()
    for each in words:
        f_out.write(each+"\n")
