import unittest
from roadLevel import roadlevelvalue
import datetime

class TestRoadLevelValue(unittest.TestCase):

    datefrom = datetime.date(2016,04,01)
    dateto = datetime.date(2016,05,01)

    def test_getHistoryDateTime(self):
        dates = roadlevelvalue.getHistoryDateTime(self.datefrom, self.dateto)
        #for date in dates:r
        #    print date
        self.assertEqual(len(dates) , 31)

    def test_getRoadLevelValueUrlByDatesList(self):
        dates = roadlevelvalue.getHistoryDateTime(self.datefrom, self.dateto)
        levelValueUrl = roadlevelvalue.getRoadLevelValueUrlByDatesList(dates)
        self.assertEqual(len(levelValueUrl),288*31)
        #for url in levelValueUrl:
        #    print url

    def test_get24TimesPer5Mins(self):
        self.assertEqual(len(roadlevelvalue.get24TimesPer5Mins()) ,288)
        #for s in roadlevelvalue.get24TimesPer5Mins():
        #    print s

    def getRoadLevelValuePer5Mints(fromDate, toDate):
        roadlevelvalue.getRoadLevelValuePer5Mints(datefrom,dateto)


if __name__ == "__main__":
    unittest.main()
