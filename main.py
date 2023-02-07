import json
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

users = [{'id': 1, 'first_name': 'Hudson', 'last_name': 'Pauloh', 'age': 31, 'email': 'elliot16@mymail.com', 'role': 'customer', 'phone': '6197021684'}, {'id': 2, 'first_name': 'George', 'last_name': 'Matter', 'age': 41, 'email': 'lawton46@mymail.com', 'role': 'executor', 'phone': '8314786677'}, {'id': 3, 'first_name': 'Grant', 'last_name': 'Traviser', 'age': 23, 'email': 'tobias45@mymail.com', 'role': 'customer', 'phone': '9528815998'}, {'id': 4, 'first_name': 'Malcolm', 'last_name': 'Douglasoh', 'age': 28, 'email': 'daniel37@mymail.com', 'role': 'customer', 'phone': '6428998684'}, {'id': 5, 'first_name': 'Lester', 'last_name': 'Archibaldoh', 'age': 20, 'email': 'joshua18@mymail.com', 'role': 'executor', 'phone': '8825887253'}, {'id': 6, 'first_name': 'Gareth', 'last_name': 'Tobiaser', 'age': 27, 'email': 'barnabe18@mymail.com', 'role': 'customer', 'phone': '8254630383'}, {'id': 7, 'first_name': 'Vivian', 'last_name': 'Philipik', 'age': 49, 'email': 'jaime46@mymail.com', 'role': 'customer', 'phone': '9884423362'}, {'id': 8, 'first_name': 'Nate', 'last_name': 'Travisik', 'age': 18, 'email': 'nate46@mymail.com', 'role': 'executor', 'phone': '8353350197'}, {'id': 9, 'first_name': 'Norman', 'last_name': 'Larryoh', 'age': 37, 'email': 'shahaf06@mymail.com', 'role': 'executor', 'phone': '6448371821'}, {'id': 10, 'first_name': 'George', 'last_name': 'Emiloh', 'age': 49, 'email': 'grant35@mymail.com', 'role': 'executor', 'phone': '8872495923'}, {'id': 11, 'first_name': 'Graham', 'last_name': 'Reginalder', 'age': 20, 'email': 'george38@mymail.com', 'role': 'executor', 'phone': '7356168167'}, {'id': 12, 'first_name': 'Malcolm', 'last_name': 'Jameser', 'age': 22, 'email': 'graham27@mymail.com', 'role': 'executor', 'phone': '8967033901'}, {'id': 13, 'first_name': 'Marvin', 'last_name': 'Austenoh', 'age': 19, 'email': 'nicholas46@mymail.com', 'role': 'executor', 'phone': '6723331776'}, {'id': 14, 'first_name': 'Jack', 'last_name': 'Normaner', 'age': 32, 'email': 'myron25@mymail.com', 'role': 'executor', 'phone': '7490416454'}, {'id': 15, 'first_name': 'Travis', 'last_name': 'Chanceer', 'age': 20, 'email': 'kurt17@mymail.com', 'role': 'customer', 'phone': '9491120005'}, {'id': 16, 'first_name': 'Neil', 'last_name': 'Ronaldoh', 'age': 43, 'email': 'john36@mymail.com', 'role': 'customer', 'phone': '8913865074'}, {'id': 17, 'first_name': 'Shahaf', 'last_name': 'Larryoh', 'age': 33, 'email': 'ebenezer08@mymail.com', 'role': 'customer', 'phone': '6514816015'}, {'id': 18, 'first_name': 'Wayne', 'last_name': 'Markik', 'age': 43, 'email': 'larry37@mymail.com', 'role': 'executor', 'phone': '6496155163'}, {'id': 19, 'first_name': 'Dougie', 'last_name': 'Adrianik', 'age': 23, 'email': 'vincent46@mymail.com', 'role': 'customer', 'phone': '9965723667'}, {'id': 20, 'first_name': 'Vincent', 'last_name': 'Davider', 'age': 47, 'email': 'cuthbert36@mymail.com', 'role': 'executor', 'phone': '7125872211'}, {'id': 21, 'first_name': 'Addison', 'last_name': 'Reginaldik', 'age': 48, 'email': 'reginald25@mymail.com', 'role': 'executor', 'phone': '9963171227'}, {'id': 22, 'first_name': 'Arthur', 'last_name': 'Chanceik', 'age': 23, 'email': 'stephen25@mymail.com', 'role': 'executor', 'phone': '6786170626'}, {'id': 23, 'first_name': 'Earl', 'last_name': 'Frankliner', 'age': 40, 'email': 'lawton47@mymail.com', 'role': 'executor', 'phone': '7851277139'}, {'id': 24, 'first_name': 'Marshall', 'last_name': 'Arloer', 'age': 43, 'email': 'floyd36@mymail.com', 'role': 'executor', 'phone': '6442333628'}, {'id': 25, 'first_name': 'Mark', 'last_name': 'Nicholasoh', 'age': 33, 'email': 'nicolas35@mymail.com', 'role': 'customer', 'phone': '8143159413'}, {'id': 26, 'first_name': 'Edgar', 'last_name': 'Arthurik', 'age': 18, 'email': 'vincent45@mymail.com', 'role': 'executor', 'phone': '6159310195'}, {'id': 27, 'first_name': 'Travis', 'last_name': 'Pelegoh', 'age': 24, 'email': 'jeffrey05@mymail.com', 'role': 'executor', 'phone': '9300837797'}, {'id': 28, 'first_name': 'Nate', 'last_name': 'Albertoh', 'age': 30, 'email': 'peleg36@mymail.com', 'role': 'executor', 'phone': '6158921977'}, {'id': 29, 'first_name': 'Cardew', 'last_name': 'Hughik', 'age': 28, 'email': 'jolyon37@mymail.com', 'role': 'executor', 'phone': '6787970230'}, {'id': 30, 'first_name': 'Graham', 'last_name': 'Joeyoh', 'age': 28, 'email': 'myron26@mymail.com', 'role': 'executor', 'phone': '6962652739'}]
orders = [{'id': 0, 'name': 'Встретить тетю на вокзале', 'description': 'Встретить тетю на вокзале с табличкой. Отвезти ее в магазин, помочь погрузить покупки. Привезти тетю домой, занести покупки и чемодан в квартиру', 'start_date': '02/08/2013', 'end_date': '03/28/2057', 'address': '4759 William Haven Apt. 194\nWest Corey, TX 43780', 'price': 5512, 'customer_id': 3, 'executor_id': 6}, {'id': 1, 'name': 'Позвать в гости девушку', 'description': 'Позвать в гости девушку и шикануть перед ней — заказать коробку конфет с доставкой на дом', 'start_date': '01/24/2016', 'end_date': '03/10/2076', 'address': '9387 Grimes Green Apt. 801\nPagetown, NM 44165', 'price': 2800, 'customer_id': 18, 'executor_id': 25}, {'id': 2, 'name': 'Требуется уборка квартиры. Площадь', 'description': 'Требуется уборка квартиры. Площадь 85 м²: спальня, детская, гостиная, кухня. Санузел раздельный. Фотографии прикладываю.', 'start_date': '04/19/2008', 'end_date': '05/23/2099', 'address': '93328 Davis Island\nRodriguezside, VT 16860', 'price': 2320, 'customer_id': 16, 'executor_id': 19}, {'id': 3, 'name': 'Сделать разом мелкий ремонт:', 'description': 'Сделать разом мелкий ремонт: повесить полочку в ванной, заклеить щели в окнах, починить выпадающую розетку, смазать дверные петли', 'start_date': '08/17/2018', 'end_date': '04/15/2045', 'address': '894 Davis Union\nStewartbury, HI 25324', 'price': 3427, 'customer_id': 24, 'executor_id': 25}, {'id': 4, 'name': 'Вынести на помойку старый', 'description': 'Вынести на помойку старый шкаф. Отвезти книжки в библиотеку, отдать ненужную одежду в пункт приема', 'start_date': '05/09/2006', 'end_date': '06/27/2004', 'address': '1122 Megan Squares Suite 848\nPort Jason, OR 55475', 'price': 5184, 'customer_id': 15, 'executor_id': 5}, {'id': 5, 'name': 'Сделать разом мелкий ремонт:', 'description': 'Сделать разом мелкий ремонт: повесить полочку в ванной, заклеить щели в окнах, починить выпадающую розетку, смазать дверные петли', 'start_date': '09/22/2019', 'end_date': '06/15/2037', 'address': '59179 Bruce Gardens Apt. 413\nLauramouth, AR 13687', 'price': 7378, 'customer_id': 6, 'executor_id': 28}, {'id': 6, 'name': 'Вынести на помойку старый', 'description': 'Вынести на помойку старый шкаф. Отвезти книжки в библиотеку, отдать ненужную одежду в пункт приема', 'start_date': '12/23/2004', 'end_date': '12/14/2094', 'address': '13991 Davis Village\nNorth Catherineborough, VT 16740', 'price': 401, 'customer_id': 0, 'executor_id': 7}, {'id': 7, 'name': 'Позвать в гости девушку', 'description': 'Позвать в гости девушку и шикануть перед ней — заказать коробку конфет с доставкой на дом', 'start_date': '04/21/2016', 'end_date': '08/28/2028', 'address': '086 Mary Cliff\nNorth Deborah, NE 24135', 'price': 4556, 'customer_id': 18, 'executor_id': 27}, {'id': 8, 'name': 'Встретить тетю на вокзале', 'description': 'Встретить тетю на вокзале с табличкой. Отвезти ее в магазин, помочь погрузить покупки. Привезти тетю домой, занести покупки и чемодан в квартиру', 'start_date': '01/28/2002', 'end_date': '07/17/2068', 'address': '634 Strong Mountains\nLake Emily, AR 89132', 'price': 4633, 'customer_id': 15, 'executor_id': 11}, {'id': 9, 'name': 'Сделать уборку в квартире:', 'description': 'Сделать уборку в квартире: помыть пол и протереть пыль, помыть посуду, погладить одежду и развесить ее в шкафу', 'start_date': '05/20/2005', 'end_date': '01/15/2022', 'address': '97207 Mccullough Well Suite 564\nNew Hannah, WA 10865', 'price': 6466, 'customer_id': 5, 'executor_id': 11}, {'id': 10, 'name': 'Организовать переезд: упаковать вещи', 'description': 'Организовать переезд: упаковать вещи в коробки, погрузить, перевезти на машине, разгрузить и расставить всё по местам', 'start_date': '06/06/2011', 'end_date': '03/21/2006', 'address': '75945 Jennifer Loaf\nPooleland, PA 25707', 'price': 491, 'customer_id': 3, 'executor_id': 18}, {'id': 11, 'name': 'Позвать в гости девушку', 'description': 'Позвать в гости девушку и шикануть перед ней — заказать коробку конфет с доставкой на дом', 'start_date': '05/18/2011', 'end_date': '10/14/2021', 'address': '9606 Barton Station Apt. 271\nJacquelinemouth, NM 74085', 'price': 3355, 'customer_id': 5, 'executor_id': 11}, {'id': 12, 'name': 'Встретить тетю на вокзале', 'description': 'Встретить тетю на вокзале с табличкой. Отвезти ее в магазин, помочь погрузить покупки. Привезти тетю домой, занести покупки и чемодан в квартиру', 'start_date': '07/19/2020', 'end_date': '01/04/2000', 'address': '4706 Amy Roads Apt. 206\nStewartborough, VT 99428', 'price': 1845, 'customer_id': 16, 'executor_id': 7}, {'id': 13, 'name': 'Два раза в день', 'description': 'Два раза в день гулять с собакой, пока хозяева уехали путешествовать', 'start_date': '01/30/2000', 'end_date': '12/21/2091', 'address': '19344 Craig Walk\nBurtontown, NV 15676', 'price': 3944, 'customer_id': 6, 'executor_id': 24}, {'id': 14, 'name': 'Сделать разом мелкий ремонт:', 'description': 'Сделать разом мелкий ремонт: повесить полочку в ванной, заклеить щели в окнах, починить выпадающую розетку, смазать дверные петли', 'start_date': '09/22/2008', 'end_date': '02/27/2018', 'address': '24000 Erin Point Suite 590\nJosephmouth, NE 49318', 'price': 1360, 'customer_id': 16, 'executor_id': 27}, {'id': 15, 'name': 'Сделать разом мелкий ремонт:', 'description': 'Сделать разом мелкий ремонт: повесить полочку в ванной, заклеить щели в окнах, починить выпадающую розетку, смазать дверные петли', 'start_date': '04/21/2018', 'end_date': '04/06/2024', 'address': '22455 Higgins Junction Apt. 042\nNew Keith, OH 17493', 'price': 950, 'customer_id': 0, 'executor_id': 8}, {'id': 16, 'name': 'Нужно забрать пакет с', 'description': 'Нужно забрать пакет с документами c Черняховского, 4а и отвезти его на Плющиху, 20', 'start_date': '12/25/2009', 'end_date': '08/21/2015', 'address': '42814 Houston Hills\nRodriguezside, NJ 62629', 'price': 1124, 'customer_id': 5, 'executor_id': 17}, {'id': 17, 'name': 'Сделать уборку в квартире:', 'description': 'Сделать уборку в квартире: помыть пол и протереть пыль, помыть посуду, погладить одежду и развесить ее в шкафу', 'start_date': '06/21/2011', 'end_date': '10/09/2046', 'address': '760 Rogers Spur\nEast Courtney, SC 11894', 'price': 5450, 'customer_id': 3, 'executor_id': 5}, {'id': 18, 'name': 'Два раза в день', 'description': 'Два раза в день гулять с собакой, пока хозяева уехали путешествовать', 'start_date': '03/29/2002', 'end_date': '07/10/2011', 'address': '60168 West Overpass\nSouth Christopher, KS 77208', 'price': 747, 'customer_id': 2, 'executor_id': 12}, {'id': 19, 'name': 'Вынести на помойку старый', 'description': 'Вынести на помойку старый шкаф. Отвезти книжки в библиотеку, отдать ненужную одежду в пункт приема', 'start_date': '09/01/2005', 'end_date': '09/09/2058', 'address': '08731 Sanders Fords\nPort Jasonberg, ID 60585', 'price': 8229, 'customer_id': 6, 'executor_id': 10}, {'id': 20, 'name': 'Сделать уборку в квартире:', 'description': 'Сделать уборку в квартире: помыть пол и протереть пыль, помыть посуду, погладить одежду и развесить ее в шкафу', 'start_date': '11/11/2012', 'end_date': '03/21/2049', 'address': '97296 Rich Park\nMarthafort, TN 26976', 'price': 2447, 'customer_id': 15, 'executor_id': 14}, {'id': 21, 'name': 'Сделать уборку в квартире:', 'description': 'Сделать уборку в квартире: помыть пол и протереть пыль, помыть посуду, погладить одежду и развесить ее в шкафу', 'start_date': '06/20/2018', 'end_date': '12/27/2082', 'address': 'USS Peterson\nFPO AP 42215', 'price': 4161, 'customer_id': 18, 'executor_id': 16}, {'id': 22, 'name': 'Нужно забрать пакет с', 'description': 'Нужно забрать пакет с документами c Черняховского, 4а и отвезти его на Плющиху, 20', 'start_date': '12/13/2010', 'end_date': '10/29/2004', 'address': '269 Robbins Valley Suite 118\nNorth Jeffreyton, AL 59298', 'price': 6285, 'customer_id': 5, 'executor_id': 8}, {'id': 23, 'name': 'Вынести на помойку старый', 'description': 'Вынести на помойку старый шкаф. Отвезти книжки в библиотеку, отдать ненужную одежду в пункт приема', 'start_date': '04/01/2011', 'end_date': '11/13/2021', 'address': '8688 Audrey Springs Apt. 634\nPetersenfort, WY 51431', 'price': 7101, 'customer_id': 18, 'executor_id': 1}, {'id': 24, 'name': 'Организовать переезд: упаковать вещи', 'description': 'Организовать переезд: упаковать вещи в коробки, погрузить, перевезти на машине, разгрузить и расставить всё по местам', 'start_date': '08/31/2020', 'end_date': '10/22/2079', 'address': '024 Cook Park\nSherriport, MT 50853', 'price': 7132, 'customer_id': 14, 'executor_id': 25}, {'id': 25, 'name': 'Встретить тетю на вокзале', 'description': 'Встретить тетю на вокзале с табличкой. Отвезти ее в магазин, помочь погрузить покупки. Привезти тетю домой, занести покупки и чемодан в квартиру', 'start_date': '01/20/2013', 'end_date': '06/21/2008', 'address': '45007 Thomas Way\nLake Hollystad, AZ 80687', 'price': 2397, 'customer_id': 16, 'executor_id': 3}, {'id': 26, 'name': 'Требуется уборка квартиры. Площадь', 'description': 'Требуется уборка квартиры. Площадь 85 м²: спальня, детская, гостиная, кухня. Санузел раздельный. Фотографии прикладываю.', 'start_date': '11/12/2015', 'end_date': '08/17/2052', 'address': '2009 Crystal Cove\nJamesfort, AR 80470', 'price': 6684, 'customer_id': 14, 'executor_id': 16}, {'id': 27, 'name': 'Позвать в гости девушку', 'description': 'Позвать в гости девушку и шикануть перед ней — заказать коробку конфет с доставкой на дом', 'start_date': '11/24/2015', 'end_date': '08/11/2083', 'address': '194 Susan Loaf Suite 183\nPort Philipstad, ID 60200', 'price': 3058, 'customer_id': 24, 'executor_id': 20}, {'id': 28, 'name': 'Вынести на помойку старый', 'description': 'Вынести на помойку старый шкаф. Отвезти книжки в библиотеку, отдать ненужную одежду в пункт приема', 'start_date': '02/18/2012', 'end_date': '01/06/2086', 'address': '74089 Jerry Trail\nHunterville, NE 74689', 'price': 4786, 'customer_id': 16, 'executor_id': 15}, {'id': 29, 'name': 'Организовать переезд: упаковать вещи', 'description': 'Организовать переезд: упаковать вещи в коробки, погрузить, перевезти на машине, разгрузить и расставить всё по местам', 'start_date': '05/12/2014', 'end_date': '06/09/2011', 'address': 'USCGC Brown\nFPO AA 20968', 'price': 4765, 'customer_id': 0, 'executor_id': 8}, {'id': 30, 'name': 'Организовать переезд: упаковать вещи', 'description': 'Организовать переезд: упаковать вещи в коробки, погрузить, перевезти на машине, разгрузить и расставить всё по местам', 'start_date': '01/16/2001', 'end_date': '10/18/2060', 'address': '75415 David Square Apt. 552\nPort Terristad, PA 19282', 'price': 2930, 'customer_id': 6, 'executor_id': 12}, {'id': 31, 'name': 'Два раза в день', 'description': 'Два раза в день гулять с собакой, пока хозяева уехали путешествовать', 'start_date': '01/28/2007', 'end_date': '06/09/2000', 'address': '045 Sarah Fort\nEast Shawn, MI 93231', 'price': 3397, 'customer_id': 18, 'executor_id': 22}, {'id': 32, 'name': 'Нужно забрать пакет с', 'description': 'Нужно забрать пакет с документами c Черняховского, 4а и отвезти его на Плющиху, 20', 'start_date': '10/14/2008', 'end_date': '09/18/2017', 'address': '5744 White Common\nNew Beverlyburgh, FL 16915', 'price': 236, 'customer_id': 2, 'executor_id': 8}, {'id': 33, 'name': 'Встретить тетю на вокзале', 'description': 'Встретить тетю на вокзале с табличкой. Отвезти ее в магазин, помочь погрузить покупки. Привезти тетю домой, занести покупки и чемодан в квартиру', 'start_date': '08/01/2007', 'end_date': '12/29/2042', 'address': '45602 Phillip Squares\nEast Robertside, WA 19150', 'price': 4174, 'customer_id': 14, 'executor_id': 19}, {'id': 34, 'name': 'Требуется уборка квартиры. Площадь', 'description': 'Требуется уборка квартиры. Площадь 85 м²: спальня, детская, гостиная, кухня. Санузел раздельный. Фотографии прикладываю.', 'start_date': '02/10/2020', 'end_date': '06/17/2057', 'address': '37580 Ortiz Mall Suite 735\nStephanieland, WY 14737', 'price': 1642, 'customer_id': 2, 'executor_id': 20}, {'id': 35, 'name': 'Сделать уборку в квартире:', 'description': 'Сделать уборку в квартире: помыть пол и протереть пыль, помыть посуду, погладить одежду и развесить ее в шкафу', 'start_date': '06/04/2009', 'end_date': '04/07/2015', 'address': '762 Reynolds Gateway\nPetersonhaven, MI 61113', 'price': 2511, 'customer_id': 0, 'executor_id': 23}, {'id': 36, 'name': 'Организовать переезд: упаковать вещи', 'description': 'Организовать переезд: упаковать вещи в коробки, погрузить, перевезти на машине, разгрузить и расставить всё по местам', 'start_date': '06/27/2021', 'end_date': '09/26/2086', 'address': '0797 Jeffery Crescent\nAmyberg, VT 98982', 'price': 7372, 'customer_id': 2, 'executor_id': 23}, {'id': 37, 'name': 'Сделать уборку в квартире:', 'description': 'Сделать уборку в квартире: помыть пол и протереть пыль, помыть посуду, погладить одежду и развесить ее в шкафу', 'start_date': '01/15/2016', 'end_date': '08/05/2012', 'address': '640 Joseph Skyway\nNorth Jonathanhaven, OR 93557', 'price': 5894, 'customer_id': 16, 'executor_id': 14}, {'id': 38, 'name': 'Сделать уборку в квартире:', 'description': 'Сделать уборку в квартире: помыть пол и протереть пыль, помыть посуду, погладить одежду и развесить ее в шкафу', 'start_date': '06/25/2013', 'end_date': '07/04/2060', 'address': '4391 Chad Greens Suite 851\nPort Frank, LA 37561', 'price': 9671, 'customer_id': 14, 'executor_id': 4}, {'id': 39, 'name': 'Сделать уборку в квартире:', 'description': 'Сделать уборку в квартире: помыть пол и протереть пыль, помыть посуду, погладить одежду и развесить ее в шкафу', 'start_date': '09/08/2017', 'end_date': '04/18/2018', 'address': '168 Figueroa Turnpike\nKellystad, SC 18564', 'price': 7209, 'customer_id': 14, 'executor_id': 11}, {'id': 40, 'name': 'Два раза в день', 'description': 'Два раза в день гулять с собакой, пока хозяева уехали путешествовать', 'start_date': '05/05/2005', 'end_date': '10/12/2016', 'address': '9728 Gomez Mountains Suite 377\nTrevorton, ME 19219', 'price': 4798, 'customer_id': 18, 'executor_id': 12}, {'id': 41, 'name': 'Вынести на помойку старый', 'description': 'Вынести на помойку старый шкаф. Отвезти книжки в библиотеку, отдать ненужную одежду в пункт приема', 'start_date': '11/10/2016', 'end_date': '02/18/2007', 'address': '57608 Gloria Common\nSmithton, RI 00991', 'price': 6716, 'customer_id': 6, 'executor_id': 3}, {'id': 42, 'name': 'Нужно забрать пакет с', 'description': 'Нужно забрать пакет с документами c Черняховского, 4а и отвезти его на Плющиху, 20', 'start_date': '03/13/2009', 'end_date': '02/26/2087', 'address': '94316 Moran Lights\nWest Robert, TX 57552', 'price': 2570, 'customer_id': 18, 'executor_id': 24}, {'id': 43, 'name': 'Сделать разом мелкий ремонт:', 'description': 'Сделать разом мелкий ремонт: повесить полочку в ванной, заклеить щели в окнах, починить выпадающую розетку, смазать дверные петли', 'start_date': '01/13/2005', 'end_date': '11/16/2060', 'address': 'USNS Warren\nFPO AE 27877', 'price': 3666, 'customer_id': 2, 'executor_id': 16}, {'id': 44, 'name': 'Требуется уборка квартиры. Площадь', 'description': 'Требуется уборка квартиры. Площадь 85 м²: спальня, детская, гостиная, кухня. Санузел раздельный. Фотографии прикладываю.', 'start_date': '05/10/2006', 'end_date': '06/11/2060', 'address': '7633 Bentley Radial Apt. 603\nPort Jacobton, SC 89301', 'price': 4354, 'customer_id': 0, 'executor_id': 12}, {'id': 45, 'name': 'Требуется уборка квартиры. Площадь', 'description': 'Требуется уборка квартиры. Площадь 85 м²: спальня, детская, гостиная, кухня. Санузел раздельный. Фотографии прикладываю.', 'start_date': '11/24/2005', 'end_date': '09/20/2031', 'address': '845 Ellis Roads\nCarpenterfort, VT 62845', 'price': 6590, 'customer_id': 24, 'executor_id': 16}, {'id': 46, 'name': 'Организовать переезд: упаковать вещи', 'description': 'Организовать переезд: упаковать вещи в коробки, погрузить, перевезти на машине, разгрузить и расставить всё по местам', 'start_date': '05/01/2007', 'end_date': '11/22/2045', 'address': '25040 Bryce Meadow\nNew Randy, IN 59968', 'price': 3135, 'customer_id': 0, 'executor_id': 18}, {'id': 47, 'name': 'Сделать уборку в квартире:', 'description': 'Сделать уборку в квартире: помыть пол и протереть пыль, помыть посуду, погладить одежду и развесить ее в шкафу', 'start_date': '07/24/2006', 'end_date': '03/16/2046', 'address': '5875 Johnson Cape\nWest Christopher, NC 45818', 'price': 3544, 'customer_id': 15, 'executor_id': 20}, {'id': 48, 'name': 'Требуется уборка квартиры. Площадь', 'description': 'Требуется уборка квартиры. Площадь 85 м²: спальня, детская, гостиная, кухня. Санузел раздельный. Фотографии прикладываю.', 'start_date': '05/22/2006', 'end_date': '06/10/2027', 'address': '8647 Wiggins Garden Apt. 481\nSouth Tylermouth, MT 65195', 'price': 4712, 'customer_id': 24, 'executor_id': 12}, {'id': 49, 'name': 'Сделать разом мелкий ремонт:', 'description': 'Сделать разом мелкий ремонт: повесить полочку в ванной, заклеить щели в окнах, починить выпадающую розетку, смазать дверные петли', 'start_date': '09/02/2015', 'end_date': '11/24/2059', 'address': '12637 Lisa Points\nWilliamsburgh, NM 29343', 'price': 8490, 'customer_id': 24, 'executor_id': 0}]
offers = [{'id': 0, 'order_id': 36, 'executor_id': 10}, {'id': 1, 'order_id': 35, 'executor_id': 4}, {'id': 2, 'order_id': 35, 'executor_id': 21}, {'id': 3, 'order_id': 47, 'executor_id': 28}, {'id': 4, 'order_id': 18, 'executor_id': 25}, {'id': 5, 'order_id': 22, 'executor_id': 25}, {'id': 6, 'order_id': 11, 'executor_id': 11}, {'id': 7, 'order_id': 10, 'executor_id': 20}, {'id': 8, 'order_id': 18, 'executor_id': 12}, {'id': 9, 'order_id': 36, 'executor_id': 1}, {'id': 10, 'order_id': 20, 'executor_id': 7}, {'id': 11, 'order_id': 43, 'executor_id': 8}, {'id': 12, 'order_id': 37, 'executor_id': 28}, {'id': 13, 'order_id': 37, 'executor_id': 8}, {'id': 14, 'order_id': 24, 'executor_id': 1}, {'id': 15, 'order_id': 18, 'executor_id': 8}, {'id': 16, 'order_id': 28, 'executor_id': 11}, {'id': 17, 'order_id': 23, 'executor_id': 25}, {'id': 18, 'order_id': 19, 'executor_id': 12}, {'id': 19, 'order_id': 34, 'executor_id': 22}, {'id': 20, 'order_id': 18, 'executor_id': 20}, {'id': 21, 'order_id': 17, 'executor_id': 9}, {'id': 22, 'order_id': 20, 'executor_id': 28}, {'id': 23, 'order_id': 1, 'executor_id': 4}, {'id': 24, 'order_id': 6, 'executor_id': 23}, {'id': 25, 'order_id': 47, 'executor_id': 23}, {'id': 26, 'order_id': 29, 'executor_id': 22}, {'id': 27, 'order_id': 5, 'executor_id': 13}, {'id': 28, 'order_id': 43, 'executor_id': 20}, {'id': 29, 'order_id': 33, 'executor_id': 19}, {'id': 30, 'order_id': 48, 'executor_id': 28}, {'id': 31, 'order_id': 42, 'executor_id': 1}, {'id': 32, 'order_id': 41, 'executor_id': 10}, {'id': 33, 'order_id': 9, 'executor_id': 21}, {'id': 34, 'order_id': 2, 'executor_id': 25}, {'id': 35, 'order_id': 25, 'executor_id': 28}, {'id': 36, 'order_id': 30, 'executor_id': 13}, {'id': 37, 'order_id': 1, 'executor_id': 9}, {'id': 38, 'order_id': 47, 'executor_id': 21}, {'id': 39, 'order_id': 40, 'executor_id': 8}, {'id': 40, 'order_id': 23, 'executor_id': 23}, {'id': 41, 'order_id': 18, 'executor_id': 20}, {'id': 42, 'order_id': 11, 'executor_id': 23}, {'id': 43, 'order_id': 18, 'executor_id': 9}, {'id': 44, 'order_id': 38, 'executor_id': 11}, {'id': 45, 'order_id': 27, 'executor_id': 7}, {'id': 46, 'order_id': 3, 'executor_id': 19}, {'id': 47, 'order_id': 13, 'executor_id': 13}, {'id': 48, 'order_id': 36, 'executor_id': 7}, {'id': 49, 'order_id': 0, 'executor_id': 13}, {'id': 50, 'order_id': 33, 'executor_id': 28}, {'id': 51, 'order_id': 29, 'executor_id': 27}, {'id': 52, 'order_id': 48, 'executor_id': 17}, {'id': 53, 'order_id': 33, 'executor_id': 22}, {'id': 54, 'order_id': 18, 'executor_id': 22}, {'id': 55, 'order_id': 8, 'executor_id': 11}, {'id': 56, 'order_id': 8, 'executor_id': 7}, {'id': 57, 'order_id': 43, 'executor_id': 11}, {'id': 58, 'order_id': 0, 'executor_id': 1}, {'id': 59, 'order_id': 45, 'executor_id': 28}, {'id': 60, 'order_id': 10, 'executor_id': 28}, {'id': 61, 'order_id': 35, 'executor_id': 26}, {'id': 62, 'order_id': 25, 'executor_id': 28}, {'id': 63, 'order_id': 18, 'executor_id': 17}, {'id': 64, 'order_id': 48, 'executor_id': 8}, {'id': 65, 'order_id': 40, 'executor_id': 17}, {'id': 66, 'order_id': 47, 'executor_id': 19}, {'id': 67, 'order_id': 13, 'executor_id': 11}, {'id': 68, 'order_id': 46, 'executor_id': 27}, {'id': 69, 'order_id': 45, 'executor_id': 28}]


