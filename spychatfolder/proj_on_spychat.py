from steganography.steganography import Steganography  # Importing module
from dict import spy_dict
# Lists
status_list = ['Online', 'Offline', 'Available', 'Unavailable', 'Busy']
name_friend_list = ['Mohan', 'Ravi', 'Rani', 'Raj', 'Ekta']
age_friend_list = ['14', '30', '40', '21', '18']
rating_friend_list= ['4.2', '3.2', '4.5', '3.9', '4.8']
secret_message = []
special_msg = ['SOS', 'Save Me', 'Danger', 'Fire in Hole']
print ' WELCOME TO SPY'
user = raw_input('What you want to do: \n1. Continue with Default User \n2. Create a new User \n')# Selection of User
if user == '1':  # If Choice is default user
    print 'You Choose to Continue with Default User \n'
    print 'Default user is: \n' + str(spy_dict)
    loop = True # loop to keep on repeating until the user chooses to exit
    while loop:
        choice = raw_input('\nSelect your Choice: \n1. ADD A STATUS UPDATE \n2. ADD A FRIEND \n3. '
                           'SEND A SECRET MESSAGE \n4. READ A SECRET MESSAGE \n5. READ CHATS FROM USER \n6. EXIT \n')
        if choice == '6':
            print 'You are Logged Out!'  # User Chooses to Exit
            loop = False
        elif choice == '1':
            print 'You Chose Status Update \n'  # Chooses to Update Status
            print status_list
            spy_status = raw_input('Select an Status from the above Status or Enter your Status: \n')# Select the Status
            if spy_status in status_list:
                print 'Your Status is ' + spy_status  # Print the Status
            else:
                status_list.append(spy_status)
                print 'Your Current Updated Status is: ' + spy_status  # Update the Status to the List
        elif choice == '2':
            print 'You Chose to Add Friend! \n'
            friend_name = raw_input('Enter Friend\'s Name: \n')  # Enter the Friend's Name
            friend_age = raw_input('Enter Friend\'s Age: \n')  # Enter the Friend's Age
            friend_rating = raw_input('Enter Friend\'s Rating: \n')  # Enter the Friend's Rating
            if friend_name not in name_friend_list:  # Check if name exist in the list
                name_friend_list.append(friend_name)  # if not available append to the list
                print name_friend_list  # print the new updated list
            else:
                print 'Your Friend is Already in the List \n'
                if friend_age > 50 or friend_age < 12:
                    print 'Invalid age\n'
                else:
                    age_friend_list.append(friend_age)
                    print 'Your Friend List is as Follow: \n' + age_friend_list
            # Print all the details of Spy's Friend
            print 'Your Friend\'s Name is: ' + friend_name + ', Friend\'s age is: ' + friend_age + ', Friend\'s rating is: ' + friend_rating
            print '\nYou have ' + str(len(name_friend_list)) + ' Friends'
        elif choice == '3':
            print('You Chose to Send a Secret Message \n')
            select_a_friend = raw_input(str(name_friend_list) + '\nSelect the name of your friend \n') # select a friend to whom a secret message has to be send
            if select_a_friend in name_friend_list:
                print 'Index of Selected Friend is: ' + str(name_friend_list.index(select_a_friend))
                input_image_path = raw_input('\nEnter the the path of the image \n')  # Choose the Image which needs to be encoded
                text = raw_input('Enter a Secret Message you want to Hide: \n')  # Enter the Secret Message
                output_image = raw_input('Enter output image name with .png extension: \n')  # Enter the Output Image path
                Steganography.encode(input_image_path, output_image, text)  # Steganography for encoding the image
                secret_text = Steganography.decode(output_image)  # Store in the image
                secret_message.append(secret_text)
            else:
                print select_a_friend + ', is not in the list of your friends'
                name_friend_list.append(select_a_friend)
                print str(name_friend_list) + '\nNew Friend added to the list, its index is: ' + str(
                    name_friend_list.index(select_a_friend))
                input_image_path = raw_input('\nEnter the the path of the image \n')
                text = raw_input('Enter a Secret Message you want to Hide: \n')
                output_image = raw_input('Enter output image name with .png extension: \n')
                Steganography.encode(input_image_path, output_image, text)
                secret_text = Steganography.decode(output_image)
                secret_message.append(secret_text)
        elif choice == '4':
            print 'You Chose to Read the Secret Message \n'
            if secret_message:
                print 'Your Secret Message is: \n' + str(secret_text)
            else:
                print 'No Received msg \n'

        elif choice == '5':
            print 'You Chose to Read the Entire Chat History \n'
            if secret_message:
                print 'You Contacted ' + str(select_a_friend) + ' and you sent him ' + str(secret_text)
            else:
                print 'No Chat History \n'
