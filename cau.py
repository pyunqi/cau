#-*- coding: utf-8 -*-
from MysqlConnection import *
import uniout

dbConnection  = DBConnection()
cursor = dbConnection.getConnection().cursor()

points_query = ("SELECT point,dealer_id,name,cont,email,area_id,area,user_id FROM test.exmares where dealer_id = %s and type_id =  %s order by point desc limit 1")

points_query_sadt = ("SELECT point,dealer_id,name,cont,email,area_id,area,identifiaction,user_id FROM test.exmares where dealer_id = %s and type_id =  %s order by point desc")

res_in_query = ("INSERT INTO `test`.`dealer_res`(`dealer_id`,`name`,`cont`,`email`,`area_id`,`area`,`sa`,`dt`,`point`,`dr`) VALUES( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

for dealer in range (1,350):
    dealer_info = ''
    sa = 'no'
    dt = 'no'
    di = 'no'
    points  = 0
    for i in range(1,6):
        if (i == 1 or i == 4):
            flag =  True
            rows_count = cursor.execute(points_query_sadt, (dealer,i))
            for (point,dealer_id,name,cont,email,area_id,area,identifiaction,user_id) in cursor:
                dealer_info = (point,dealer_id,name,cont,email,area_id,area)
                if(flag):
                    points = points+point
                    flag = False
                if (identifiaction == 'yes' and i == 1):
                    sa = 'yes'
                elif identifiaction == 'yes' :
                    dt = 'yes'
        else:
            cursor.execute(points_query, (dealer,i))
            for (point,dealer_id,name,cont,email,area_id,area,user_id) in cursor:
                dealer_info = (point,dealer_id,name,cont,email,area_id,area)
                points = points+point
    print points

    try: 
        sa 
    except NameError: 
        print "xxxf"
        sa = 'no'
    try: 
        dt 
    except  NameError: 
        dt = 'no'
    if (sa == 'yes' and dt == 'yes'):
        di = 'yes'
    else:
        di = 'no'
    if(dealer_info != ''):
        cursor.execute(res_in_query,(dealer_info[1],dealer_info[2],dealer_info[3],dealer_info[4],dealer_info[5],dealer_info[6],sa,dt,points,di))
cursor.close()
dbConnection.closeConnection()