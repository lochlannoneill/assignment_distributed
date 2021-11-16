import grpc
from dictionary import Dictionary
from concurrent import futures
import logging

from spellingb_pb2_grpc import SpellingBServicer, add_SpellingBServicer_to_server
from spellingb_pb2 import GameResponse, WordResponse, PointsResponse
import pangrams
from random import choice

class Server(SpellingBServicer): # change to SpellingBServicer
    def __init__(self):
        self.dictionary = Dictionary()
        self.points = 0
        
    def StartGame(self, request, context):
        pangram = pangrams.get_pangram()
        required_letter = choice(pangram)
        return GameResponse(pangram = pangram, requiredLetter = required_letter)
    
    def VerifyWord(self, request, context):
        word = request.word
        required_letter = request.required_letter
        if self.dictionary.is_word(word):
            #if required_letter in word:
                #if len(word) < 4:
                    #return WordResponse(isWord = False, str = "Must not be less than 4 letters")
                #elif len(word) == 4:
                    #self.points += 1
                    #return WordResponse(isWord = True, str = "Valid word scoring 1 point")
                #elif 4 < len(word) < 7:
                    #self.points += len(word)
                    #return WordResponse(isWord = Ture, str = "Valid Word scoring {} points".format(points_scored))
                #elif len(word) == 7:
                    #self.points += 16
                    #return WordResponse(isWord = True, str = "Pangram! 16 points")
            #else:
                #return WordReponse(isWord = False, str = "Must include the required letter")
            self.points += 1
            return WordResponse(isWord = True)
        else:
            return WordResponse(isWord = False)
            #return WordResponse(isWord = False, str = "Not a valid word")
    
    def ReturnPoints(self, request, context):
        return PointsResponse(points=self.points) # the server will keep these points even if i close the ide
    
    
def startServer():
    print("Starting server...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) # find out what 10 means
    add_SpellingBServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:50055') # maybe change to localhost:50051
    server.start()
    print("Server Started")
    server.wait_for_termination()
    
    
logging.basicConfig()
startServer()