
#this function adds indicies to the iterable and returns a tuple pack
lst =['apple','banana','grapes']

for index, lst in enumerate(lst):
    print("%s  %s"%(index,lst))


l= ['eat','sleep','talk','read']
x= enumerate(l)
print(list(x))
print(type(x))

# import logging
# logger=logging.basicConfig(filename="")
# logger=logging.getLogger()
# logger.setLevel(logging.info())
#
# import configparser
# config=configparser.ConfigParser()
# config.read("file")
# config.get("info","user")