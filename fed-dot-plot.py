import matplotlib as mpl
mpl.use("Agg")
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

def set_style():
    # This sets reasonable defaults for font size for
    # a figure that will go in a paper
    sns.set_context("paper")
    
    # Set the font to be serif, rather than sans
    sns.set(font='serif')
    
    # Make the background white, and specify the
    # specific font family
    sns.set_style("white", {
        "font.family": "serif",
        "font.serif": ["Times", "Palatino", "serif"]
    })

set_style()


def compute_pts(data, group_len, pts_len):
    pts = []
    median_pts = []
    xticks = []
    xgrids = []
    n = len(data)
    for g, d in enumerate(data):
        g_middle = (g+0.5) * group_len
        data = []
        for y, c in d:
            if c % 2 == 1:
                leftmost = g_middle - (c//2) * pts_len
            else:
                leftmost = g_middle - (c//2-0.5) * pts_len

            for i in range(c):
                pts.append( (leftmost+i*pts_len, y) )
                data.append(y)

        data.sort()
        median = data[len(data)//2]
        median_pts.append( (g_middle, median) )

        xticks.append(g_middle)
        xgrids.append(g * group_len)

    xgrids.append(n * group_len)
    return np.array(pts), np.array(median_pts), xticks, xgrids
        

d2017 = [(1.125, 4), (1.375, 8), (1.625, 4)]
d2018 = [(1.125, 1), (1.625, 1), (1.875, 2), (2.125, 5), (2.375, 2), (2.625, 3), (2.75, 1), (3.125, 1)]
d2019 = [(1.125, 1), (2.375, 2), (2.625, 3), (2.875, 2), (3.0, 2), (3.125, 3), (3.25, 1), (3.375, 1), (4.125, 1)]
d2020 = [(2.5, 1), (2.75, 5), (3.0, 8), (3.5, 1)]

data = [d2017, d2018, d2019, d2020]
pts, median_pts, xticks, xgrids = compute_pts(data, group_len=12, pts_len=1)
minor_grids = []
minor_grids = filter(lambda x: int(x)!=x, np.arange(0, 5, 0.25))
print(minor_grids)


fig, ax = plt.subplots()
scale = 0.75
fig.set_size_inches(11.37*scale, 6.54*scale)
fig.set_dpi(500)
ax.plot(pts[:,0], pts[:,1], '.', color='#4D5258')
ax.plot(median_pts[:,0], median_pts[:,1], 'r.')
ax.text(-5, 5.2, 'Percent', fontsize=12)
x = ax.get_xaxis()
ax.set_xticks(xgrids, minor=False)
ax.set_xticklabels(['', '', '', '', ''], minor=False)
ax.set_xticks(xticks, minor=True)
ax.set_xticklabels(['2017', '2018', '2019', 'Longer run'], minor=True)
ax.set_yticks([0, 1, 2, 3, 4, 5], minor=False)
ax.set_yticks(minor_grids, minor=True)
ax.set_ylim([0, 5])
ax.grid(b=True, which='major', axis='y')
ax.grid(b=True, which='minor', axis='y', linestyle=':')
fig.savefig('fed-dot.pdf')
fig.savefig('fed-dot.png')
