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
# 1
references_arr.append(
    Reference([Author("Л", "И", "Русинов"), Author("Д", "А", "Варшалович")],
              "Электромагнитные переходы в изомерных ядрах",
              "Атомная Энергия 5, 432--445", 1958,
              Reference([Author("L", "I", "Rusinov"), Author("D", "A", "Varshalovich")],
                        "Electromagnetic transitions in isomeric nuclei",
                        "Journal of Nuclear Energy. Part A. Reactor Science, 10, 170--181", 1959)))

# 2
references_arr.append(
    Reference([Author("Л", "К", "Пекер"), Author("Д", "А", "Варшалович")],
              "Магнитные моменты деформированных ядер с $К$=1/2",
              "Известия Академии Наук СССР. Серия Физическая 24 (3), 372---376", 1959))

# 3
references_arr.append(
    Reference([Author("Д", "А", "Варшалович")],
              "Вероятности электромагнитных переходов и статистические моменты сферических нечетно-нечетных ядер",
              "ЖЭТФ, 38, 172--180", 1960,
              Reference([Author("D", "A", "Varshalovich")],
                        "Electromagnetic Transition Probabilities and Static Moments of Odd-Odd Atomic Nuclei",
                        "JETP, 11 (1), 125", 1960)))

# 4
references_arr.append(
    Reference([Author("Д", "А", "Варшалович")],
              "Вероятности ротационных $gamma$-переходов типа Е2 и квадрупольные моменты деформированных ядер с $K$=1 и 1/2",
              "ЖЭТФ, 39, 461--462", 1960,
              Reference([Author("D", "A", "Varshalovich")],
                        "Probabilities of Rotational Gamma Transitions of Type E2 and Quadrupole Moments of Deformed Nuclei with $K$=1 and 1/2",
                        "JETP, 12 (2), 324", 1961)))

# 5
references_arr.append(
    Reference([Author("Д", "А", "Варшалович")],
              "Экспериментальные и теоретические коэффициенты смеси состояний и поляризация нуклонов в деформированных ядрах",
              "Известия Академии Наук СССР. Серия Физическая 24, 895-898", 1960))

# 6
references_arr.append(
    Reference([Author("Д", "А", "Варшалович")],
              "Вероятности $gamma$-переходов в деформированных нечетно-нечетных ядрах",
              "Известия Академии Наук СССР. Серия Физическая 25, 77--82", 1961))

# 7
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("Л", "К", "Пекер")],
              "Особенности деформированных нечетно-нечетных ядер с К=0",
              "Известия Академии Наук СССР. Серия Физическая 25, 287--297", 1961))

# 8
references_arr.append(
    Reference([Author("Д", "А", "Варшалович")],
              "Исследование тонкой и сверхтонкой структуры в ядерных спектрах",
              "Известия Академии Наук СССР. Серия Физическая 28, 275--286", 1964))

# 9
references_arr.append(
    Reference([Author("Д", "А", "Варшалович")],
              "Заторможенные $gamma$-переходы в $^{22}N$a",
              "Известия Академии Наук СССР. Серия Физическая 28, 287--288", 1964))

# 10
references_arr.append(
    Reference([Author("Д", "А", "Варшалович")],
              "Интерференция событий во времени",
              "Известия Академии Наук СССР. Серия Физическая 28, 396--399", 1964))

# 11
references_arr.append(
    Reference([Author("Д", "А", "Варшалович")],
              "Ориентация атомов и молекул резонансным излучением в космическом пространстве",
              "Астрономический журнал 42, 557--567", 1965,
              Reference([Author("D", "A", "Varshalovich")],
                        "Orientation of Atoms and Molecules by Resonance Radiation in Cosmic Space",
                        "Soviet Astronomy, Vol. 9, p.442", 1965)))

# 12
references_arr.append(
    Reference([Author("Д", "А", "Варшалович")],
              "Возможность создания направленного ядерного излучения",
              "Известия Академии Наук СССР. Серия Физическая 29, 2173-2176", 1965))

# 13
references_arr.append(
    Reference([Author("Д", "А", "Варшалович")],
              "Неупругое рассеяние модулированного излучения",
              "Ядерная физика 5, 643-646", 1966))

# 14
references_arr.append(
    Reference([Author("Д", "А", "Варшалович")],
              "Возможность когерентного усиления радиоизлучения $lambda$=21 см в космической среде",
              "Письма в редакцию ЖЭТФ 5, 180-182", 1966,
              Reference([Author("D", "A", "Varshalovich")],
                        "Coherent Amplification of Radio Emission in a Cosmic Medium",
                        "Journal of Experimental and Theoretical Physics Letters, Vol. 4, p.124", 1966)))

# 15
references_arr.append(
    Reference([Author("Д", "А", "Варшалович")],
              "Ориентация атомов водорода резонансным излучением",
              "ЖЭТФ 52, 242-254", 1967,
              Reference([Author("D", "A", "Varshalovich")],
                        "Orientation of Hydrogen Atoms by Resonance Radiation",
                        "Soviet Physics JETP, Vol. 25, p.157", 1967)))

# 16
references_arr.append(
    Reference([Author("Д", "А", "Варшалович")],
              "Правила отбора для многофотонных переходов",
              "Оптика и Спектроскопия 25, 162-163", 1968))

# 17
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("Р", "А", "Сюняев")],
              "Профиль спектральной линии Lα-излучения и спиновая температура в межгалактической среде",
              "Астрофизика 4, 359-371", 1968))

# 18
references_arr.append(
    Reference([Author("Д", "А", "Варшалович")],
              "Объяснение интерференционных экспериментов с HI и HeII",
              "Письма в редакцию ЖЭТФ 8, 584-588", 1968,
              Reference([Author("D", "A", "Varshalovich")],
                        "Explanation of Interference Experiments with H I and He II",
                        "Journal of Experimental and Theoretical Physics Letters, Vol. 8, p.357", 1968)))

# 19
references_arr.append(
    Reference([Author("Д", "А", "Варшалович")],
              "Динамическая ориентация спинов частиц в космической среде",
              "Астрофизика 4, 519-537", 1968))

# 20
references_arr.append(
    Reference([Author("Д", "А", "Варшалович")],
              "Возможность мазерных эффектов в атмосферах комет",
              "сборник «Физика комет» серия «Астрометрия и астрофизика» 4, 54-57", 1968))

# 21
references_arr.append(
    Reference([Author("Д", "А", "Варшалович")],
              "Поляризация излучения OH",
              "ЖЭТФ 56, 614-618", 1969,
              Reference([Author("D", "A", "Varshalovich")],
                        "Polarization of the OH Radio-emission."," JETP, 29 (2), 337", 1969)))

# 22
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("М", "И", "Дьяконов")],
              "Об эффекте Шварца и Хора",
              "Письма в редакцию ЖЭТФ 11, 594-597", 1970,
              Reference([Author("D", "A", "Varshalovich"), Author("M", "I", "D’yakonov")],
                        "Quantum Theory of Modulation of an Electron Beam at Optical Frequencies",
                        "JETP, 33 (1), 51", 1971)))

# 23
references_arr.append(
    Reference([Author("Д", "А", "Варшалович")],
              "Спиновое состояние атомов и молекул в космической среде",
              "УФН, 101, 369-383", 1970,
              Reference([Author("D", "A", "Varshalovich")],
                        "Spin States of Atoms and Molecules in the Cosmic Medium",
                        "Soviet Physics Uspekhi, Vol. 13, p.429", 1970)))

# 24
references_arr.append(
    Reference([Author("В", "Н", "Федоренко"), Author("Д", "А", "Варшалович")],
              "Интерференционные эффекты при резонансном рассеянии света на атомах в магнитном поле",
              "ЖЭТФ 59, 2048-2054", 1970,
              Reference([Author("V", "N", "Fedorenko"), Author("D", "A", "Varshalovich")],
                        "Interference Effects in Resonant Scattering of Light by Atoms in a Magnetic Field",
                        "JETP, 32 (6), 1110", 1971)))

# 25
references_arr.append(
    Reference([Author("D", "A", "Varshalovich")],
              "Spin Alignment in Cosmic Matter",
              "Soviet Science Review 2, 80-84", 1971))
# 26
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("В", "Н", "Федоренко")],
              "О некоторых особенностях спектров водородной плазмы, обусловленных пересечением уровней",
              "Оптика и Спектроскопия 30, 377-378", 1971))

# 27
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("Б", "В", "Комберг")],
              "Выстраивание спинов частиц в оболочках квазаров",
              "Астрономический журнал 48, 1075-1087", 1971,
              Reference([Author("Varshalovich", "D.", "A."), Author("Komberg", "B.", "V.")],
                        "Alignment of Particle Spins in Quasar Envelopes",
                        "Soviet Astronomy, Vol. 15, p.858", 1972)))

# 28
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("М", "И", "Дьяконов")],
              "Квантовая теория модуляции электронного пучка излучением лазера",
              "ЖЭТФ 60, 90-101", 1971,
              Reference([Author("D", "A", "Varshalovich"), Author("M", "I", "D’yakonov")],
                        "Quantum Theory of Modulation of an Electron Beam at Optical Frequencies",
                        "Soviet Journal of Experimental and Theoretical Physics, Vol. 33, p. 51", 1971)))

# 29
references_arr.append(
    Reference([Author("M", "I", "Dyakonov"), Author("D", "A", "Varshalovich")],
              "Optical modulation of electron beam by inverse Cerenkov effect",
              "Physics Letters 35A, 277-279", 1971))

