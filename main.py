import unittest

from Courses import CourseRecord
from Courses import CompletionStatus
from Courses import Courses

class CoursesTest(unittest.TestCase):

    def setUp(self):
      self.__course_records = dict()
      self.__course_records["MT101"] = CourseRecord("MT101", 80.0, 2020, CompletionStatus.COMPLETE)
      self.__course_records["CS101"] = CourseRecord("CS101", 81.0, 2020, CompletionStatus.INCOMPLETE)
      self.__course_records["HS101"] = CourseRecord("HS101", 82.0, 2020, CompletionStatus.WITHDRAWAL)
      self.__course_records["PS101"] = CourseRecord("PS101", 83.0, 2020, CompletionStatus.COMPLETE)
      self.__course_records["PH101"] = CourseRecord("PH101", 84.0, 2020, CompletionStatus.COMPLETE)
      self.__course_records["CS201"] = CourseRecord("CS201", 85.0, 2021, CompletionStatus.COMPLETE)
      self.__course_records["HS201"] = CourseRecord("HS201", 86.0, 2021, CompletionStatus.COMPLETE)

    def test_average_courses_per_year_with_none(self):
        courses = Courses(self.__course_records)
        course_names = []
        averages_per_year = courses.average_some_courses_per_year(course_names)
        self.assertEqual(len(averages_per_year), 0)

    def test_average_courses_per_year_with_many_one_year(self):
        courses = Courses(self.__course_records)
        course_names = ["MT101", "CS101", "HS101", "PH101"]
        averages_per_year = courses.average_some_courses_per_year(course_names)
        self.assertEqual(len(averages_per_year), 1)
        self.assertAlmostEqual(averages_per_year[2020], (80.0 + 84.0) / 2)

    def test_average_courses_per_year_with_no_matching(self):
        courses = Courses(self.__course_records)
        course_names = ["NOT"]
        averages_per_year = courses.average_some_courses_per_year(course_names)
        self.assertEqual(len(averages_per_year), 0)

    def test_average_courses_per_year_with_mix(self):
        courses = Courses(self.__course_records)
        course_names = ["MT101", "CS101", "HS101", "PS101", "PH101", "NOT", "CS201", "HS201"]
        averages_per_year = courses.average_some_courses_per_year(course_names)
        self.assertEqual(len(averages_per_year), 2)
        self.assertAlmostEqual(averages_per_year[2020], (80.0 + 83.0 + 84.0) / 3)
        self.assertAlmostEqual(averages_per_year[2021], (85.0 + 86.0) / 2)


if __name__ == '__main__':
    unittest.main()