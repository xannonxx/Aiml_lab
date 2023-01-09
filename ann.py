from random import random
from math import exp
from random import seed

def activate(weights,inputs):
    summ = weights[-1];
    for i in range(len(inputs)-1):
        summ += weights[i]*inputs[i]
    
    return summ;

def transfer(activation):
    return 1.0/(1.0+exp(-activation))
    
def transfer_derivative(ouput):
    return ouput*(1-ouput)

def forward_prop(network,row):
    inputs = row
    
    for layer in network:
        nxt_inp = []
        for neuron in layer:
            activation = activate(neuron['weights'], inputs)
            neuron['output'] = transfer(activation)
            nxt_inp.append(neuron['output'])
        inputs = nxt_inp
    
    return inputs

def initialize(n_input,n_hidden,n_output):
    network = []
    hidden_layer = [{'weights':[random() for i in range(n_inputs+1)]} for i in range(n_hidden)]
    network.append(hidden_layer)
    output_layer = [{'weights':[random() for i in range(n_inputs+1)]} for i in range(n_hidden)]
    network.append(output_layer)
    return network


def backward_propogation(network,expected):
    
    for i in reversed(range(len(network))):
        layer = network[i]
        errors = []
        if i != len(expected)-1:
            for j in range(len(layer)):
                err = 0
                for neuron in network[i+1]:
                    err += neuron['delta']*neuron['weights'][j]
                errors.append(err)
        else:
            for j in range(len(layer)):
                neuron = layer[j]
                errors.append(expected[j] - neuron['output'])
        
        for j in range(len(layer)):
            neuron = layer[j]
            neuron['delta'] = errors[j]*transfer_derivative(neuron['output'])
    


def update_weights(network,l_rate,row):
    
    inputs = row
    for i in range(len(network)):
        layer = network[i]
        
        if(i != 0):
            inputs = [neuron['output'] for neuron in network[i-1]]
            
        for j in range(len(layer)):
            neuron = layer[i]
            for k in range(len(inputs)):
                neuron['weights'][k] += l_rate*inputs[k]*neuron['delta']
            
            

def train_network(network, l_rate, epoch, dataset):
    
    for i in range(epoch):
        sum_err = 0
        for row in dataset:
            
            output = forward_prop(network,row)
            
            expected = [0 for i in range(2)]
            expected[row[-1]] = 1
            sum_err += sum([(output[i] - expected[i])**2 for i in range(len(expected))])
            
            backward_propogation(network,expected)
            update_weights(network,l_rate,row)
            
        print(sum_err)
    

seed(1)
dataset = [[2.7810836,2.550537003,0],
[1.465489372,2.362125076,0],
[3.396561688,4.400293529,0],
[1.38807019,1.850220317,0],
[3.06407232,3.005305973,0],
[7.627531214,2.759262235,1],
[5.332441248,2.088626775,1],
[6.922596716,1.77106367,1],
[8.675418651,-0.242068655,1],
[7.673756466,3.508563011,1]]

n_inputs = 2
n_outputs = 2
n_hidden = 2

network = initialize(n_inputs,n_hidden,n_outputs)
#print(network)
train_network(network,0.5,20,dataset)