# 30
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("М", "И", "Дьяконов")],
              "Квантовая теория модуляции электронного пучка на оптических частотах",
              "УФН 103, 774–776", 1971,
              Reference([Author("Varshalovich", "D.", "A."), Author("D’yakonov", "M.", "I.")],
                        "Quantum Theory of the Modulation of the Electron Beam at Optical Frequencies",
                        "Soviet Physics Uspekhi, Volume 14, Issue 2, pp. 232-233", 1971)))

# 31
references_arr.append(
    Reference([Author("В", "В", "Бурдюжа"), Author("Д", "А", "Варшалович")],
              "Спиновая ориентация молекул OH инфракрасным излучением",
              "Астрономический Журнал 49, 727-736", 1972,
              Reference([Author("Burdyuzha", "V.", "V."), Author("Varshalovich", "D.", "A.")],
                        "Spin Alignment of OH Molecules by Infrared Radiation",
                        "Soviet Astronomy, Vol. 16, p.597", 1973)))

# 32
references_arr.append(
    Reference([Author("В", "В", "Бурдюжа"), Author("Д", "А", "Варшалович")],
              "Вероятности ИК и радиопереходов молекул OH и CH",
              "Астрономический журнал 49, 1211-1217", 1972,
              Reference([Author("Burdyuzha", "V.", "V."), Author("Varshalovich", "D.", "A.")],
                        "Infrared and Radio Transition Probabilities of OH and CH",
                        "Soviet Astronomy, Vol. 16, p.980", 1973)))

# 33
references_arr.append(
    Reference([Author("V.", "S.", "Strelnitskii"), Author("R.", "A.", "Sunjaev"), Author("D.", "A.", "Varshalovich")],
              "Abnormal hydrogen abundance in maser sources",
              "Comments on Astrophysics and Space Science 4, 155-159", 1972))

# 34
references_arr.append(
    Reference([Author("M.", "I.", "Dyakonov"), Author("D.", "A.", "Varshalovich")],
              "The optical modulation of electron beams",
              "Soviet Science Review 3, 347-351", 1972))

# 35
references_arr.append(
    Reference([Author("В.", "В.", "Бурдюжа"), Author("Д.", "А.", "Варшалович")],
              "Инфракрасная накачка мазерных источников OH, связанных с зонами HII",
              "Астрономический журнал 50, 481-490", 1973,
              Reference([Author("Burdyuzha", "V.", "V."), Author("Varshalovich", "D.", "A.")],
                        "Infrared pumping of maser OH sources associated with H II regions",
                        "Soviet Astronomy, Vol. 17, p.308 (1973)", 1973)))

# 36
references_arr.append(
    Reference([Author("Д.", "А.", "Варшалович"), Author("А.", "Н.", "Москалев"), Author("В.", "К.", "Херсонский")],
              "Представление группы вращения в переменных ω и n(θ,φ)",
              "Известия Академии Наук СССР. Серия Физическая 38, 1711-1726", 1974))
# 37
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("А", "Н", "Москалев")],
              "Новые теоремы сложения поворотов",
              "Известия Академии Наук СССР. Серия Физическая 38, 1727-1732", 1974))

# 38
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("В", "В", "Бурдюжа")],
              "Поляризация излучения космического мазера OH",
              "Астрономический журнал 52, 1178-1186", 1975,
              Reference([Author("Varshalovich", "D.", "A."), Author("Burdiuzha", "V.", "V.")],
                        "Polarization of cosmic OH masers",
                        "Soviet Astronomy, vol. 19, no. 6, p. 705-710", 1976)))

# 39
references_arr.append(
    Reference([Author("В", "К", "Херсонский"), Author("Д", "А", "Варшалович")],
              "Межзвездные молекулы I: спектральные характеристики $^{12}$C$^{16}$O, $^{12}$C$^{18}$O, $^{12}$C$^{17}$O, $^{13}$C$^{16}$O",
              "Сообщения САО АН СССР 14, 43-58", 1975))

# 40
references_arr.append(
    Reference([Author("В", "К", "Херсонский"), Author("Д", "А", "Варшалович")],
              "Межзвездные молекулы II: спектральные характеристики $^{12}$C$^{32}$S, $^{12}$C$^{33}$S, $^{12}$C$^{34}$S, $^{13}$C$^{32}$S",
              "Сообщения САО АН СССР 14, 59-77", 1975))

# 41
references_arr.append(
    Reference([Author("В", "К", "Херсонский"), Author("Д", "А", "Варшалович")],
              "Межзвездные молекулы III: спектральные характеристики $^{28}$Si$^{16}$O, $^{29}$Si$^{16}$O, $^{30}$Si$^{16}$O",
              "Сообщения САО АН СССР 14, 78-93", 1975))

# 42
references_arr.append(
    Reference([Author("В", "К", "Херсонский"), Author("А", "Н", "Москалев"), Author("Д", "А", "Варшалович")],
              "К вычислению $12j$ — символов I рода",
              "Известия Академии Наук СССР. Серия Физическая 40, 702-706", 1976))

# 43
references_arr.append(
    Reference([Author("В", "К", "Херсонский"), Author("А", "Н", "Москалев"), Author("Д", "А", "Варшалович")],
              "К вычислению $12j$ — символов II рода",
              "Известия Академии Наук СССР. Серия Физическая 40, 707-711", 1976))

# 44
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("В", "К", "Херсонский"), Author("Ю", "А", "Шибанов")],
              "Приближенный метод расчета межмолекулярного взаимодействия",
              "ЖЭТФ 70, 1204-1213", 1976,
              Reference([Author("Varshalovich", "D.", "A."), Author("Khersonskii", "V.", "K."), Author("Shibanov", "Yu.", "A.")],
                        "An approximate method for calculating intermolecular interaction",
                        "JETP, Vol. 43 (4), p. 625", 1976)))

# 45
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("В", "К", "Херсонский")],
              "Роль молекулы HD в образовании первичных конденсаций",
              "Письма в Астрономический журнал 2, 574-576", 1976,
              Reference([Author("Varshalovich", "D.", "A."), Author("Khersonskii", "V.", "K.")],
                        r"The role of the HD molecule in the development of primordial condensations",
                        r"Soviet Astronomy Letters, vol. 2, Nov.-Dec. 1976, p. 227-228", 1976)))

# 46
references_arr.append(
    Reference([Author("В", "К", "Херсонский"), Author("Д", "А", "Варшалович")],
              r"Радиоизлучение межзвездной молекулы NS",
              r"Астрономический журнал 54, 915-919 (1977)", 1977,
              Reference([Author("Varshalovich", "D.", "A."), Author("Khersonskii", "V.", "K."), Author("Chernyi", "G.", "F.")],
                        r"Radio emission of the interstellar NS molecule",
                        r"Soviet Astronomy, vol. 21, July-Aug., p. 517-518", 1977)))

# 47
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("В", "К", "Херсонский")],
              r"Коллизионное возбуждение межзвездных молекул",
              r"Астрономический журнал 55, 328-333 (1978)", 1978,
              Reference([Author("Varshalovich", "D.", "A."), Author("Khersonskii", "V.", "K.")],
                        r"Collisional excitation of interstellar molecules",
                        r"Astronomy Letters, vol. 22, Mar.-Apr. 1978, p. 192-194", 1978)))

# 48
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("В", "К", "Херсонский")],
              r"Искажение спектра реликтового излучения водородной линией $lambda$=21 см в эпоху Z = 150-15",
              r"Письма в Астрономический журнал 3, 291-294", 1977,
              Reference([Author("Varshalovich", "D.", "A."), Author("Khersonskii", "V.", "K.")],
                        r"Distortion of the primordial radiation spectrum by the 21-cm hydrogen line at epochs $z$ = 150-15",
                        r"Soviet Astronomy Letters, vol. 3, July-Aug. 1977, p. 155-156", 1977)))

# 49
references_arr.append(
    Reference([Author("В", "К", "Херсонский"), Author("Д", "А", "Варшалович")],
              r"Инфракрасное излучение межзвездных молекул HD",
              r"Письма в Астрономический журнал 3, 506-509", 1977,
              Reference([Author("Khersonskii", "V.", "K."), Author("Varshalovich", "D.", "A.")],
                        r"Infrared emission of interstellar HD molecules",
                        r"Soviet Astronomy Letters, vol. 3, Nov.-Dec. 1977, p. 277-278", 1977)))

# 50
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("В", "К", "Херсонский")],
              r"Один из механизмов создания инверсной населенности уровней линейных молекул",
              r"Астрономический журнал 55, 328-333",1978,
              Reference([Author("Varshalovich", "D.", "A."), Author("Khersonskii", "V.", "K.")],
                        r"One mechanism for the creation of a population inversion in the levels of linear molecules",
                        r"Soviet Astronomy, vol. 22, Mar.-Apr. 1978, p. 192-194", 1978)))
# 51
references_arr.append(
    Reference([Author("В", "К", "Херсонский"), Author("Д", "А", "Варшалович")],
              "Охлаждение первичного вещества молекулярным водородом",
              "Астрономический журнал 55, 487-489", 1978,
              Reference([Author("Khersonskii", "V.", "K."), Author("Varshalovich", "D.", "A.")],
                        "Cooling of primordial matter by molecular hydrogen",
                        "Soviet Astronomy, vol. 22, May-June 1978, p. 279-280", 1978)))

# 52
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("В", "К", "Херсонский")],
              "Населенности вращательных уровней молекул в межзвездной среде",
              "Астрономический журнал 55, 1169-1175", 1978,
              Reference([Author("Varshalovich", "D.", "A."), Author("Khersonskii", "V.", "K.")],
                        "One mechanism for the creation of a population inversion in the levels of linear molecules",
                        "Soviet Astronomy, vol. 22, Mar.-Apr. 1978, p. 192-194", 1978)))

