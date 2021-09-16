from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)

def getScore(text):
    result = model.predict([text], k=2)[0]
    
    positive = result.get('positive', 0)
    #neutral = max([result.get('neutral', 0), result.get('skip', 0), result.get('speech', 0)])
    negative = result.get('negative', 0)

    if positive > 0.5 and positive > negative:
        return int(positive * 100)

    if negative > 0.5 and negative > positive:
        return int((1 - negative) * 100)

    return 50 + int(positive * 100) - int(negative * 100)

if __name__ == '__main__':
    print(getScore('Очень плохой банк'), getScore('Привет'), getScore('Супер пупер'))