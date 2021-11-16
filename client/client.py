import grpc
#from server import spellingb_pb2 as spellingb_pb2
#from server import spellingb_pb2_grpc as spellingb_pb2_grpc
import spellingb_pb2 as spellingb_pb2
import spellingb_pb2_grpc as spellingb_pb2_grpc
import logging
import reading_from_user

def display_intro(pangram):
    print("Pangram Game!")
    print("Make as many words as possible, MUST include middle letter")
    print()
    # print("{} {} {} [{}] {} {} {}".format(pangram[0], pangram[1], pangram[2], pangram[3], pangram[4], pangram[5], pangram[6]))
    
    
def ask_input(pangram):
    print("{} {} {} [{}] {} {} {}".format(pangram[0], pangram[1], pangram[2], pangram[3], pangram[4], pangram[5], pangram[6]))
    input = reading_from_user.read_nonempty_alphabetical_string("Enter word >>> ")
    return input
    
        
def start_client():
    #WORKING
    print("Starting client...")
    channel = grpc.insecure_channel('127.0.0.1:50055')
    stub = spellingb_pb2_grpc.SpellingBStub(channel)
    print("Client started")
    
    # game request + response
    # WORKING
    game_request = spellingb_pb2.GameRequest()
    game_response = stub.StartGame(game_request)
    pangram = game_response.pangram
    required_letter = game_response.requiredLetter #----NOT WORKING----
    
    
    # just for testing - need to remove
    # NOT WORKING
    print("Pangram > " + pangram)
    print("Required Letter > " + required_letter)
    print()
    
    
    # display the introduction of the game
    display_intro(pangram)

    
    # ask user for input
    # word request + response 
    # point request + reponse
    # WORKING
    while True:
        input = ask_input(pangram)
        #_____________check to see if in word____________________
        
        word_request = spellingb_pb2.WordRequest(word = input)
        word_response = stub.VerifyWord(word_request)
        #print(word_response.isWord)
        
        points_request = spellingb_pb2.PointsRequest()
        points_response = stub.ReturnPoints(points_request)
        print ("Current Score: {}".format(points_response.points))
        print()
    
    
    
    
def main():
    logging.basicConfig()
    start_client()

main()