elif user == '2':
    user_name = raw_input('Enter your new Name: \n')
    if len(user_name) > 0:
        salutation = raw_input(user_name + ', you are MALE or FEMALE? \nChoose m/f \n')
        if salutation == 'm':
            print 'Hello! Mr. ' + user_name
            user_age = int(raw_input('Mr. ' + user_name + ', enter your age \n'))
            if user_age > 50 or user_age < 12:
                print 'Access Denied!'
                exit()
            else:
                user_rating = float(raw_input('Enter your Rating \n'))
                if user_rating > 3.5:
                    print 'You are great \n'
                else:
                    print 'improve yourself! \n'
        elif salutation == 'f':
            print 'Hello! Ms. ' + user_name
            user_age = int(raw_input('Ms. ' + user_name + ', enter your age \n'))
            if user_age > 50 or user_age < 12:
                print 'Access Denied!'
                exit()
            else:
                user_rating = float(raw_input('Enter your Rating Out of 5 \n'))
                if user_rating > 3.5:
                    print 'you are great \n'
                else:
                    print 'improve yourself! \n'
        print 'HI' + custom_user_name + ' YOU ARE ' + salutation + ', YOU ARE ' + str(
            user_age) + ' YEARS OLD & YOUR"S RATING IS ' + str(user_rating)
    else:
        print 'Invalid Choice, Enter a Valid Name \n'
    loop = True # loop to keep on repeating the menu, until the user chooses to exit
    while loop:
        choice = raw_input('\nSelect your Choice: \n1. ADD A STATUS UPDATE \n2. ADD A FRIEND \n3. '
                           'SEND A SECRET MESSAGE \n4. READ A SECRET MESSAGE \n5. READ CHATS FROM USER \n6. EXIT \n')
        if choice == '6':
            print 'You QUIT!'  # User Chooses to Exit
            loop = False

        elif choice == '1':
            print 'You Chose Status Update \n'  # User Chooses to Update Status
            print status_list
            spy_status = raw_input('Select a Status which is already present or Enter your own Status: \n') # Select the Status
            if spy_status in status_list:
                print 'Your Status is ' + spy_status  # Print the Status
            else:
                status_list.append(spy_status)
                print 'Your Current Updated Status is: ' + spy_status  # Update the Status to the List and Print it
        elif choice == '2':
            print 'You Chose to Add a Friend! \n'
            friend_name = raw_input('Enter Friend\'s Name: \n')  # Enter the Friend's Name
            friend_age = raw_input('Enter Friend\'s Age: \n')  # Enter the Friend's Age
            friend_rating = raw_input('Enter Friend\'s Rating: \n')  # Enter the Friend's Rating
            if friend_name not in friend_list_name:  # Check if name exist in the list
                name_friend_list.append(friend_name)  # if not available append to the list
                print name_friend_list  # print the new updated list
            else:
                print 'Your Friend is Already in the List \n'
                if friend_age > 50 or friend_age < 12:
                    print 'Sorry! Generation Gap, Age Requirement not Fulfilled\n'
                else:
                    age_friend_list.append(friend_age)
                    print 'Your Friends are: \n' + age_friend_list

            print 'Your Friend\'s Name is: ' + friend_name + ', Friend\'s age is: ' + friend_age + ', Friend\'s rating is: ' + friend_rating
            print '\nYou have ' + str(len(name_friend_list)) + ' Friends'# Print all the details of Spy's Friend
        elif choice == '3':
            print('Send a Secret Message \n')
            select_a_friend = raw_input(str(name_friend_list) + '\nSelect the name of your friend \n')# selecting the friend to whom a secret message has to be send
            if select_a_friend in name_friend_list:
                print 'Index of Selected Friend is: ' + str(name_friend_list.index(select_a_friend))
                input_image_path = raw_input('\nEnter the the path of the image \n')  # Choose the Image which needs to be encoded
                text = raw_input('Enter a Secret Message \n')  # Enter the Secret Message
                output_image = raw_input('Enter output image name with .png extension: \n')  # Enter the Output Image path
                Steganography.encode(input_image_path, output_image, text)  # Steganography for encoding the image
                secret_text = Steganography.decode(output_image)  # Store in the image
                secret_message.append(secret_text)
            else:
                print select_a_friend + ', is not in the list of your friends'  # if friend not in list
                name_friend_list.append(select_a_friend)  # Add friend to the existing list
                print str(name_friend_list) + '\nNew Friend added to the list, its index is: ' + str(
                    name_friend_list.index(select_a_friend))  # Print the Index of the Friend Name from the list
                input_image_path = raw_input('\nEnter the the path of the image of secret message: \n')  # Path of Image to be Encoded
                text = raw_input('Enter a  Message you want to Hide: \n')  # Secret Message
                output_image = raw_input('Enter output image name with .png extension: \n')  # Path of Output Image
                Steganography.encode(input_image_path, output_image, text)  # Steganography arguments
                secret_text = Steganography.decode(output_image)  # Decoding the secret message
                secret_msg.append(secret_text)
        elif choice == '4':
            print 'Read the Secret Message \n'  # Chooses to read the Secret Message
            if secret_message:
                print 'Your Secret Message is: \n' + str(secret_text)  # if message sent, Printing the Secret Message
            else:
                print 'No Message Received \n'  # Else print no message received
        elif choice == '5':
            print 'You Chose to Read the Entire Chat History \n'  # Chooses to read the Entire Chat History
            if secret_msg:  # If a Secret Message is sent, means the user is having a chat with a friend
                print 'You Contacted ' + str(select_a_friend) + ' and you sent him ' + str(
                    secret_text)  # print the name of the user's friend and the secret
            else:
                print 'No Chat History \n'