# 53
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("С", "А", "Левшаков")],
              "Линии поглощения молекулярного водорода в спектрах квазаров",
              "Письма в Астрономический журнал 4, 115-118", 1978,
              Reference([Author("Varshalovich", "D.", "A."), Author("Levshakov", "S.", "A.")],
                        "Molecular hydrogen lines in quasar spectra",
                        "Soviet Astronomy Letters, vol. 4, Mar.-Apr. 1978, p. 61-62", 1978)))

# 54
references_arr.append(
    Reference([Author("И", "Л", "Еверская"), Author("В", "К", "Херсонский"), Author("Д", "А", "Варшалович")],
              "Оценки кинетической температуры и концентрации межзвездного газа по наблюдениям молекулярных линий",
              "Астрономический журнал 56, 60-66", 1979,
              Reference([Author("Everskaia", "I.", "L."), Author("Khersonskii", "V.", "K."), Author("Varshalovich", "D.", "A.")],
                        "Kinetic temperature and density of the interstellar medium estimated from molecular line intensities",
                        "Astronomicheskii Zhurnal, Vol. 56, p.60", 1979)))

# 55
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("С", "А", "Левшаков")],
              "Линии поглощения H2 и CO в спектре квазара PHL 957",
              "Письма в Астрономический журнал 5, 371-374", 1979,
              Reference([Author("Varshalovich", "D.", "A."), Author("Levshakov", "S.", "A.")],
                        r"H$_2$ and CO absorption lines in the spectrum of the quasar PHL 957",
                        r"Soviet Astronomy Letters, vol. 5, July-Aug. 1979, p. 199-201", 1979)))

# 56
references_arr.append(
    Reference([Author("S.", "A", "Левшаков"), Author("Д.", "А", "Варшалович")],
              r"Molecular hydrogen lines in the absorption spectrum of quasar OQ 172",
              r"Astrophysical Letters 20, 67-73 (1979)", 1979))

# 57
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("В", "К", "Херсонский")],
              r"Связь радиальных кулоновских интегралов и аппарата углового момента",
              r"Известия Академии Наук СССР. Серия Физическая 43, 2099-2102 (1979)", 1979))

# 58
references_arr.append(
    Reference([Author("И.", "Н", "Бакулина"), Author("Н.", "М", "Блашенков"), Author("Д.", "А", "Варшалович"), Author("Г.", "Я", "Лаврентьев"), Author("Б.", "Н", "Шустов")],
              r"Лабораторное моделирование физико-химических процессов в космических газово-пылевых облаках",
              r"Астрономический журнал 57, 352-361 (1980)", 1980,
              Reference([Author("Bakulina", "I.", "N."), Author("Blashenkov", "N.", "M."), Author("Varshalovich", "D.", "A."), Author("Lavrentev", "G.", "Y."), Author("Shustrov", "B.", "N.")],
                        r"Laboratory Simulation of the Physiochemical Processes in Cosmic Gas / Dust Clouds",
                        r"Soviet Astronomy, vol. 24, Mar.-Apr. 1980, p. 203-208", 1980)))

# 59
references_arr.append(
    Reference([Author("Д", "А", "Варшалович")],
              r"Сообщение о работе «Межзвездная среда в лаборатории»",
              r"Природа 7, 102-103 (1980)"))
# 60
references_arr.append(
    Reference([Author("В", "К", "Херсонский"), Author("Д", "А", "Варшалович")],
              "Возможность наблюдений рекомбинационных линий в излучении Солнца",
              "Астрономический журнал, 57, 621-623", 1980,
              Reference([Author("Khersonskii", "V.", "K."), Author("Varshalovich", "D.", "A.")],
                        "The Possibility of Observing Recombination Lines in Solar Radiation",
                        "Soviet Astronomy, vol. 24, May-June 1980, p. 359, 360")))

# 61
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("С", "А", "Левшаков")],
              "Квазары и молекулярные облака",
              "Земля и Вселенная 3, 23-27", 1980))

# 62
references_arr.append(
    Reference([Author("C.", "W", "Kegel"), Author("Д.", "А", "Варшалович")],
              "On the interpretation of type I OH maser sources",
              "Nature 286, 136-138", 1980))

# 63
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("В", "К", "Херсонский")],
              "Молекулярная спектроскопия межзвездной среды",
              "Природа 12, 44-53", 1980))

# 64
references_arr.append(
    Reference([Author("D.", "A", "Varshalovich"), Author("G.", "F", "Chorny")],
              "Determination of magnetic field direction in a comet's head",
              "Icarus 43, 385-390", 1980))

# 65
references_arr.append(
    Reference([Author("В", "К", "Херсонский"), Author("Д", "А", "Варшалович"), Author("С", "А", "Левшаков")],
              "Об оценках возможностей радионаблюдений молекулярных облаков на космологических расстояниях",
              "Астрономический журнал 58, 29-33", 1981,
              Reference([Author("Khersonskii", "V.", "K."), Author("Varshalovich", "D.", "A."), Author("Levshakov", "S.", "A.")],
                        "Prospects for radio observations of molecular clouds at cosmological distances.",
                        "Sov. Astron., Vol. 25, p. 16-19 (1981)")))

# 66
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("В", "К", "Херсонский"), Author("Р", "А", "Сюняев")],
              "Нагрев первичного газа реликтовым излучением при наличии тяжелых элементов",
              "Астрофизика 17, 487-493", 1981))

# 67
references_arr.append(
    Reference([Author("Д", "А", "Варшалович")],
              "Межзвездные молекулы",
              "Астрофизика и Космическая физика 1, 135-185", 1981,
              Reference([Author("Varshalovich", "D.", "A.")],
                        "Interstellar molecules",
                        "Astrophysics and Space Physics Reviews 1, 123-175 (1981)")))

# 68
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("В", "К", "Херсонский")],
              r"Вращательное возбуждение линейных молекул при столкновениях",
              r"ЖТФ 51, 1569-1576 (1981)"))

# 69
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("С", "А", "Левшаков")],
              r"Квазар PKS 0237-233: Абсорбционные системы линий молекул CO с большим красным смещением",
              r"Письма в Астрономический журнал 7, 204-208 (1981)",
              Reference([Author("Varshalovich", "D.", "A."), Author("Levshakov", "S.", "A.")],
                        r"The quasar PKS 0237-233: high-redshift absorption systems of CO lines.",
                        r"Soviet Astron. Lett., Vol. 7, p. 113-115 (1981)")))

# 70
references_arr.append(
    Reference([Author("С.", "А", "Левшаков"), Author("Д.", "А", "Варшалович")],
              r"Анализ абсорбционных спектров одиннадцати квазаров с $Z_e geq 2$",
              r"Астрофизика 18, 49-62 (1982)"))

# 71
references_arr.append(
    Reference([Author("D.", "A", "Varshalovich"), Author("S.", "A", "Levshakov")],
              r"High red shift molecular clouds and absorption line spectra of quasars",
              r"Comments on Astrophysics 9, 199-210 (1982)"))

# 72
references_arr.append(
    Reference([Author("D.", "G", "Iakovlev"), Author("S.", "A", "Levshakov"), Author("D.", "A", "Varshalovich"), Author("I.", "G", "Mitrofanov")],
              r"Effects of spherically-symmetric gravitational lenses produced by galaxies and clusters",
              r"Astrophysics and Space Sciences 91, 133-155 (1983)"))

# 73
references_arr.append(
    Reference([Author("В.", "Б", "Небелицкий"), Author("Д.", "А", "Варшалович"), Author("С.", "А", "Левшаков"), Author("А.", "Ф", "Фоменко")],
              r"Спектральные наблюдения квазаров",
              r"Оптика и Спектроскопия 54, 763-765 (1983)"))

# 74
references_arr.append(
    Reference([Author("Д.", "А", "Варшалович"), Author("В.", "Х", "Кегель"), Author("С.", "", "Чандра")],
              r"Квазирезонансная столкновительная накачка мазеров H$_2$O",
              r"Письма в Астрономический журнал 9, 395-400 (1983)",
              Reference([Author("Varshalovich", "D.", "A."), Author("Kegel", "W.", ""), Author("Chandra", "", "")],
                        r"Quasiresonance Collisional Pumping of Water Masers",
                        r"Soviet Astronomy Letters, vol. 9, July-Aug. 1983, p. 209-212.")))

# 75
references_arr.append(
    Reference([Author("В.", "Б", "Небелицкий"), Author("А.", "Ф", "Фоменко"), Author("С.", "А", "Левшаков"), Author("Д.", "А", "Варшалович")],
              r"Спектральные наблюдения квазара OQ 172",
              r"Письма в Астрономический журнал 10, 83-89 (1984)",
              Reference([Author("Nebelitskii", "", ""), Author("Fomenko", "", ""), Author("Levshakov", "", ""), Author("Varshalovich", "", "")],
                        r"Spectra of the Quasar OQ172",
                        r"Soviet Astronomy Letters, Vol.10, NO.1, P. 32, 1984")))

# 76
references_arr.append(
    Reference([Author("S.", "", ""), Author("Chandra","C.W.","Kegel"), Author("D.","A.","Varshalovich"), Author("M.","","Albrecht")],
              r"Radiative transfer effects in H$_2$O masers",
              r"Astronomy and Astrophysics 140, 295-303 (1984)"))
# 77
references_arr.append(
    Reference([Author("S.", "Chandra"), Author("D.", "A.", "Varshalovich"), Author("C.W.", "Kegel")],
              "Einstein A — values for rotational transitions in the H2O – molecule",
              "Astronomy and Astrophysics Supplement Series 55, 51-53", 1984))

