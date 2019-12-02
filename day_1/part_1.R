# R script for Advent of Code day 1 part 1
#
# It's just a simple math operation and summation, so R
# is straightforward. I like the Hadleyverse so I'll use it.

# Only needed package
library(tidyverse)

# load the data
df <- read.table('input.txt')

# Do the thing.

df %>%
	mutate(x = floor(V1/3)-2) %>%
	summarize(x = sum(x))