from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc


def run():
    
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        value1 = input("Enter value 1:")
        value2 = input("Enter value 2:")
        response = stub.addition(calculator_pb2.AddRequest(val1=int(value1), val2=int(value2)))
    print("Sum of the two numbers is "+str(response.result))

if __name__ == '__main__':
    run()
