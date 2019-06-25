#! /usr/bin/python

from optparse import OptionParser
import pymongo

optp = OptionParser()
optp.add_option("-i", "--init", dest="init", action="store_true", default=False,
        help="create the database and collection")
optp.add_option("-a", "--add", dest="add", action="store_true", default=False,
        help = "add new pairs to collection")
optp.add_option("-d", "--delete", dest="delete", action="store_true", default=False,
        help = "delete an user")
optp.add_option("-l", "--list", dest="list", action="store_true", default=False,
        help = "list all users")

(opt, args) = optp.parse_args()

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.dabd

if opt.init:
  print("Creating users collection")
  db.users

elif opt.add:
  print("Adding further users, leave empty username to finish")
  while True:
    u = raw_input("username: ")
    if not u:
      break
    p = raw_input("passwd: ")
    res = db.users.insert_one({"username": u, "passwd": p})
    print(res)

elif opt.delete:
  print("Deleting an user")
  u = raw_input("username: ")
  res = db.users.find_one({"username": u})
  if res:
    db.users.delete_one({"username": u})
    print("User %s deleted." % u)
  else:
    print("User %s not found." % u)

elif opt.list:
  print("Listing full users collection:")
  for res in db.users.find():
    for k,v in res.iteritems():
      print str(k), ": ", str(v)
    print

else:
  print("Checking some user")
  u = raw_input("username:")
  p = raw_input("passwd:")
  res = db.users.find_one({"username": u, "passwd": p})
  if res:
    print("Access granted to user: %s via passwd: %s" % (res["username"], res["passwd"]))
  else:
    print("Access denied")

