from analyzer import analyzer

def test_analyzer():
    try:
        with open('words-for-analyzer.txt') as file:
            words = file.read()
    except:
        print('oops there was an error :(')
    
    assert analyzer(words) == {'word': 3}


