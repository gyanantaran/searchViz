# searchViz - A Beautiful and ⚡️ Fast Search Visualizer

https://github.com/gyanantaran/searchViz/assets/95016059/8a3eab8e-1456-48a5-a91c-750cf1e47f12

<img width="709" alt="Screenshot 2024-04-09 at 12 57 55 AM" src="https://github.com/gyanantaran/searchViz/assets/95016059/0de525e8-0363-47e3-87e7-8591f35fecb1">

## Contributions

All contributions/suggestions are welcome!

## Introduction

Search methods are boring and fruitless untill they are visualised. Depth first search feels like a random walker on a lonely island. Breadth first search is like a stow but steady fire burning through a dense forestry. Don't believe me? See for your selves! Also, feel free to try writing your very own search methods, with the current API (not documented, only examples available inside searchViz/src/searchViz/Search.py::DFS and BFS).

## Instructions to build the project

```sh
cd searchViz                     # cd into the cloned directory
pip install -r requirements.txt  # basically installs numpy and pygame
python src/main.py               # run the entry-point file

# now just press spacebar to play or pause the search for the current search-method. DFS is the default.
```

## Some Demo examples

A nice and long, demo video:

[![A long Walkthrough Video -- searchViz](https://github.com/gyanantaran/searchViz/assets/95016059/0de525e8-0363-47e3-87e7-8591f35fecb1)](https://youtu.be/BKF-PEgd1PA?t=393)

<!-- https://user-images.githubusercontent.com/95016059/273106123-19ccd387-f563-4078-825d-e62327bfdde7.mp4 -->

A short Walkthrough:

[![Short Walkthrough Video -- searchViz](https://github.com/gyanantaran/searchViz/assets/95016059/0de525e8-0363-47e3-87e7-8591f35fecb1)](https://youtu.be/kNGsOoWh9fM?t=2)

## Features

1. Nodes distributions can be one of a few options (gaussian, unifrom)
2. Edge connections can be one of a few options (exponential, thresholded)

## Implementation

1. Using vectorized functions in numpy

creative commons License, copyright, gyanantaran aka vishalpaudel 2022.
