class Author(object):
    def __init__(self, first_name, second_name, surname):
        self.first_name = first_name
        self.second_name = second_name
        self.surname = surname


class Reference(object):
    def __init__(self, authors, title, journal_data, year, english_ref=0):
        self.authors = authors
        self.title = title
        self.journal_data = journal_data
        self.year = year
        self.english_ref = english_ref


Author("P", "A", "Kislitsyn")

references_arr = []
references_arr.append(
    Reference([Author("Л", "И", "Русинов")
                  , Author("Д", "А", "Варшалович")], "Электромагнитные переходы в изомерных ядрах",
              "Атомная Энергия 5, 432--445", 1958,
              Reference([Author("L", "I", "Rusinov")
                            , Author("D", "A", "Varshalovich")], "Electromagnetic transitions in isomeric nuclei",
                        "Journal of Nuclear Energy. Part A. Reactor Science, 10, 170--181", 1959))
)

print([ref.authors[1].surname for ref in references_arr])