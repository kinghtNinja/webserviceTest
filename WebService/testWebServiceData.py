from WebServiceData import WebServiceData


class TestWebServiceData:
    webserviceData=WebServiceData()

    def setup_method(self):
        self.webserviceData=WebServiceData()

    def test_check_that_name_matches(self):
        assert  self.webserviceData.getByCity("Atlanta")=="Atlanta","Name of the City Does not Match"
        print ("city name Matches")

    def test_check_that_coordinates_match(self):
        myCordinates =self.webserviceData.getCordinates("35", "79")

        assert myCordinates.__getitem__(0) == 35, "Latitude does not match"
        print("Latitude matches")
        assert myCordinates.__getitem__(1) == 79,"Longitude does not match"
        print("Longitude matches")

    def test_check_that_zipCode_matchesEnteredCity(self):
        assert self.webserviceData.getCityNameByZipCode("10015")=='"New York"',"City Name does not match NewYork"
        print("City name Matches")