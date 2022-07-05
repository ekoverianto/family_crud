from Orang import Orang

class Keluarga(Orang):
    def __init__(self, nama='', jenis_kelamin='', id_parent=''):
        super().__init__(nama, jenis_kelamin)
        self.id_parent = id_parent

    # def getInfo(self):
    #     print(self.nama)
    #     print(self.jenis_kelamin)
    #     print(self.id_parent)

    def readData(self, db):
        cur = db.cursor()
        sql = 'SELECT * FROM keluarga'
        cur.execute(sql)
        res = cur.fetchall()
        if cur.rowcount == 0:
            print('Data tidak ada')
        else:
            for i in res:
                print(i)

    def createData(self, db):
        sql = 'INSERT INTO keluarga (nama, jenis_kelamin, id_parent) VALUES (%s, %s, %s)'
        data = (self.nama, self.jenis_kelamin, self.id_parent)
        db.cursor().execute(sql, data)
        db.commit()
        print('Data berhasil disimpan')

    def updateData(self, db, id):
        sql = 'UPDATE keluarga SET nama=%s, jenis_kelamin=%s, id_parent=%s WHERE id=%s'
        data = (self.nama, self.jenis_kelamin, self.id_parent, id)
        db.cursor().execute(sql, data)
        db.commit()
        print('Data berhasil diubah')

    def deleteData(self, db, id):
        sql = 'DELETE FROM keluarga WHERE id=%s'
        data = (id,)
        db.cursor().execute(sql, data)
        db.commit()
        print('Data berhasil di hapus')