# 78
references_arr.append(
    Reference([Author("S.A.", "Levshakov"), Author("D.A.", "Varshalovich"), Author("V.S.", "Nebelitsky")],
              "Absorption Line Spectra of Quasars",
              "Advance in Space Research 3 (№10-12), 187-190", 1984))

# 79
references_arr.append(
    Reference([Author("S.", "Chandra"), Author("C.W.", "Kegel"), Author("D.", "A.", "Varshalovich")],
              "Einstain A coefficients for rotational transitions in the hydrogen sulphide molecule",
              "Journal of Physics B (Atomic and Molecular Physics) 17, 585-586", 1984))

# 80
references_arr.append(
    Reference([Author("S.", "Chandra"), Author("C.W.", "Kegel"), Author("D.", "A.", "Varshalovich")],
              "Einstein A — values for purely rotational transitions in the HDO molecule",
              "Astronomy and Astrophysics Supplement Series 58, 687-691", 1984))

# 81
references_arr.append(
    Reference([Author("S.A.", "Levshakov"), Author("D.A.", "Varshalovich")],
              "Molecular hydrogen in the $z$=2.811 absorbing material toward the quasar PKS 0528-250",
              "MNRAS 212, 517-521", 1985))

# 82
references_arr.append(
    Reference([Author("М.Г.", "Соловьев"), Author("Д.А.", "Варшалович")],
              "Вращательные спектры молекул TiO и ZrO и возможности их радионаблюдений",
              "Астрономический журнал 62, 268-271", 1985,
              Reference([Author("Solovev", "M. G."), Author("Varshalovich", "D. A.")],
                        "The TiO and ZrO Rotational Spectra and Candidate Radio Lines",
                        "Soviet Astronomy, vol. 29, Mar.-Apr. 1985, p. 153-155")))

# 83
references_arr.append(
    Reference([Author("S.", "Chandra"), Author("C.W.", "Kegel"), Author("D.", "A.", "Varshalovich")],
              "Prediction of maser emission from para-H2O at 1.635 mm and 922 µm",
              "Astronomy and Astrophysics 148, 145-150", 1985))

# 84
references_arr.append(
    Reference([Author("S.", "Chandra"), Author("D.", "A.", "Varshalovich"), Author("C.W.", "Kegel")],
              "Einstein A — coefficients for pure rotational transitions in D2O",
              "Pramana 25, 557-563", 1985))

# 85
references_arr.append(
    Reference([Author("С.А.", "Левшаков"), Author("В.К.", "Херсонский"), Author("Д.А.", "Варшалович")],
              "Возможная абсорбционная деталь в радиоспектре квазара PHI 61 и ее интерпретация",
              "Астрономический журнал 63, 25-30", 1986,
              Reference([Author("Levshakov", "S. A."), Author("Khersonskii", "V. K."), Author("Varshalovich", "D. A.")],
                        "A Candidate Radio Absorption Line in the Quasar PHL:61 - Some Interpretations",
                        "Soviet Astronomy, vol. 30, Jan.-Feb. 1986, p. 16-19")))

# 86
references_arr.append(
    Reference([Author("М.Г.", "Опендак"), Author("Д.А.", "Варшалович")],
              "Молекулярные ионы в плотных межзвездных облаках",
              "Астрономический журнал 63, 458-464", 1986))

# 87
references_arr.append(
    Reference([Author("С.А.", "Левшаков"), Author("Д.А.", "Варшалович")],
              "Исследование спектра PHL 61",
              "Письма в Астрономический журнал 12, 829-830", 1986))

# 88
references_arr.append(
    Reference([Author("S.", "Jaruschewski"), Author("S.", "Chandra"), Author("D.", "A.", "Varshalovich"), Author("C.W.", "Kegel")],
              "Einstein A — values for rotational transitions in the H$_2$CO molecule",
              "Astronomy and Astrophysics Supplement Series 63, 307-312", 1986))

# 89
references_arr.append(
    Reference([Author("С.А.", "Левшаков"), Author("Д.А.", "Варшалович"), Author("Е.А.", "Назаров")],
              "Спектральные исследования квазаров из Второго Бюраканского Обзора северного неба. I Квазары SBS 0953+549, SBS 1116+603, SBS1138+584",
              "Сообщения САО АН СССР 50, 48-50", 1986))

# 90
references_arr.append(
    Reference([Author("С.А.", "Левшаков"), Author("Д.А.", "Варшалович"), Author("Е.А.", "Назаров")],
              "Спектральные исследования квазаров из Второго Бюраканского Обзора северного неба. I Квазары SBS 0953+549, SBS 1116+603, SBS1138+584",
              "Астрофизика 25, 495-506", 1986))

# 91
references_arr.append(
    Reference([Author("В.К.", "Херсонский"), Author("Д.А.", "Варшаловиич")],
              "Диазирин – кандидат для обнаружения в межзвездной среде",
              "Астрофизические исследования (Известия САО АН СССР) 23, 11-16", 1985))

# 92
references_arr.append(
    Reference([Author("Д.А.", "Варшалович"), Author("С.А.", "Левшаков"), Author("Е.А.", "Назаров"), Author("О.И.", "Спиридонова"), Author("А.Ф.", "Фоменко")],
              r"Спектральное исследование квазара S5 0014+81: I Анализ эмиссионного спектра",
              r"Астрономический Журнал 64, 262-270", 1987))

# 93
references_arr.append(
    Reference([Author("С.А.", "Левшаков"), Author("Д.А.", "Варшалович"), Author("Е.А.", "Назаров"), Author("А.Ф.", "Фоменко")],
              r"Спектральное исследование квазара S5 0014+81: II Анализ адсорбционного спектра",
              r"Астрономический журнал 64,929-939", 1987))

# 94
references_arr.append(
    Reference([Author("В.К.", "Херсонский"), Author("Д.А.", "Варшаловиич")],
              r"Столкновительные переходы между вращательными уровнями линейных молекул",
              r"ЖТФ 57,639-647",1987))

# 95
references_arr.append(
    Reference([Author("В.К.","Херсонский"), Author("Д.А.","Варшалович"), Author("М.Г.","Опендак")],
              r"Межзвездные молекулы HCO",
              r"Кинематика и механика небесных тел 3 (№2),3-10 (1987)"))

# 96
references_arr.append(
    Reference([Author("В.К.","Херсонский"), Author("Д.А.","Варшаловиич")],
              r"Спектральные характеристики межзвездной молекулы H$_3$O+",
              r"Астрофизика27,325-334 (1987)"))

# 97
references_arr.append(
    Reference([Author("В.К.","Херсонский"), Author("Д.А.","Варшаловиич"), Author("М.Г.","Опендак")],
              r"Вращательные переходы межзвездной молекулы H$_2$D+",
              r"Астрономический журнал64,520-526 (1987)"))
# 98
references_arr.append(
    Reference([Author("Д.", "А", "Варшалович"), Author("Г.", "Г", "Павлов"), Author("А.", "Д", "Каманкер"), Author("Д.", "Г", "Варшалович")],
              "Всесоюзный семинар по физике нейтронных звезд",
              "Астрономический журнал 65, 1333-1337", 1988))

# 99
references_arr.append(
    Reference([Author("G.", "", "Piehler"), Author("W.H.", "", "Kegel"), Author("D.A.", "", "Varshalovich"), Author("V.K.", "", "Khersonskii")],
              "Analytic approximations of the temperature dependence of the collisional rate coefficients for H$_2$O and H$_2$CO",
              "Astronomy and Astrophysics Supplement Series 76, 195-204", 1988))

# 100
references_arr.append(
    Reference([Author("С.", "А", "Левшаков"), Author("Д.", "А", "Вернер"), Author("Д.", "Г", "Яковлев"), Author("Д.", "А", "Варшалович")],
              "Квазар 4C 24.61: наблюдение и анализ линий в абсорбционных системах с $Z_alpha > Z_e$",
              "Сообщения САО АН СССР 61, 84-88", 1989))

# 101
references_arr.append(
    Reference([Author("Д.", "А", "Варшалович"), Author("А.", "Д", "Каманкер"), Author("Д.", "Г", "Яковлев")],
              "Всесоюзный семинар по физике нейтронных звезд",
              "Письма в Астрономический журнал 18, 1108", 1992))

# 102
references_arr.append(
    Reference([Author("Д.", "А", "Варшалович"), Author("С.", "А", "Левшаков"), Author("А.", "Ю", "Потехин")],
              "Проверка неизменности фундаментальных констант за космологическое время",
              "УФН 163, 111-113", 1993))

# 103
references_arr.append(
    Reference([Author("Д.", "А", "Варшалович"), Author("А.", "В", "Санников")],
              "Молекулярные ионы H$_2^+$ в межзвездной среде",
              "Письма в Астрономический журнал 19, 719-724", 1993))

# 104
references_arr.append(
    Reference([Author("Д.", "А", "Варшалович"), Author("С.", "А", "Левшаков")],
              "К вопросу о зависимости физических констант от времени",
              "Письма в редакцию ЖТФ, 58, 231-235", 1993))

# 105
references_arr.append(
    Reference([Author("A.Y.", "", "Potekhin"), Author("D.A.", "", "Varshalovich")],
              "An upper limit on possible time variation of the fine-structure constant from QSO absorption spectra",
              "Astronomical and Astrophysical Transactions, 5, 103-106", 1994))

# 106
references_arr.append(
    Reference([Author("A.Y.", "", "Potekhin"), Author("D.A.", "", "Varshalovich")],
              "Non-variability of the fine-structure constant over cosmological time scales",
              "Astronomy and Astrophysics Supplementary Series 104, 89-98", 1994))

