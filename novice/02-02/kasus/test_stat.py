import statistics as stat

data = [50,50,45,69,70,50,45,65,66,76]
a = stat.mean(data)
b = stat.median(data) 
def test_stat():
    assert a == 58.6, "should be 58.6"
    assert b == 55, "should be 57.5"
if __name__ == "__main__":
    test_stat()
    print("evrything passed")