#Создаем нужные модели
with app.app_context():
    class User(db.Model):
        __tablename__ = "users"
        id = db.Column(db.Integer, primary_key=True)
        first_name = db.Column(db.Text(100))
        last_name = db.Column(db.Text(100))
        age = db.Column(db.Integer)
        email = db.Column(db.Text(100))
        role = db.Column(db.Text(100))
        phone = db.Column(db.Text(100))



with app.app_context():
    class Orders(db.Model):
        __tablename__ = "orders"
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.Text)
        description = db.Column(db.Text)
        start_date = db.Column(db.Text)
        end_date = db.Column(db.Text)
        address = db.Column(db.Text)
        price = db.Column(db.Integer)
        customer_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
        executor_id = db.Column(db.Integer, db.ForeignKey('users.id'))

        users = relationship("User")
        orders = relationship("Orders")

with app.app_context():
    class Offers(db.Model):
        __tablename__ = "offers"
        id = db.Column(db.Integer, primary_key=True)
        order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
        executor_id = db.Column(db.Integer, db.ForeignKey('users.id'))

        users = relationship("User")

#Загружаем данные
with app.app_context():
    db.drop_all()
    db.create_all()
    for user in users:
        all_user = User(id=user['id'], first_name=user['first_name'], last_name=user['last_name'],
                        age=user['age'], email=user['email'], role=user['role'], phone=user['phone'])
        db.session.add(all_user)
        db.session.commit()

    for order in orders:

        all_orders = Orders(id=order['id'], name=order['name'], description=order['description'],
                            start_date=order['start_date'],
                            end_date=order['end_date'], address=order['address'],
                            price=order['price'], customer_id=order['customer_id'], executor_id=order['executor_id'])
        db.session.add(all_orders)
        db.session.commit()

    for offer in offers:
        all_offers = Offers(id=offer['id'], order_id=offer['order_id'],
                            executor_id=offer['executor_id'])

        db.session.add(all_offers)
        db.session.commit()