# 107
references_arr.append(
    Reference([Author("Д.", "А", "Варшалович"), Author("А.", "Ю", "Потехин")],
              "Проверка возможного космологического изменения постоянной тонкой структуры на основе анализа спектров квазаров",
              "Письма в Астрономический журнал 20, 883-889", 1994))

# 108
references_arr.append(
    Reference([Author("Д.", "А", "Варшалович"), Author("А.", "Ю", "Потехин")],
              "Спектроскопия квазаров и космология",
              "Природа №4, 3-15", 1995))

# 109
references_arr.append(
    Reference([Author("D.A.", "", "Varshalovich"), Author("A.Y.", "", "Potekhin")],
              "Cosmological variability of fundamental physical constants by analysis of quasar spectra",
              "Space Science Reviews 74, 259-268", 1995))

# 110
references_arr.append(
    Reference([Author("Д.", "А", "Варшалович"), Author("А.", "Ю", "Потехин")],
              "Менялись ли массы молекул за время жизни Вселенной?",
              "Письма в Астрономический журнал 22, 3-7", 1996))

# 111
references_arr.append(
    Reference([Author("Д.", "А", "Варшалович"), Author("В.", "Е", "Панчук"), Author("А.", "В", "Иванчик")],
              "Абсорбционные системы в спектрах квазаров HS 1946+76, S5 0014+81, S40636+68. Новые ограничения на космологическое изменение постоянной тонкой структуры",
              "Письма в Астрономический журнал 22, 8-16", 1996))

# 112
references_arr.append(
    Reference([Author("Е.", "Б", "Александров"), Author("Д.", "А", "Варшалович")],
              r"О поляризационной зависимости оптических сигналов когерентности магнитных подуровней сверхтонкой структуры основного состояния щелочных атомов",
              r"Оптика и Спектроскопия 82, 181-185", 1997))

# 113
references_arr.append(
    Reference([Author("Д.", "А", "Варшалович"), Author("И.", "Е", "Мазец")],
              r"Угловые моменты системы тождественных частиц с определенной схемой Юнга",
              r"Оптика и Спектроскопия 84, 571-580", 1998))

# 114
references_arr.append(
    Reference([Author("Д.", "А", "Варшалович"), Author("И.", "Е", "Мазец")],
              r"Поправка к статье «Угловые моменты системы тождественных частиц с определенной схемой Юнга»",
              r"Оптика и Спектроскопия 85, 1056", 1998))

# 115
references_arr.append(
    Reference([Author("Д.", "А", "Варшалович"), Author("А.", "В", "Иванчик"), Author("А.", "Ю", "Потехин")],
              r"Менялись ли в процессе космологической эволюции фундаментальные физические константы?",
              r"Известия РАН. Серия Физическая 62, 1714-1715", 1998))

# 116
references_arr.append(
    Reference([Author("А.И.", "", "Рябинков"), Author("Д.А.", "", "Варшалович"), Author("А.Д.", "", "Каминкер")],
              r"Пространственно-временное распределение вещества в интервале красных смещений $Z$=1.2-3.2",
              r"Письма в Астрономический журнал 24, 488-497", 1998))

# 117
references_arr.append(
    Reference([Author("A.Y.", "", "Potekhin"), Author("A.V.", "", "Ivanchik"), Author("D.A.", "", "Varshalovich"), Author("K.M.", "", "Lanzetta"), Author("J.A.", "", "Baldwin"), Author("G.M.", "", "Williger"), Author("R.F.", "", "Carswell")],
              r"Testing cosmological variability of the proton-to-electron mass ratio using the spectrum of PKS 0528-250",
              r"Astrophysical Journal 505, 523-528", 1998))

# 118
references_arr.append(
    Reference([Author("D.", "", "Ershov"), Author("S.A.", "", "Gulyaev"), Author("A.V.", "", "Ivanchik"), Author("D.A.", "", "Varshalovich"), Author("A.", "", "Tsivilev")],
              r"Interpretation of anomalous helium abundance derived from radio recombination line observations of nebulae",
              r"Astronomical and Astrophysical Transactions 15, 281-289", 1998))

# 119
references_arr.append(
    Reference([Author("Д.А.", "", "Варшалович"), Author("А.В.", "", "Иванчик"), Author("А.Ю.", "", "Потехин")],
              r"Фундаментальные физические константы: одинаковы ли их значения в различных областях пространства–времени?",
              r"ЖТФ 69, 1-5", 1999))
# 120
references_arr.append(
    Reference([Author("A.V.", "Ivanchik"), Author("A.Y.", "Potekhin"), Author("D.A.", "Varshalovich")],
              "The fine-structure constant: a new observational limit on its cosmological variation and some theoretical consequences",
              "Astronomy & Astrophysics 343, 439-445", 1999))

# 121
references_arr.append(
    Reference([Author("A.I.", "Ryabinkov"), Author("A.D.", "Kaminker"), Author("D.V.", "Varshalovich")],
              "The space-time distribution of absorption matter in the redshift interval $Z$ = 0.2 — 3.2",
              "Gravitation & Cosmology 5 (Supplement), 72-76", 1999))

# 122
references_arr.append(
    Reference([Author("Н.С.", "Бабковская"), Author("Д.А.", "Варшалович")],
              "Модель молекулярного аккреционного диска и H$_2$O-мазера в ядре галактики NGC4258",
              "Письма в Астрономический журнал 26, 180 - 189", 2000))

# 123
references_arr.append(
    Reference([Author("A.D.", "Kaminker"), Author("A.I.", "Ryabinkov"), Author("D.A.", "Varshalovich")],
              "Space-time distributions of QSO absorption systems",
              "Astronomy & Astrophysics 358, 1 - 12", 2000))

# 124
references_arr.append(
    Reference([Author("A.V.", "Orlov"), Author("A.V.", "Ivanchik"), Author("D.A.", "Varshalovich")],
              "Primordial nucleosynthesis: Effects of possible variations of fundamental physical constants",
              "Astronomical and Astrophysical Transactions 19, 375-383", 2000))

# 125
references_arr.append(
    Reference([Author("D.A.", "Varshalovich"), Author("A.Y.", "Potekhin"), Author("A.V.", "Ivanchik")],
              "Puzzle of the constancy of fundamental constants",
              "Comments on Modern Physics 2, D223 - D232", 2001))

# 126
references_arr.append(
    Reference([Author("Д.А.", "Варшалович"), Author("А.В.", "Иванчик"), Author("П.", "Петитжан"), Author("Р.", "Шриананд"), Author("С.", "Леду")],
              "Молекулярные линии HD в абсорбционной системе с красным смещением z = 2.3377",
              "Письма в Астрономический журнал 27, 803 - 806", 2001))

# 127
references_arr.append(
    Reference([Author("А.В.", "Иванчик"), Author("А.В.", "Орлов"), Author("Д.А.", "Варшалович")],
              "Влияние возможного отклонения значений фундаментальных физических констант на первичный нуклеосинтез",
              "Письма в Астрономический журнал 27, 723 - 734", 2001))

# 128
references_arr.append(
    Reference([Author("А.И.", "Рябинков"), Author("А.Д.", "Каминкер"), Author("Д.А.", "Варшалович")],
              "Космологические вариации пространственно-временного распределения абсорбционных систем в спектрах квазаров",
              "Письма в Астрономический журнал 27, 643 - 652", 2001))

# 129
references_arr.append(
    Reference([Author("D.A.", "Varshalovich"), Author("A.Y.", "Potekhin"), Author("A.V.", "Ivanchik")],
              "Problems of cosmological variability of fundamental physical constants",
              "Physica Scripta 95, 76 - 80", 2001))

# 130
references_arr.append(
    Reference([Author("А.В.", "Иванчик"), Author("Э.", "Родригес"), Author("П.", "Петижан"), Author("Д.А.", "Варшалович")],
              "Меняются ли фундаментальные константы в процессе космологической эволюции?",
              "Письма в Астрономический журнал 28, 483 - 488", 2002))

# 131
references_arr.append(
    Reference([Author("A.V.", "Ivanchik"), Author("D.A.", "Varshalovich"), Author("P.", "Petitjean"), Author("E.", "Rodriguez")],
              r"Does the proton-to-electron mass ratio $mu=m_p/m_e$ vary in the course of cosmological evolution?",
              r"Astrophysics and Space Science 283, 583 - 588", 2003))

# 132
references_arr.append(
    Reference([Author("A.I.", "Ryabinkov"), Author("A.D.", "Kaminker"), Author("D.A.", "Varshalovich")],
              r"A catalogue of absorption-line systems in QSO spectra",
              r"Astronomy & Astrophysics 412, 707 - 709", 2003))

# 133
references_arr.append(
    Reference([Author("М.Г.", "Ревнивцев"), Author("Р.А.", "Суняев"), Author("Д.А.", "Варшалович"), Author("В.В.", "Железняков"), Author("А.М.", "Черепащук"), Author("А.А.", "Лутовинов"), Author("Е.М.", "Чуразов"), Author("С.А.", "Гребенев"), Author("М.Р.", "Гилфанов")],
              r"Обзор области Галактического Центра в жестких рентгеновских лучах телескопом IBIS обсерватории ИНТЕГРАЛ. Каталог источников",
              r"Письма в Астрономический журнал 30, 430 - 435", 2004))

