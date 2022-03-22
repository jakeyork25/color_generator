import random
print("Let's find the perfect color for you!");
redAdjArray = ["Excited", "Joy", "Angry", "Lustful", "Love"];
orangeAdjArray = ["Confident", "Brave", "Social", "Sincere"];
yellowAdjArray = ["Happy", "Creative", "Cheerful"];
greenAdjArray = ["Refreshing", "Natural", "Spititual", "Rugged"];
blueAdjArray = ["Calm", "Relaxing", "Trustful", "Peaceful"];
purpleAdjArray = ["Luxurious", "Ambitious", "Sweet", "Compassionate"];
blackAdjArray = ["Sophisticated", "Dramatic", "Formal", "Stylish"];
whiteAdjArray = ["Clean", "Honest", "Simple", "Futuristic"];

adjArray = redAdjArray + orangeAdjArray + yellowAdjArray + greenAdjArray + blueAdjArray + purpleAdjArray + blackAdjArray + whiteAdjArray;

listToStr = ' '.join(map(str, adjArray));
  
print(listToStr) 
mood = input("What adjective describes the piece best?: ");
print("dull, mid, bright")
brightness = input("What level of brightness would work best for the color?: ");

def addBrightness(amount, brightness):
    return amount + '-' + brightness;
    
def getRGB(amount):
    return {
        'small-dull': random.randint(0, 10),
        'small-mid': random.randint(5, 15),
        'small-bright': random.randint(10, 20),
        'main-dull': random.randint(70, 130),
        'main-mid': random.randint(130, 190),
        'main-bright': random.randint(190, 250),
        'upper-dull': random.randint(100, 130),
        'upper-mid': random.randint(160, 190),
        'upper-bright': random.randint(220, 250),
        'lower-dull': random.randint(70, 100),
        'lower-mid': random.randint(130, 160),
        'lower-bright': random.randint(190, 220)
    }[amount]

def setRGB(r, g, b, brightness):
    amountArray = [r, g, b];
    tempArray = [];
    for amount in amountArray:
        updatedAmount = addBrightness(amount, brightness);
        value = str(getRGB(updatedAmount));
        tempArray.append(value);
    return tempArray;

rgbArray = [];     

if mood in redAdjArray:
    rgbArray = setRGB('main', 'small', 'small', brightness);
elif mood in orangeAdjArray:
    rgbArray = setRGB('upper', 'lower', 'small', brightness);
elif mood in yellowAdjArray:
    rgbArray = setRGB('main', 'main', 'small', brightness);
elif mood in greenAdjArray:
    rgbArray = setRGB('small', 'main', 'small', brightness);
elif mood in blueAdjArray:
    rgbArray = setRGB('small', 'small', 'main', brightness);
elif mood in purpleAdjArray:
    rgbArray = setRGB('main', 'small', 'main', brightness);
elif mood in blackAdjArray:
    rgbArray = setRGB('small', 'small', 'small', 'dull');
elif mood in whiteAdjArray:
    rgbArray = setRGB('main', 'main', 'main', 'bright');

red = rgbArray[0];
green = rgbArray[1];
blue = rgbArray[2];

print('(' + red + ', ' + green + ', ' + blue + ')');

