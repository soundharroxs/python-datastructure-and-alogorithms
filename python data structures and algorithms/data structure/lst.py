def contcat(sentence,split_count):
    temp = list(sentence.split(" "))
    result =[]
    for i in range(len(temp)-1):
        if split_count >= len(temp[i]+temp[i+1]):
            temp[i+1]= (temp[i]+temp[i+1])
        else:
            result.append(temp[i])
    else:
        result.append(temp[i+1])

    print(result)

sentence = input("enter the sentence : ")
split_count = int(input(" enter the number : "))
contcat(sentence,split_count)
