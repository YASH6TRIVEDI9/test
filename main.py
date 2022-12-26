THRESHOLD_VALUE = 10

# def combination_of_sentences(my_list):

#     my_dict = {}
#     output_list = []
#     sentence = ""
#     for i in range(len(my_list)):
#         sentence = my_list[i]["sentence"]
#         start_time = float(my_list[i]["start_time"])     
#         end_time = float(my_list[i]["end_time"])

#         if my_dict != {}:
#             start_time = my_dict["start_time"]
#             sentence = my_dict["sentence"] + " " + sentence 

#             my_dict = {
#                 "sentence": sentence,
#                 "start_time": start_time,
#                 "end_time": end_time
#                 }
        
#         if (end_time - start_time) <= THRESHOLD_VALUE:
#             my_dict = {
#             "sentence": sentence,
#             "start_time": start_time,
#             "end_time": end_time
#             }

#         else:
#             output_list.append(my_dict)
#             my_dict = {}
#             sentence = ""

#     return output_list

def combination_of_sentences(cool_list):

    my_dict = {}
    out_list = []
    sentence = ""
    for i in range(len(cool_list)):
        sentence = cool_list[i]["sentence"]
        start_time = float(cool_list[i]["start_time"])     
        end_time = float(cool_list[i]["end_time"])

        if my_dict != {}:
            start_time = my_dict["start_time"]
            sentence = my_dict["sentence"] + " " + sentence 

            my_dict = {
                "sentence": sentence,
                "start_time": start_time,
                "end_time": end_time
                }

        if (end_time - start_time) > THRESHOLD_VALUE:
            my_dict = {
            "sentence": sentence,
            "start_time": start_time,
            "end_time": end_time
            }
            out_list.append(my_dict)
            my_dict = {}
            sentence = ""
        
        if (end_time - start_time) <= THRESHOLD_VALUE:
            my_dict = {
            "sentence": sentence,
            "start_time": start_time,
            "end_time": end_time
            }

        # else:
        #     # my_dict = {
        #     # "sentence": sentence,
        #     # "start_time": start_time,
        #     # "end_time": end_time
        #     # }
        #     out_list.append(my_dict)
        #     my_dict = {}
        #     sentence = ""

    print(out_list)

    return out_list



if __name__ == "__main__":

    with open("my_list.txt") as f:
        my_list = f.read()
        my_list = eval(my_list)

    THRESHOLD_VALUE = 10

    combination_of_sentences(my_list)
