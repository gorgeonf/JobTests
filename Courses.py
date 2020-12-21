from enum import Enum


# Course completion status
class CompletionStatus(Enum):
    INCOMPLETE = 1
    WITHDRAWAL = 2
    COMPLETE = 3


# Fields associated with a Course
class CourseRecord:
    def __init__(self, name, mark, year_taken, status):
        """
        :param name: str
        :param mark: float
        :param year_taken: int
        :param status: CompletionStatus
        """
        self.__name = name
        self.__mark = mark
        self.__year_taken = year_taken
        self.__status = status

    def get_name(self):
        return self.__name

    def get_mark(self):
        return self.__mark

    def get_year_taken(self):
        return self.__year_taken

    def get_status(self):
        return self.__status

    def __str__(self):
        return "Course: " + self.__name + "; mark: " + self.__mark + "; year:" + self.__year_taken + "; status:" + self.__status


# Courses taken by a student
class Courses:
    def __init__(self, course_records):
        """
        :param course_records: {str: CourseRecord} Name to Record
        """
        self.__course_records = course_records

    def average_some_courses_per_year(self, course_names):
        """
        Return the average marks per year for the given courses.
        Only include completes for the year.
        :param course_names: List of Strings
        :return: {int: float} year_taken to average
        """

        # Dictionary: dict{year:average}
        averages_per_year = {}

        # Dictionary: dict{year:[marks]}
        marks_per_year = {}

        if course_names != []:
            # We parse the courses in course_names
            for course in course_names:
                # We check if the course name is valid (present in the course_records)
                if course in self.__course_records.keys():
                    # We check if the course was completed
                    if self.__course_records[course].get_status() == CompletionStatus.COMPLETE:
                        # We build a dictionary: dict{year:[marks]}
                        yy = self.__course_records[course].get_year_taken()
                        mark = self.__course_records[course].get_mark()
                        # If the year is not already in the dictionnary we create the entry
                        if yy not in marks_per_year.keys():
                            marks_per_year[yy] = [mark]
                        # Otherwise we append the list of marks
                        else:
                            marks_per_year[yy].append(mark)

            # Fill the dictionary computing the average of the marks
            for year in marks_per_year.keys():
                average = sum(marks_per_year[year]) / len(marks_per_year[year])
                averages_per_year[year] = average

        return averages_per_year

    def __str__(self):
        str = "Courses: "
        for course_name, course_record in self.__course_records.items():
            str += course_record + ";"
        return str