from matplotlib import pyplot as plt

with open(".\generated_files\doc_topics.txt") as f:
     lines = [line.rstrip().split(sep=' ', maxsplit=-1) for line in f]

# creating a dictionary to store the pairs
# topic - # docs in this topic
counts = dict()
for line in lines:
  counts[int(line[3])] = counts.get(int(line[3]), 0) + 1

X = []
Y = []
for key in sorted(counts):
    X.append(key)
    Y.append(counts[key])

fig, ax = plt.subplots()
bars = ax.barh(X, Y)
ax.bar_label(bars)
ax.set_xlabel("Number of docs")
ax.set_ylabel("Number of topics")

plt.show()
