from peewee import *
from clases import *


"""получить код поинта по его нзвнию
    нужно обвесить эксепшеном

"""
def get_id(string):
    return (Point.get(Point.name==string)).id
def get_instance_path_by_id(id):
    return (Floor.get(Floor.id==id)).picture_path





"""поинт - место на карте (кабинет, лвход на лестницу итд)"""
class Point(Model):
    id = PrimaryKeyField()
    name = CharField()                 #имя
    floor_index = IntegerField()        #индекс инстанса в котором находится точка
    path_for_point_pic = CharField()    #путь к картинке
    x = IntegerField()                  #координата х на карте инстанса
    y = IntegerField()                  #координата у на карте инстанса



""" этаж
    в близжайшем буду щем станет
    инстансом
    ИНСТАНС - фрагмент местности внутри здания (кусок циркуля, часть этажа)
    """
class Floor(Model):
    id=PrimaryKeyField()
    picture_path = CharField()   #
    #floor_index = IntegerField() # ошибка



class GraphConnection(Model):
    id=PrimaryKeyField()
    point1 = IntegerField()                 # указатель на поинт 1
    point2 = IntegerField()                 #указатель на поит 2
    connection_weight = IntegerField()      # вес соедиения
    connection_comment = CharField()        # коментарий соединения
    picture_path = CharField()              # путь к картинке соединения
    floor_index = IntegerField()            # указатель на инстанс если соединение внутри одного инстанса
    trans_floor_marker = BooleanField()     # маркер того что поинты входящие в соединение находятся в разных инстансах

""" таблица диалогов с тремя стилями
1й стиль - официальный
2й стиль - средний
3й стиль - не официал

например реплика с ключом 0
1й стиль - здравствуйте
2й стиль - привет
3й стиль - здарова братуха
"""
class Dialogs(Model):
    id=IntegerField()       #
    style1=CharField()      #
    style2=CharField()      #
    style3=CharField()      #



def get_building()->Building:
    building = Building()
    building.graph=get_graph()
    building.floors=Floor.select()
    return building



def get_graph()->Graph:
    graph=Graph()
    graph.connections=GraphConnection.select()
    graph.points=Point.select()
    graph.points_dict={}
    for point in graph.points:
        graph.points_dict[point.id]=point
    return graph

#Floor.create_table(True)
#Point.create_table(True)
#GraphConnection.create_table(True)
#Dialogs.create_table(True)

#grandma = Person.select().where(Person.name == 'Grandma L.').get()