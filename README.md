# Netflix Movie Queue

<img src="https://s3.amazonaws.com/after-school-assets/netflix-queue.jpg" align="right" hspace="10" width="300">

Sometimes it's hard to keep up with your Netflix movie queue. Sometimes, all you need is a Friday night to binge watch Scandal.

We're going to use lists to manipulate our own movie queue.

Open this lab locally. Run `learn` in terminal to run the tests. Use those tests as a guide to code your solution in `movies.py`.

Each of the functions below (except step 3) should have one parameter, a list of movies, which will be altered by the function.

###Step 1: 

Define a function `first_movie` that returns the first movie in the queue. This function should accept a list as an argument (the movie queue)

####Step 2: 

Define a function `watch_next_movie` that deletes the first movie in the list and returns the modified list. This function should accept an list as an argument (the movie queue).

####Step 3: 

Define a function `add_to_queue` that returns the updated list. This function takes two arguments (the list of movies and the movie you want to add to the queue).

####Step 4:

Define a function `view_queue` that uses the each function to iterate over the list of movies. This function should use puts to print out "You will watch [movie name]" for every movie in the list. This function should accept an list as an argument (the movie queue).