# 134
references_arr.append(
    Reference([Author("P.", "Petitjean"), Author("A.V.", "Ivanchik"), Author("R.", "Srianand"), Author("B.", "Aracil"), Author("D.A.", "Varshalovich"), Author("H.", "Chand"), Author("E.", "Rodriguez"), Author("C.", "Ledoux"), Author("P.", "Boisse")],
              r"Time dependence of the proton-to-electron mass ratio",
              r"Comptes Rendus Physique, 5, 411 - 415", 2004))

# 135
references_arr.append(
    Reference([Author("A.V.", "Ivanchik"), Author("P.", "Petitjean"), Author("D.A.", "Varshalovich"), Author("B.", "Aracil"), Author("R.", "Srianand"), Author("H.", "Chand"), Author("C.", "Ledoux"), Author("P.", "Boisse")],
              r"A new constraint on the time dependence of the proton-to-electron mass ratio: Analysis of the Q 0347-383 and Q 0405-443 spectra",
              r"Astronomy & Astrophysics 440, 45 - 52", 2005))
# 136
references_arr.append(
    Reference([Author("E.E", "К", "Холупенко"), Author("А.В", "И", "Иванчик"), Author("Д.А", "В", "Варшалович")],
              "CMBR distortion concerned with recombination of the primordial hydrogen plasma",
              "Gravitation & Cosmology 11, 161-165", 2005,
              Reference([Author("E.E", "K", "Kholupenko"), Author("A.V", "I", "Ivanchik"), Author("D.A", "V", "Varshalovich")],
                        "CMBR distortion concerned with recombination of the primordial hydrogen plasma",
                        "Gravitation & Cosmology 11, 161-165", 2005))
)

# 137
references_arr.append(
    Reference([Author("Е", "М", "Чуразов"), Author("Р", "А", "Сюняев"), Author("С", "Ю", "Сазонов"), Author("М", "Г", "Ревнивцев"), Author("Д", "А", "Варшалович")],
              "Positron annihilation spectrum from the Galactic Centre region observed by SPI/INTEGRAL",
              "MNRAS 357, 1377 — 1386", 2005,
              Reference([Author("E", "M", "Churazov"), Author("R", "A", "Sunyaev"), Author("S", "Y", "Sazonov"), Author("M", "G", "Revnivtsev"), Author("D", "A", "Varshalovich")],
                        "Positron annihilation spectrum from the Galactic Centre region observed by SPI/INTEGRAL",
                        "MNRAS 357, 1377 — 1386", 2005))
)

# 138
references_arr.append(
    Reference([Author("В.В", "М", "Мешков"), Author("А.В", "С", "Столяров"), Author("А.В", "И", "Иванчик"), Author("Д.А", "В", "Варшалович")],
              "Неодиабатический ab initio расчет коэффициентов чувствительности X1 Σ GU+ → B1 U+; C1 Π U систем H2 к изменению отношения масс протона и электронов",
              "Письма ЖЭТФ 83, 363 - 366", 2006,
              Reference([Author("V.V", "M", "Meshkov"), Author("A.V", "S", "Stolyarov"), Author("A.V", "I", "Ivanchik"), Author("D.A", "V", "Varshalovich")],
                        "Nonadiabatic ab initio calculation of the sensitivity coefficients for the X1 Σ GU+ → B1 U+; C1 Π U systems of H2 to the change of the proton and electron mass ratio",
                        "JETP Letters 83, 363 - 366", 2006))
)

# 139
references_arr.append(
    Reference([Author("Д.А", "В", "Варшалович"), Author("А.В", "И", "Иванчик"), Author("Н.С", "Б", "Бабковская")],
              "Мазерная линия λ0= 1.35 см молекулы H2O: сверхтонкая структура и ассиметрия спектрального профиля",
              "Письма в Астрономический журнал 32, 32 - 41", 2006,
              Reference([Author("D.A", "V", "Varshalovich"), Author("A.V", "I", "Ivanchik"), Author("N.S.", "", "Babkovskaya")],
                        "Masers line λ0= 1.35 cm of H2O molecule: hyperfine structure and asymmetry of spectral profile",
                        "Letters to Astronomical Journal 32, 32 - 41", 2006))
)

# 140
references_arr.append(
    Reference([Author("Е.М", "Чуразов"), Author("Р.А", "Сюняев"), Author("С.Ю", "Сазонов"), Author("М.Г", "Ревнивцев"), Author("Д.А", "Варшалович")],
              "Аннигиляционное излучение центральной зоны Галактики: результаты зоны ИНТЕГРАЛ",
              "УФН 176, 334 - 339", 2006,
              Reference([Author("E.M.", "Churazov"), Author("R.A.", "Sunyaev"), Author("S.Y.", "Sazonov"), Author("M.G.", "Revnivtsev"), Author("D.A.", "Varshalovich")],
                        "Annihilation radiation from the Galactic Center region: results from the INTEGRAL zone",
                        "Physics Uspekhi 176, 334 - 339", 2006))
)

# 141
references_arr.append(
    Reference([Author("E.E.", "", "Kholupenko"), Author("A.V.", "", "Ivanchik"), Author("D.A.", "", "Varshalovich")],
              "Rapid HeII -> HeI recombination and radiation arising from this process",
              "MNRAS Letters 378, L39 - L43", 2007,
              Reference([Author("E.E.", "", "Kholupenko"), Author("A.V.", "", "Ivanchik"), Author("D.A.", "", "Varshalovich")], "Rapid HeII -> HeI recombination and radiation arising from this process",
                        "MNRAS Letters 378, L39 - L43", 2007))
)

# 142
references_arr.append(
    Reference([Author("Ryabinkov", "", "AI"), Author("Kaminker", "", "AD"), Author("Varshalovich", "", "DA")],
              "The redshift distribution of absorption-line systems in QSO spectra",
              "MNRAS 376, 1838 — 1848", 2007,
              Reference([Author("Ryabinkov", "", ""), Author("Kaminker", "", ""), Author("Varshalovich", "", "")],
                        "The redshift distribution of absorption-line systems in QSO spectra",
                        "MNRAS 376, 1838 — 1848", 2007))
)

# 143
references_arr.append(
    Reference([Author("A", "V", "Ivanchik"), Author("D", "A", "Varshalovich"), Author("P", "", "Petitjean")],
              "Current status of astronomical observations on possible cosmological variations of the proton-to-electron mass ratio $mu=m_p/m_e$",
              "European Physical Journal - Special Topics 63, 191-196", 2008,
              Reference([Author("A", "V", "Ivanchik"), Author("D", "A", "Varshalovich"), Author("P", "", "Petitjean")],
                        "Current status of astronomical observations on possible cosmological variations of the proton-to-electron mass ratio $mu=m_p/m_e$",
                        "European Physical Journal - Special Topics 63, 191-196", 2008))
)

# 144
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("А", "В", "Иванчик"), Author("П", "", "Петижан")],
              "Современное состояние астрономических наблюдений по проблеме возможного космологического изменения отношения масс протона и электрона",
              "Труды Института прикладной астрономии РАН 18, 92-93", 2008,
              Reference([Author("D", "A", "Varshalovich"), Author("A", "V", "Ivanchik"), Author("P", "", "Petitjean")],
                        "Current status of astronomical observations on possible cosmological variations of the proton-to-electron mass ratio",
                        "Proceedings of the Institute of Applied Astronomy RAS 18, 92-93", 2008))
)

# 145
references_arr.append(
    Reference([Author("Е", "Е", "Холупенко"), Author("А", "В", "Иванчик"), Author("Д", "А", "Варшалович")],
              "Рекомбинация первичной гелиевой плазмы HeII $to$ HeI с учетом влияния нейтрального водорода",
              "Письма в Астрономический журнал 34, 803 - 818", 2008,
              Reference([Author("E", "E", "Kholupenko"), Author("A", "V", "Ivanchik"), Author("D", "A", "Varshalovich")],
                        "Recombination of primordial helium plasma HeII → HeI considering the influence of neutral hydrogen",
                        "Letters to Astronomical Journal 34, 803 - 818", 2008))
)

# 146
references_arr.append(
    Reference([Author("С", "А", "Балашев"), Author("Д", "А", "Варшалович"), Author("А", "В", "Иванчик")],
              "Направленное излучение и фотодиссоционные области в облаках молекулярного водорода",
              "Письма в Астрономический журнал 35, 171 - 188", 2009,
              Reference([Author("S", "A", "Balashev"), Author("D", "A", "Varshalovich"), Author("A", "V", "Ivanchik")],
                        "Directed radiation and photodissociative regions in molecular hydrogen clouds",
                        "Letters to Astronomical Journal 35, 171 - 188", 2009))
)