#Создаем представление для пользователей, которое обрабатывало бы GET-запросы для всех пользователей
# и одного пользователя по идентификатору /users/1
# и реализуем создания пользователя по средоством метода Post.
# Реализуем  обновление пользователя user посредством метода PUT
# Реализуем удаление пользователя
@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        users = User.query.all()
        user_response = []

        for us in users:
            user_response.append(
                {'id': us.id,
                 'first_name': us.first_name,
                 'last_name': us.last_name,
                 'age': us.age,
                 'email': us.email,
                 'role': us.role,
                 'phone': us.phone}
            )
        return json.dumps(user_response)
    elif request.method == 'POST':
        user_data = json.loads(request.data)
        db.session.add(User(**user_data))
        db.session.commit()
        return ''

@app.route("/users/<int:sid>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_users(sid: int):
    if request.method == 'GET':
        users = User.query.get(sid)
        if users is None:
            return "user not found"

        return json.dumps(
                {'id': users.id,
                 'first_name': users.first_name,
                 'last_name': users.last_name,
                 'age': users.age,
                 'email': users.email,
                 'role': users.role,
                 'phone': users.phone}
            )
    elif request.method == 'DELETE':
        users = User.query.get(sid)
        db.session.delete(users)
        db.session.commit()
        return ''
    elif request.method == 'PUT':
        user_data = json.loads(request.data)
        user = User.query.get(sid)
        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.age = user_data['age']
        user.email = user_data['email']
        user.role = user_data['role']
        user.phone = user_data['phone']
        db.session.add(user)
        db.session.commit()
        return ''

#Создаем представление для заказа, которое обрабатывало бы GET-запросы для всех заказов
# и одного заказа по идентификатору /orders/1
# и реализуем создания заказа по средоством метода Post.
# Реализуем  обновление предложения orders посредством метода PUT
# Реализуем удаление заказа
@app.route('/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'GET':
        orders = Orders.query.all()
        user_response = []
        for orde in orders:
            user_response.append(
                {'id': orde.id,
                 'name': orde.name,
                 'description': orde.description,
                 'start_date': orde.start_date,
                 'end_date': orde.end_date,
                 'address': orde.address,
                 'price': orde.price,
                 'customer_id': orde.customer_id,
                 'executor_id': orde.executor_id}
            )
        return json.dumps(user_response, ensure_ascii=False)
    elif request.method == 'POST':
        order_data = json.loads(request.data)
        db.session.add(Orders(**order_data))
        db.session.commit()
        return ''

@app.route("/orders/<int:sid>", methods=['GET', 'PUTT', 'DELETE'])
def get_orders(sid: int):
    if request.method == 'GET':
        orders = Orders.query.get(sid)
        if users is None:
            return "user not found"

        return json.dumps(
            {'id': orders.id,
             'name': orders.name,
             'description': orders.description,
             'start_date': orders.start_date,
             'end_date': orders.end_date,
             'address': orders.address,
             'price': orders.price,
             'customer_id': orders.customer_id,
             'executor_id': orders.executor_id}
            )

    elif request.method == 'DELETE':
        orders = Orders.query.get(sid)
        db.session.delete(orders)
        db.session.commit()
        return ''
    elif request.method == 'PUT':
        order_data = json.loads(request.data)
        order = Orders.query.get(sid)
        order.name =  order_data['name']
        order.description =  order_data['description']
        order.start_date =  order_data['start_date']
        order.end_date =  order_data['end_date']
        order.address =  order_data['address']
        order.price =  order_data['price']
        order.customer_id =  order_data['customer_id']
        order.executor_id =  order_data['executor_id']
        db.session.add(order)
        db.session.commit()
        return ''

#Создаем представление для предложения, которое обрабатывало бы GET-запросы для всех предложений
# и одного предложения по идентификатору /offers/1
# и реализуем создания предложения по средоством метода Post.
# Реализуем  обновление предложения orders посредством метода PUT
# Реализуем удаление предложения
@app.route('/offers', methods=['GET', 'POST'])
def offers():
    if request.method == 'GET':
        offers = Offers.query.all()
        user_response = []

        for of in offers:
            user_response.append(
                {'id': of.id,
                 'order_id': of.order_id,
                 'executor_id': of.executor_id}
            )
        return json.dumps(user_response)
    elif request.method == 'POST':
        offer_data = json.load(offer.data)
        db.session.add(Offers(**offer_data))
        db.session.commit(offer_data)
        return ''

@app.route("/offers/<int:sid>", methods=['GET', 'POST'])
def get_offers(sid: int):
    if request.method == 'GET':
        offers = Offers.query.get(sid)
        if offers is None:
            return "user not found"

        return json.dumps(
            {'id': offers.id,
             'order_id': offers.order_id,
             'executor_id': offers.executor_id}
            )

    elif request.method == 'DELETE':
        offers = Offers.query.get(sid)
        db.session.delete(offers)
        db.session.commit()
        return ''
    elif request.method == 'PUT':
        orffer_data = json.loads(request.data)
        offers = Offers.query.get(sid)
        offers.order_id = orffer_data['order_id']
        offers.executor_id = orffer_data['executor_id']
        return ''


if __name__ == '__main__':
    app.run(debug=True)