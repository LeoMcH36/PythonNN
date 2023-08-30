import math
import copy
from decimal import Decimal, getcontext
from featureExtraction import *
from Data import dataLanguage, testData
learningRate = 1
biasC = 0
# desiredOutput = 0.125
arrows = []
neurons = []
modelArrows = []
modelNeurons = []
inputA = 0
inputB = 0
finalOutput = 0
count = 0


def forwardPassTest(paragraph, label, model):

    featuresTest = [averageWordLength(paragraph), mostCommonVowel(
        paragraph), leastCommonVowel(paragraph), doubleLettersFrequency(paragraph)]
    print(featuresTest)

    model.arrows[0].input = featuresTest[0]
    model.arrows[0].model = modelTemp
    # arrow2
    model.arrows[1].input = featuresTest[1]
    model.arrows[1].model = modelTemp
    # arrow3
    model.arrows[2].input = featuresTest[2]
    model.arrows[2].model = modelTemp
    # arrow4
    model.arrows[3].input = featuresTest[3]
    model.arrows[3].model = modelTemp

    # re calculate neuron values from arrows of model specifically
    neuronFeature1 = Neuron("nf1", 0, model, label)
    neuronFeature2 = Neuron("nf2", 0, model, label)
    neuronFeature3 = Neuron("nf3", 0, model, label)
    neuronFeature4 = Neuron("nf4", 0, model, label)

    # add neurons to list of model neurons completed
    model.neurons[0] = neuronFeature1
    model.neurons[1] = neuronFeature2
    model.neurons[2] = neuronFeature3
    model.neurons[3] = neuronFeature4

    # get hidden arrow inputs from new models neurons
    model.arrows[4].input = modelTemp.neurons[0].getOutput()
    model.arrows[4].model = modelTemp
    model.arrows[5].input = modelTemp.neurons[1].getOutput()
    model.arrows[5].model = modelTemp
    model.arrows[6].input = modelTemp.neurons[2].getOutput()
    model.arrows[6].model = modelTemp
    model.arrows[7].input = modelTemp.neurons[3].getOutput()
    model.arrows[7].model = modelTemp

    # re calculate neuron values from arrows of model specifically
    neuronHidden1 = Neuron("h1", 0, model, label)
    neuronHidden2 = Neuron("h2", 0, model, label)

    model.neurons[4] = neuronHidden1
    model.neurons[5] = neuronHidden2

    # output arrows
    model.arrows[8].input = modelTemp.neurons[4].getOutput()
    model.arrows[8].model = modelTemp

    model.arrows[9].input = modelTemp.neurons[5].getOutput()
    model.arrows[9].model = modelTemp

    neuronHidden1 = Neuron("output", 0, model, label)
    model.neurons[6] = neuronOutput

    # getOutput always needs called
    # print("*************************************************outcome********************************************************")
    return neuronOutput.getOutput()

class arrow:
    def __init__(self, weight, input, prevNeuronName, nextNeuronName, model):
        self.weight = weight
        self.input = input
        self.prevNeuronName = prevNeuronName
        self.nextNeuronName = nextNeuronName
        self.model = model
        if model == 0:
            arrows.append(self)
        else:
            model.arrows.append(self)

    def getInputAdjusted(self):
        return self.weight * self.input

    # reverse pass

    def setNewWeight(self):

        if self.model == 0:
            for n in neurons:
                if n.name == self.nextNeuronName:
                    self.weight = self.weight + \
                        (n.error * self.input * learningRate)
                    return self.weight
        else:
            for n in self.model.neurons:
                if n.name == self.nextNeuronName:
                    self.weight = self.weight + \
                        (n.error * self.input * learningRate)
                    return self.weight

class Neuron:
    def __init__(self, name, outputBool, model, desiredOutput):
        self.name = name
        self.outputBool = outputBool
        self.value = 0
        self.model = model
        self.desiredOutput = desiredOutput
        # self.value = self.getOutput(self.name,self.outputBool)
        self.error = 0
        if model == 0:
            neurons.append(self)
        else:
            model.neurons.append(self)

    def getOutput(self):

        totalInput = 0
        if self.model == 0:

            for arr in arrows:
                if self.name == arr.nextNeuronName:
                    totalInput += arr.getInputAdjusted()
        else:
            for arr in self.model.arrows:
                if self.name == arr.nextNeuronName:
                    totalInput += arr.getInputAdjusted()
        if self.outputBool == 1:

            global finalOutput
            finalOutput = 1/(1 + (math.exp(-(totalInput - biasC))))
        self.value = 1/(1 + (math.exp(-(totalInput - biasC))))
        return 1/(1 + (math.exp(-(totalInput - biasC))))

    # reverse

    def calculateError(self):
        if self.outputBool == 1:
            global count
            count += 1
            self.error = self.value * \
                (1-self.value) * (self.desiredOutput - self.value)
            return self.error
        else:
            refN = ""
            error = 0
            weight = 0
            for arr in arrows:
                if arr.prevNeuronName == self.name:
                    weight = arr.weight
                    refN = arr.nextNeuronName
                    for n in neurons:
                        if n.name == refN:
                            error = n.error
            self.error = self.value * (1-self.value) * (weight * error)
            return self.error

