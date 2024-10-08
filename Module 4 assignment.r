# Load necessary libraries
library(ggplot2)
library(readr)

# Load the dataset
df <- read_csv("netflix_data.csv")

# Most watched genres
ggplot(df, aes(y = reorder(type, -..count..))) +
  geom_bar() +
  labs(title = "Most Watched Genres", x = "Number of Shows/Movies", y = "type") +
  theme_minimal()

# Ratings distribution
ggplot(df, aes(x = rating)) +
  geom_bar(fill = "lightblue") +
  labs(title = "Ratings Distribution", x = "Rating", y = "Count") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