# 147
references_arr.append(
    Reference([Author("", "", "Greiner"), Author("", "", "Iyudin"), Author("", "", "Kanbach"),
               Author("", "", "Zoglauer"), Author("", "", "Diehl"), Author("", "", "Ryde"),
               Author("", "", "Hartmann"), Author("A", "V", "Kienlin"), Author("", "", "McBreen"),
               Author("", "", "Ajello"), Author("", "", "Bagoly"), Author("L", "G", "Balasz"),
               Author("", "", "Barbiellini"), Author("", "", "Bellazini"), Author("", "", "Bezrukov"),
               Author("D", "V", "Bisikalo"), Author("G", "", "Bisnovaty-Kogan"),
               Author("S", "", "Boggs"), Author("A", "", "Bykov"),
               Author("A", "", "Cherepashuk"), Author("", "", "Chernenko"),
               Author("W", "", "Collmar"), Author("G", "", "DiCocco"),
               Author("W", "", "Dröge"), Author("M", "", "Gierlik"),
               Author("L", "", "Hanlon"), Author("I", "", "Horvath"),
               Author("R", "", "Hudec"), Author("J", "", "Kiener"),
               Author("C", "", "Labanti"), Author("N", "", "Langer"),
               Author("S", "", "Larsson"), Author("G", "", "Lichti"),
               Author("V", "M", "Lipunov"), Author("B", "K", "Lubsandorgiev"),
               Author("A", "", "Majczyna"), Author("K", "", "Mannheim"),
               Author("R", "", "Marcinkowski"), Author("M", "", "Marisaldi"),
               Author("B", "", "McBreen"), Author("A", "", "Meszaros"),
               Author("E", "", "Orlando"), Author("M", "", "Panasyuk"),
               Author("", "", "Pearce"), Author("", "", "Pian"),
               Author("", "", "Poleschuk"), Author("", "", "Pollo"),
               Author("", "", "Pozanenko"), Author("", "", "Savaglio"),
               Author("", "", "Shustov"), Author("", "", "Strong"),
               Author("", "", "Svertilov"), Author("", "", "Tatischeff"),
               Author("", "", "Uvarov"), Author("", "", "Varshalovich"),
               Author("", "", "Wunderer"), Author("", "", "Wrochna"),
               Author("", "", "Zabrodskij"), Author("", "", "Zeleny")],
              "Gamma-ray burst investigation via polarimetry and spectroscopy (GRIPS)",
              "Experimental Astronomy 23, 91-120", 2009,
              Reference([Author("", "", ""), # ... остальные авторы ...
                         ],
                        "Gamma-ray burst investigation via polarimetry and spectroscopy (GRIPS)",
                        "Experimental Astronomy 23, 91-120", 2009))
)

# 148
references_arr.append(
    Reference([Author("С", "А", "Балашев"), Author("А", "В", "Иванчик"),
               Author("Д", "А", "Варшалович")],
              "Молекулярные облака HD/H в ранней Вселенной. Проблема первичного дейтерия",
              "Письма в Астрономический журнал 36, 803 - 815", 2010,
              Reference([Author("S", "A", "Balashev"),
                         # ... остальные авторы ...
                         ],
                        "Molecular clouds HD/H in the early Universe. The problem of primordial deuterium",
                        "Letters to Astronomical Journal 36, 803 - 815", 2010))
)

# 149
references_arr.append(
    Reference([Author("A", "V", "Ivanchik"), Author("P", "", "Petitjean"),
               Author("S", "A", "Balashev"), Author("", "", ""),
               Author("D", "A", "Varshalovich"), Author("", "", ""),
               Author("", "", "")],
              # ... остальные авторы ...
              )
)

# 150
references_arr.append(
    Reference([Author("E","E","Kholupenko"),
               Author("A","V","Ivanchik"),
               Author("D","A","Varshalovich")],
              # ... остальные авторы ...
              )
)

# 151
references_arr.append(
    Reference([Author("А", "В", "Нестерёнок"), Author("Д", "А", "Варшалович")],
              "Асимметрия спектра высокоскоростных компонент мазерного излучения Н$_2$O активных ядер галактик",
              "Письма в Астрономический журнал 36, 3 - 8", 2010,
              Reference([Author("A", "V", "Nesteruonok"), Author("D", "A", "Varshalovich")],
                        "Asymmetry of the spectrum of high-velocity components of the maser emission of H$_2$O in active galactic nuclei",
                        "Letters to Astronomical Journal 36, 3 - 8", 2010))
)

# 152
references_arr.append(
    Reference([Author("Д", "А", "Варшалович"), Author("А", "В", "Иванчик"),
               Author("С", "А", "Балашев"), Author("П", "", "Петижан")],
              "Первичный нуклеосинтез дейтерия и содержание молекул HD/H$_2$ в межзвездных облаках, существовавших 12 млрд. лет назад",
              "УФН 180, 415 - 419", 2010,
              Reference([Author("D", "A", "Varshalovich"), Author("A", "V", "Ivanchik"),
                         Author("S", "A", "Balashev"), Author("P", "", "Petitjean")],
                        "Primordial nucleosynthesis of deuterium and the content of HD/H$_2$ molecules in interstellar clouds existing 12 billion years ago",
                        "Physics Uspekhi 180, 415 - 419", 2010))
)

# 153
references_arr.append(
    Reference([Author("С", "А", "Балашев"), Author("Д", "А", "Варшалович"),
               Author("А", "В", "Иванчик")],
              "Особенности переноса излучения в облаках молекулярного водорода",
              "Динамика сложных систем - XXI век 5 (2), 10 - 22", 2011,
              Reference([Author("S", "A", "Balashev"), Author("D", "A", "Varshalovich"),
                         Author("A", "V", "Ivanchik")],
                        "Features of radiation transfer in molecular hydrogen clouds",
                        "Dynamics of Complex Systems - XXI century 5 (2), 10 - 22", 2011))
)

# 154
references_arr.append(
    Reference([Author("А", "В", "Иванчик"), Author("Д", "А", "Варшалович"),
               Author("С", "А", "Балашев")],
              "Спектры квазаров - пространственно-временные фотографии Вселенной",
              "Динамика сложных систем - XXI век 5 (2), 4 - 10", 2011,
              Reference([Author("A", "V", "Ivanchik"), Author("D", "A", "Varshalovich"),
                         Author("S", "A", "Balashev")],
                        "Quasar spectra - space-time photographs of the Universe",
                        "Dynamics of Complex Systems - XXI century 5 (2), 4 - 10", 2011))
)

# 155
references_arr.append(
    Reference([Author("S", "A", "Balashev"), Author("P", "", "Petitjean"),
               Author("A", "V", "Ivanchik"), Author("C", "", "Ledoux"),
               Author("R", "", "Srianand"), Author("P", "", "Noterdaeme"),
               Author("D", "A", "Varshalovich")],
              "Partial coverage of the broad-line region of Q1232+082 by an intervening H$_2$-bearing cloud",
              "MNRAS 418, 357 - 369", 2011,
              Reference([Author("S", "A", "Balashev"), Author("P", "", "Petitjean"),
                         Author("A", "V", "Ivanchik"), Author("C", "", "Ledoux"),
                         Author("R", "", "Srianand"), Author("P", "", "Noterdaeme"),
                         Author("D", "A", "Varshalovich")],
                        "Partial coverage of the broad-line region of Q1232+082 by an intervening H$_2$-bearing cloud",
                        "MNRAS 418, 357 - 369", 2011))
)

# 156
references_arr.append(
    Reference([Author("E", "E", "Kholupenko"), Author("A", "V", "Ivanchik"),
               Author("S", "A", "Balashev"), Author("D", "A", "Varshalovich")],
              "Advanced three-level approximation for numerical treatment of cosmological recombination",
              "MNRAS 417, 2417 - 2425", 2011,
              Reference([Author("E", "E", "Kholupenko"), Author("A", "V", "Ivanchik"),
                         Author("S", "A", "Balashev"), Author("D", "A", "Varshalovich")],
                        "Advanced three-level approximation for numerical treatment of cosmological recombination",
                        "MNRAS 417, 2417 - 2425", 2011))
)

# 157
references_arr.append(
    Reference([Author("А", "В", "Нестеренок"), Author("Д", "А", "Варшалович")],
              "Мазерное излучение Н$_2 {}^{16}$О и Н$_2 {}^{18}$О газопылевых облаков",
              "Письма в Астрономический журнал 37, 499 - 511", 2011,
              Reference([Author("A", "V", "Nesteruonok"), Author("D", "A", "Varshalovich")],
                        "Maser emission of H$_2 {}^{16}$O and H$_2 {}^{18}$O in gas-dust clouds",
                        "Letters to Astronomical Journal 37, 499 - 511", 2011))
)

# 158
references_arr.append(
    Reference([Author("E","Churazov"), Author("S","Sazonov"),
               Author("S","Tsygankov"), Author("R","Sunyaev"),
               Author("D","A","Varshalovich")],
              "Positron annihilation spectrum from the Galactic Centre region observed by SPI/INTEGRAL revisited: Annihilation in a cooling ISM?",
              "MNRAS 411, 1727 - 1743", 2011,
              Reference([Author("E","Churazov"), Author("S","Sazonov"),
                         Author("S","Tsygankov"), Author("R","Sunyaev"),
                         Author("D","A","Varshalovich")],
                        "Positron annihilation spectrum from the Galactic Centre region observed by SPI/INTEGRAL revisited: Annihilation in a cooling ISM?",
                        "MNRAS 411, 1727 - 1743", 2011))
)

# 159
references_arr.append(
    Reference([Author("D","A","Varshalovich"), Author("A","V","Ivanchik"),
               Author("S","A","Balashev")],
              "Quasar Spectroscopy and Cosmology",
              "Journal of Physics: Conference Series 397, 012051", 2012,
              Reference([Author("D","A","Varshalovich"), Author("A","V","Ivanchik"),
                         Author("S","A","Balashev")],
                        "Quasar Spectroscopy and Cosmology",
                        "Journal of Physics: Conference Series 397, 012051", 2012))
)

# 160
references_arr.append(
    Reference([Author("В","В","Клименко"), Author("А","В","Иванчик"),
               Author("Д","А","Варшалович"), Author("А","Г","Павлов")],
              "Влияние гамма-излучения на изотопный состав облаков межзвездной среды",
              "Письма в Астрономический журнал 38, 414 - 430", 2012,
              Reference([Author("V","V","Klimenko"), Author("A","V","Ivanchik"),
                         Author("D","A","Varshalovich"), Author("A","G","Pavlov")],
                        "Influence of gamma radiation on the isotopic composition of interstellar medium clouds",
                        "Letters to Astronomical Journal 38, 414 - 430", 2012))
)

