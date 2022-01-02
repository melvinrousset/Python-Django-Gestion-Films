from django.test import TestCase

from .models import Movie_Model

class Movie_Model_Test(TestCase):
    def test_title_with_not_number(self):
        """
        check if the title has not a number if this the case return True
        """

        future_Movie = Movie_Model(title = "1321313", description = "test", price = 9.9)
        self.assertIs(future_Movie.check_title(), True)

   

    
    def test_price_not_to_high(self):
        """
        check if the price exceed 25$ if this the case return True
        """

        future_Movie = Movie_Model(title = "1321313", description = "test", price = 25.1)
        self.assertIs(future_Movie.check_price(), True)

    def test_price_not_null(self):
        """
        check if the price is null if this the case return True
        """

        future_Movie = Movie_Model(title = "1321313", description = "test", price = 0.0)
        self.assertIs(future_Movie.check_price(), True)

    def test_price_not_negative(self):
        """
        check if the price is negative if this the case return True
        """

        future_Movie = Movie_Model(title = "1321313", description = "test", price = -5.2)
        self.assertIs(future_Movie.check_price(), True)


    

    

# Create your tests here.
