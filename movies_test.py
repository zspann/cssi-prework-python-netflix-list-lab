import sys
import unittest

from movies import *

class TestMovies(unittest.TestCase):

    def test_first_movie(self):
        movie_list = ["The Shawshank Redemption", "Wall-E", "The Dark Knight Rises", "George of the Jungle", "Fargo"]
        self.assertEqual(first_movie(movie_list), "The Shawshank Redemption")

    def test_watch_next_movie(self):
        movie_list = ["The Shawshank Redemption", "Wall-E", "The Dark Knight Rises", "George of the Jungle", "Fargo"]
        self.assertEqual(watch_next_movie(movie_list), ["Wall-E", "The Dark Knight Rises", "George of the Jungle", "Fargo"])

    def test_add_to_queue(self):
        movie_list = ["The Shawshank Redemption", "Wall-E", "The Dark Knight Rises", "George of the Jungle", "Fargo"]
        updated_movie_list = ["The Shawshank Redemption", "Wall-E", "The Dark Knight Rises", "George of the Jungle", "Fargo", "Amadeus"]
        self.assertEqual(add_to_queue(movie_list, "Amadeus"), updated_movie_list)
    
    def test_view_queue(self):
        movie_list = ["The Shawshank Redemption", "Wall-E", "The Dark Knight Rises", "George of the Jungle", "Fargo"]
        self.assertEqual(view_queue(movie_list), "1. The Shawshank Redemption\n2. Wall-E\n3. The Dark Knight Rises\n4. George of the Jungle\n5. Fargo\n")

if __name__ == '__main__':
    unittest.main()
