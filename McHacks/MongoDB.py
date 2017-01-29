from pymongo import MongoClient
import datetime

class Connection:
	client = None

	def verifyConnection(self):
		if Connection.client is None:
			try:
				Connection.client = MongoClient('localhost', 27017)
				db = Connection.client.database_names()
			except Exception as e:
				Connection.client = None
			finally:
				pass

		return Connection.client is not None

	def closeConnection(self):
		Connection.client.close()


class MongoDB:

    def createConnection(self):
        databaseBigEarth = self.client.BigEarth
        collectionBigEarth = databaseBigEarth.BigEarth

    #def insertDocumentInsideDatabase(self,a ,b ,c ,d, e, f, g, h, i, j, k, l, m, n, o):

    def savePerson(firstName, lastName, age, previousJobs, id=None):
        doc = {
            "firstName": firstName,
            "lastName": lastName,
            "age": age,
            "jobs": previousJobs
        }

        if id is None:
            # insert
            Connection.client.ficheGFP.personnes.insert(doc)
        else:
            # update
            query = {"_id": id}
            Connection.client.ficheGFP.personnes.update(query, doc)

    def search(age, requiredJob, limit):
        results = []
        if len(age) > 0 or len(requiredJob) > 0:
            query = {}
            if len(age) > 0:
                query["age"] = {"$gte": int(age)}
            if len(requiredJob) > 0:
                query["jobs"] = requiredJob
            curseur = Connection.client.ficheGFP.personnes.find(query).limit(limit)
            curseur.sort("firstName", 1)
            for doc in curseur:
                results.append(doc)

        return results

