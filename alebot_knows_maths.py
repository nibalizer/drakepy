#Spencerk and Alevar
#dbad license




#input strings look like
# alebot: convert 10 mph to m/s

string_to_parse = "10 mph to m/s"



from twisted.internet import reactor

processProtocol = MyProcessProtocol()
reactor.spawnProcess(processProtocol, executable, args=[units, source, destination],
                     env={'HOME': os.environ['HOME']}, path,
                     uid, gid, usePTY, childFDs)






