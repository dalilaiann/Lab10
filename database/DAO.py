from database.DB_connect import DBConnect
from model.country import Country


class DAO():

    @staticmethod
    def getAllNodes(year):
        conn=DBConnect.get_connection()
        cursor=conn.cursor(dictionary=True)

        query="""select distinct(c.CCode), c.StateAbb, c.StateNme
                from country c, contiguity cc
                where c.CCode=cc.state1no and cc.state1no!=cc.state2no and year<=%s
                order by c.StateNme"""

        cursor.execute(query, (year,))
        res=[]

        for row in cursor:
            res.append(Country(**row))

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getEdges(year, idMap):
        conn=DBConnect.get_connection()
        cursor=conn.cursor(dictionary=True)

        query="""select state1no as s1, state2no as s2
                from contiguity
                where state1no<state2no and year<=%s and conttype=1"""


        cursor.execute(query, (year,))
        res=[]

        for row in cursor:
            res.append((idMap[row["s1"]], idMap[row["s2"]]))

        cursor.close()
        conn.close()
        return res


if __name__=="__main__":
    print(DAO.getAllNodes())