# the error used in calculating the new error of the neuron is
# the error of the arrow's next neuron,
# where said arrow's previous neuron is this one

class Model:
    def __init__(self, arrows, neurons):
        self.arrows = copy.copy(arrows)
        self.neurons = copy.copy(neurons)


data = []
features = []

for rowNum in range(len(dataLanguage)-1):
    paragraph = dataLanguage[rowNum]['paragraph']

    features.append([[averageWordLength(paragraph), mostCommonVowel(paragraph), leastCommonVowel(
        paragraph), doubleLettersFrequency(paragraph)], dataLanguage[rowNum]['label']])

modelTemp = []

runs = 5000
#TRAINING
firstRunFlag = True
for i in range(len(features)):
    print("new intput")
    print(features[i][1])

    newInput = True
    for x in range(runs):
        print("*************************************************************", x)

        if firstRunFlag:
            # 1st row, 1st element,  element
            print(features[i][0][0])
            arrowFeature1 = arrow(0.1, features[i][0][0], "", "nf1", 0)
            neuronFeature1 = Neuron("nf1", 0, 0, features[i][1])

            print(features[i][0][1])
            arrowFeature2 = arrow(0.8, features[i][0][1], "", "nf2", 0)
            neuronFeature2 = Neuron("nf2", 0, 0, features[i][1])

            print(features[i][0][2])
            arrowFeature3 = arrow(0.4, features[i][0][2], "", "nf3", 0)
            neuronFeature3 = Neuron("nf3", 0, 0, features[i][1])

            print(features[i][0][3])
            arrowFeature4 = arrow(0.6, features[i][0][3], "", "nf4", 0)
            neuronFeature4 = Neuron("nf4", 0, 0, features[i][1])

            print("feature neurons outputs")
            print(neuronFeature1.getOutput())
            print(neuronFeature2.getOutput())
            print(neuronFeature3.getOutput())
            print(neuronFeature4.getOutput())

            # time.sleep(5)
            # input neurons 1-2 connect to hidden 1
            arrowhidden1 = arrow(
                0.3, neuronFeature1.getOutput(), "nf1", "h1", 0)
            arrowhidden2 = arrow(
                0.3, neuronFeature2.getOutput(), "nf2", "h1", 0)
            neuronHidden1 = Neuron("h1", 0, 0, features[i][1])

            # input neurons 3-4 connect to hidden 2
            arrowhidden3 = arrow(
                0.3, neuronFeature3.getOutput(), "nf3", "h2", 0)
            arrowhidden4 = arrow(
                0.3, neuronFeature4.getOutput(), "nf4", "h2", 0)
            neuronHidden2 = Neuron("h2", 0, 0, features[i][1])

            print(neuronHidden1.getOutput())
            print(neuronHidden2.getOutput())

            # hidden neurons 1-2 connect to output
            arrowOutput1 = arrow(
                0.3, neuronHidden1.getOutput(), "h1", "output", 0)
            arrowOutput2 = arrow(
                0.3, neuronHidden2.getOutput(), "h2", "output", 0)

            neuronOutput = Neuron("output", 1, 0, features[i][1])

            print("first run output")
            # getOutput always needs called
            print(neuronOutput.getOutput())

            print("training")

            # reverse pass
            print(neuronOutput.calculateError())

            print(arrowOutput1.setNewWeight())

            print(arrowOutput2.setNewWeight())

            print(neuronHidden1.calculateError())

            print(neuronHidden2.calculateError())

            print(arrowhidden1.setNewWeight())
            print(arrowhidden2.setNewWeight())
            print(arrowhidden3.setNewWeight())
            print(arrowhidden4.setNewWeight())

            print(neuronFeature1.calculateError())
            print(neuronFeature2.calculateError())
            print(neuronFeature3.calculateError())
            print(neuronFeature4.calculateError())

            print(arrowFeature1.setNewWeight())
            print(arrowFeature2.setNewWeight())
            print(arrowFeature3.setNewWeight())
            print(arrowFeature4.setNewWeight())

            modelTemp = Model(arrows, neurons)
            print("loop :", i)
            print("feature first", features[i][0][0])
        else:

            newInput = False
            # overwrite input layer with next input data
            modelTemp.arrows[0].input = features[i][0][0]

            modelTemp.arrows[0].model = modelTemp
            # arrow2
            modelTemp.arrows[1].input = features[i][0][1]
            modelTemp.arrows[1].model = modelTemp
            # arrow3
            modelTemp.arrows[2].input = features[i][0][2]
            modelTemp.arrows[2].model = modelTemp
            # arrow4
            modelTemp.arrows[3].input = features[i][0][3]
            modelTemp.arrows[3].model = modelTemp

            # re calculate neuron values from arrows of model specifically
            neuronFeature1 = Neuron("nf1", 0, modelTemp, features[i][1])
            neuronFeature2 = Neuron("nf2", 0, modelTemp, features[i][1])
            neuronFeature3 = Neuron("nf3", 0, modelTemp, features[i][1])
            neuronFeature4 = Neuron("nf4", 0, modelTemp, features[i][1])

            # add neurons to list of model neurons completed
            modelTemp.neurons[0] = neuronFeature1
            modelTemp.neurons[1] = neuronFeature2
            modelTemp.neurons[2] = neuronFeature3
            modelTemp.neurons[3] = neuronFeature4

            # get hidden arrow inputs from new models neurons
            modelTemp.arrows[4].input = modelTemp.neurons[0].getOutput()
            modelTemp.arrows[4].model = modelTemp
            modelTemp.arrows[5].input = modelTemp.neurons[1].getOutput()
            modelTemp.arrows[5].model = modelTemp
            modelTemp.arrows[6].input = modelTemp.neurons[2].getOutput()
            modelTemp.arrows[6].model = modelTemp
            modelTemp.arrows[7].input = modelTemp.neurons[3].getOutput()
            modelTemp.arrows[7].model = modelTemp

            # re calculate neuron values from arrows of model specifically
            neuronHidden1 = Neuron("h1", 0, modelTemp, features[i][1])
            neuronHidden2 = Neuron("h2", 0, modelTemp, features[i][1])

            modelTemp.neurons[4] = neuronHidden1
            modelTemp.neurons[5] = neuronHidden2

            # output arrows
            modelTemp.arrows[8].input = modelTemp.neurons[4].getOutput()
            modelTemp.arrows[8].model = modelTemp

            modelTemp.arrows[9].input = modelTemp.neurons[5].getOutput()
            modelTemp.arrows[9].model = modelTemp

            neuronHidden1 = Neuron("output", 0, modelTemp, features[i][1])
            modelTemp.neurons[6] = neuronOutput

            print("*************************************************outcome********************************************************")
            print(neuronOutput.getOutput())

            # Reverse Pass
            # output
            modelTemp.neurons[6].calculateError()

            modelTemp.arrows[8].setNewWeight()

            modelTemp.arrows[9].setNewWeight()

            # hidden
            modelTemp.neurons[5].calculateError()

            modelTemp.neurons[4].calculateError()

            modelTemp.arrows[7].setNewWeight()
            modelTemp.arrows[6].setNewWeight()
            modelTemp.arrows[5].setNewWeight()
            modelTemp.arrows[4].setNewWeight()

            # input
            modelTemp.neurons[3].calculateError()
            modelTemp.neurons[2].calculateError()
            modelTemp.neurons[1].calculateError()
            modelTemp.neurons[0].calculateError()

            modelTemp.arrows[4].setNewWeight()
            modelTemp.arrows[3].setNewWeight()
            modelTemp.arrows[2].setNewWeight()
            modelTemp.arrows[1].setNewWeight()

        firstRunFlag = False

print("After Training")
print("remember to check all inputted values like desired outcome etc")




#TESTING
modelLanguages = Model(modelTemp.arrows, modelTemp.neurons)

testResults = []
success = 0
avgOutcome = 0
totalOutcome = 0
threshold = 0.0024
for row in range(len(testData)):

    outcome = forwardPassTest(
        testData[row]['paragraph'], testData[row]['label'], modelLanguages)
    totalOutcome += outcome
    prediction = ""

    if outcome > threshold:
        if testData[row]['label'] == 1:
            success += 1
        prediction = "spanish"
    else:
        if testData[row]['label'] == 0:
            success += 1
        prediction = "english"

    testResults.append((outcome, testData[row]['label'], prediction))

successRate = (success / len(testData))
avgOutcome = (totalOutcome / len(testData))

print("0 is english 1 is spanish")
for result in testResults:

    print(result)

print("Average outcome", avgOutcome)
print("Accuracy: ", successRate , f"Where threshold is {threshold}, runs per feature is {runs}, bias is {biasC} and learning rate is {learningRate}")
