# This gist contains a direct connection to a local PostgreSQL database
# called "suppliers" where the username and password parameters are "postgres"

# This code is adapted from the tutorial hosted below:
# http://www.postgresqltutorial.com/postgresql-python/connect/

# import psycopg2
# import pymongo
#
# connyo = pymongo.MongoClient("mongodb+srv://benslow:Grannyboy1@cluster0.kuvzf.mongodb.net",
#                              ssl_cert_reqs=ssl.CERT_NONE)
# dbyo = connyo[f"GRAVVIBOY"]


# Establish a connection to the database by creating a cursor object
# The PostgreSQL server must be accessed through the PostgreSQL APP or Terminal Shell

# conn = psycopg2.connect("dbname=suppliers port=5432 user=postgres password=postgres")

# Or:
# conn = psycopg2.connect(host="node67749-gravvisoft-clone2.w1-us.cloudjiffy.net", port = 5432, database="postgres3", user="webadmin", password="VRDylt04210")
#
# # Create a cursor object
# cur = conn.cursor()
#
# # A sample query of all data from the "vendors" table in the "suppliers" database
# cur.execute("""SELECT * FROM api_lead WHERE user_id = '99'""")
# query_results = cur.fetchall()
# for leads in query_results:
#
#     print(leads[0])
#     print(leads[1])
#
# # Close the cursor and connection to so the server can allocate
# # bandwidth to other requests
# cur.close()
# conn.close()