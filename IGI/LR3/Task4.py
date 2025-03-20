import Input
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Execution time:", end_time - start_time, "seconds")
        return result

    return wrapper


@measure_time
def text_analyze():
    """
        Developer Pavel Zdor
        date: 10.03.2025
        function is developed for calculating amount of words,
        widest string and its index, and printing all odd indexed strings
        function has own decorator which calculates time of runtime of function with 10000000 approximation
        :return:
        """
    counter = 1
    text_to_analyze = ("So she was considering in her own mind, as well as she could, "
                       "for the hot day made her feel very sleepy and stupid, "
                       "whether the pleasure of making a daisy-chain would be"
                       " worth the trouble of getting up and picking the daisies, "
                       "when suddenly a White Rabbit with pink eyes ran close by her.")
    all_str = ""
    max_str = ""
    tmp_str = ""
    index = 0
    text_to_analyze = text_to_analyze.replace(',', "")
    text_to_analyze = text_to_analyze.replace('.', "")
    for i in text_to_analyze:
        if i == ' ':
            counter += 1
            all_str += " "
            if len(max_str) < len(tmp_str):
                max_str = tmp_str
                index = counter - 1
            tmp_str = ""
        else:
            tmp_str += i
            if (counter-1) % 2 == 0:
                all_str += i
    print("Amount of words are", counter)
    print("The most wide word is", max_str, "Its index is", index)
    print("All strings with odd indexes", all_str)
    for _ in range(10000000):
        pass