# 161
references_arr.append(
    Reference([Author("J","G","Greiner"), Author("K","M","Mannheim"),
               Author("F","A","Aharonian"), Author("M","A","Ajello"),
               Author("L","G","Balasz"), Author("G","B","Barbiellini"),
               Author("R","B","Bellazzini"), Author("S","B","Bishop"),
               Author("G","S","Bisnovatij-Kogan"), Author("S","B","Boggs"),
               Author("A","B","Bykov"), Author("G","D","DiCocco"),
               Author("R","D","Diehl"), Author("D","E","Elsässer"),
               Author("S","F","Foley"), Author("C","F","Fransson"),
               Author("N","G","Gehrels"), Author("L","H","Hanlon"),
               Author("D","H","Hartmann"), Author("W","H","Hermsen"),
               Author("W","H","Hillebrandt"), Author("R","H","Hudec"),
               Author("A","I","Iyudin"), Author("J","J","Jose"),
               Author("M","K","Kadler"), Author("G","K","Kanbach"),
               Author("W","K","Klamra"), Author("J","K","Kiener"),
               Author("S","K","Klose"), Author("I","K","Kreykenbohm"),
               Author("L","K","Kuiper"), Author("N","K","Kylafis"),
               Author("C","L","Labanti"), Author("K","L","Langanke"),
               Author("N","L","Langer"), Author("S","L","Larsson"),
               Author("B","L","Leibundgut"), Author("U","L","Laux"),
               Author("F","L","Longo"), Author("K","M","Maeda"),
               Author("R","M","Marcinkowski"), Author("M","M","Marisaldi"),
               Author("B","M","McBreen"), Author("S","M","McBreen"),
               Author("A","M","Meszaros"), Author("K","N","Nomoto"),
               Author("M","P","Pearce"), Author("A","P","Peer"),
               Author("E","P","Pian"), Author("N","P","Prantzos"),
               Author("G","R","Raffelt"), Author("O","R","Reimer"),
               Author("W","R","Rhode"), Author("F","R","Ryde"),
               Author("C","S","Schmidt"), Author("J","S","Silk"),
               Author("B","M.","Shustov"), Author("A.","S.","Strong"),
               Author("N.","T.","Tanvir"), Author("F.-K.","T.","Thielemann"),
               Author("O.","T.","Tibolla"), Author("D.","T.","Tierney"),
               Author("J.","T.","Trümper"), Author("D.","A.","Varshalovich"),
               Author("J.","W.","Wilms"), Author("G.","W.","Wrochna"),
               Author("A.","Z.","Zdziarski"), Author("A.","Z.","Zoglauer")],
              "GRIPS - Gamma-Ray Imaging, Polarimetry and Spectroscopy",
              "Experimental Astronomy 34, 551 - 582", 2012,
              Reference([Author("J.","G.","Greiner"), Author("K.","M.","Mannheim"),
                         Author("F.","A.","Aharonian"), Author("M.","A.","Ajello"),
                         Author("L.","G.","Balasz"), Author("G.","B.","Barbiellini"),
                         # и так далее для всех авторов...
                        ],
                        "GRIPS - Gamma-Ray Imaging, Polarimetry and Spectroscopy",
                        "Experimental Astronomy 34, 551 - 582", 2012))
)

# 162
references_arr.append(
    Reference([Author("A","I","Sobolev"), Author("D","A","Varshalovich")],
              "Numerical modeling of light-induced drift in a cloud of interstellar gas",
              "Journal of Physics: Conference Series 572, 012013", 2014)
)

# 163
references_arr.append(
    Reference([Author("А","В","Нестерёнок"), Author("Д","А","Варшалович")],
              "Накачка мазеров Н$_2$О: эффект квазирезонансной передачи энергии в столкновениях между молекулами Н$_2$ и Н$_2$О",
              "Письма в Астрономический журнал 40, 473 - 483", 2014)
)

# 164
references_arr.append(
    Reference([Author("S","A","Balashev"), Author("V","V","Klimenko"),
                Author("A","V","Ivanchik"), Author("D","A","Varshalovich"),
                Author("P","","Petitjean"), Author("P","","Noterdaeme")],
              "Molecular hydrogen absorption systems in sloan digital sky survey",
              "MNRAS 440, 225 - 239", 2014)
)

# 165
references_arr.append(
    Reference([Author("A","I","Sobolev"), Author("A","V","Ivanchik"),
                Author("D","A","Varshalovich"), Author("S","A","Balashev")],
              "Measurements of the Cosmic Microwave Background Temperature at high redshift by analysis of CO excitation",
              "Journal of Physics: Conference Series 661, 012013", 2015)
)

# 166
references_arr.append(
    Reference([Author("V","V","Klimenko"), Author("S","A","Balashev"),
                Author("A","V","Ivanchik"), Author("D","A","Varshalovich")],
              "A new estimation of HD/2H$_2$ at high redshift using the spectrum of the quasar J 2123-0050",
              "Journal of Physics: Conference Series 661, 012005", 2015)
)

# 167
references_arr.append(
    Reference([Author("S","A","Balashev"), Author("E","E","Kholupenko"),
                Author("J","","Chluba"), Author("A","V","Ivanchik"),
                Author("D","A","Varshalovich")],
              "Spectral distortions of the CMB dipole",
              "The Astrophysical Journal, 810, 131", 2015)
)

# 168
references_arr.append(
    Reference([Author("E","E","Kholupenko"), Author("S","A","Balashev"),
                Author("A","V","Ivanchik"), Author("D","A","Varshalovich")],
              "The thermal Sunyaev-Zeldovich effect of primordial recombination radiation",
              "MNRAS 446, 3593 - 3607", 2015)
)

# 169
references_arr.append(
    Reference([Author("V","V","Klimenko"), Author('S','A','Balashev'),
                Author('A','V','Ivanchik'), Author('C','','Ledoux'),
                Author('P','','Noterdaeme'), Author('P','','Petitjean'),
                Author('R','','Srianand'), Author('D','A','Varshalovich')],
              "Partial covering of the emission regions of Q 0528-250 by intervening H2 clouds",
              "MNRAS 448, 280 - 298", 2015)
)

# 170
references_arr.append(
    Reference([Author('А','В','Иванчик'), Author('С','А','Балашев'),
                Author('Д','А','Варшалович'), Author('В','В','Клименко')],
              "Молекулярные облака H$_2$/HD в ранней вселенной. Независимый способ оценки концентрации барионов во вселенной",
              "Астрономический журнал 92, 119 - 138", 2015)
)

# 171
references_arr.append(
    Reference([Author('С','А','Балашев'), Author('П','','Noterdaeme'),
                Author('В','В','Клименко'), Author('П','','Petitjean'),
                Author('Р','','Srianand'), Author('C','','Ledoux'),
                Author('А','В','Иванчик'), Author('Д','А','Варшалович')],
              "Neutral chlorine and molecular hydrogen at high redshift",
              "Astronomy & Astrophysics 575, L8", 2015)
)

# 172
references_arr.append(
    Reference([Author('Д','А','Варшалович'), Author('А','В','Карпова')],
              "Радиальные матричные элементы и аппарат углового момента",
              "Оптика и Спектроскопия 118, 3 - 7", 2015)
)

# 173
references_arr.append(
    Reference([Author("S","A","Balashev"), Author("E","O","Zavarygin"),
                Author("A","V","Ivanchik"), Author("K","N","Telikova"),
                Author("D","A","Varshalovich")],
              "The primordial deuterium abundance: SubDLA system at $z_{abs}$ = 2.437 towards the QSO J 1444+2919",
              "MNRAS 458, 2188 - 2198", 2016)
)

# 174
references_arr.append(
    Reference([Author("В","В","Клименко"), Author("С","А","Балашев"),
                Author("А","В","Иванчик"), Author("Д","А","Варшалович")],
              "Оценка физических условий в холодной фазе межзвездной среды в суб-DLA системе с $z=$2.06 в спектре квазара J 2123–0050",
              "Письма в Астрономический журнал 42, 161-188", 2016)
)

# 175
references_arr.append(
    Reference([Author("S","A","Balashev"), Author("P","","Noterdaeme"),
                Author("H","","Rahmani"), Author("V","V","Klimenko"),
                Author("C","","Ledoux"), Author("P","","Petitjean"),
                Author("R","","Srianand"), Author("A","V","Ivanchik"),
                Author("D","A","Varshalovich")],
              "CO-dark molecular gas at high redshift: very large H$_2$ content and high pressure in a low-metallicity damped Lyman alpha system",
              "MNRAS 470, 2890 - 2910", 2017)
)

# 176
references_arr.append(
    Reference([Author("S","A","Balashev"), Author("V","V","Klimenko"),
                Author("P","","Noterdaeme"), Author("J","K","Krogager"),
                Author("C","","Ledoux"), Author("A","V","Ivanchik"),
                Author("D","A","Varshalovich"), Author("P","","Petitjean")],
              "The cold neutral phase of the interstellar medium in high redshift galaxies",
              "Journal of Physics: Conference Series 1400, 022030", 2019)
)

# 177
references_arr.append(
    Reference([Author("S","A","Balashev"), Author("V","V","Klimenko"),
                Author("P","","Noterdaeme"), Author("J","K","Krogager"),
                Author("D","A","Varshalovich"), Author("A","V","Ivanchik"),
                Author("P","","Petitjean"), Author("R","","Srianand"),
                Author("C","","Ledoux")],
              "X-shooter observations of strong H$_2$-bearing DLAs at high redshift",
              "MNRAS 490, 2668-2678", 2019)
)







print([ref.authors[1].surname for ref in references_arr])