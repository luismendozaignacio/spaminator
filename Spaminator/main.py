from autoMessenger import auto_send_messages, auto_send_default_messages, open_app, open_testing_input_file_app ,end


if __name__ == "__main__":

	while True:
	    try:
	        user_answer = input("Do you want to input a sentence? Y or N? ---->  ")
	        if user_answer == "Y" or user_answer == "y" or user_answer == "Yes" or user_answer == "yes":
	            user_input = input("Type something ---->  ")
	            break
	        elif user_answer == "N" or user_answer == "n" or user_answer == "No" or user_answer == "no":
	            print("Messages will be sent from a file for 5 times")

	            open_testing_input_file_app() #this is to test everything is working. Comment it once the testing is done
	            #open_app() #uncomment this once testing is done to open the messaging app 

	            auto_send_default_messages() #sends default messages, do not comment this line
	            end()
	            exit() #ends  the script
	            break
	        else:
	            raise NameError("Invalid response.")       
	    except NameError:
	        print("Wrong answer")
	    else:
	        break
	 
	while True:
	    try:
	        number_of_times_input = abs(int(input("How many times? ---->  "))) 
	        number_of_times_input = number_of_times_input if number_of_times_input <= 10 else 10 #safety spam mechanism
	        print("{0} will be sent.".format(number_of_times_input))

	        open_testing_input_file_app() #this is to test everything is working. Comment it once the testing is done
	        #open_app() #uncomment this once testing is done to open the messaging app 

	        auto_send_messages(user_input, number_of_times_input) #sends messages, do not comment this line
	        end()
	        break
	    except ValueError:
	        print("Enter a positive number. ---->  ")
	exit() #ends the script