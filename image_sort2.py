import shutil, os
import PIL
from PIL import Image
#add main directory with mixed files needing to be sorted here replacing the file path ./batch with your folders file path
directory_main = './batch'
total_files = 0
active = True

for img in os.listdir(directory_main):
    total_files += 1


while active:
    print(f'There are: {total_files} left to sort.')
    if total_files == 0:
        print('You have completed the set, Well done! Thanks for your help :)')
        active = False
    else:
        start = input('Would you like to start sorting images?(Y/N): ')
        if start.lower() == 'y':
            print('Awesome lets get started:')
            print('To sort each image we will be using the following characters:\nd = Dog,\nc = Cat,\nb = Background,\n? = Not sure')
            print('Once you start an image will pop up and you will have the option to input one of those characters, doing so will move the image to the folder corresponding to that character as outlined above.')
            print("To start input 'y' otherwise write 'q' you can write 'q' at any time to quit and come back later.")
            second_start = input(': ')
            if second_start.lower() == 'y':
                while len(os.listdir(directory_main) ) != 0:
                    for img in os.listdir(directory_main):
                        print('An image should pop up...')
                        #add the correct file path here
                        square_picture = Image.open(f'./batch/{img}')
                        square_picture.show()
                        response = input('Enter your sort value: ')
                        square_picture.close()
                        if response.lower() == 'q':
                            print('Thanks for your help, see you again soon...')
                            active = False
                            break
                        elif response.lower() == 'd':
                            #add the file paths to the folders corresponding to the input values
                            shutil.move(f'./batch/{img}', './Dogs')
                            print('File moved into: Dogs folder')
                        elif response.lower() == 'c':
                            shutil.move(f'./batch/{img}', './Cats')
                            print('File moved into: Cats folder')
                        elif response.lower() == 'b':
                            shutil.move(f'./batch/{img}', './Background')
                            print('File moved into: Background folder')
                        elif response.lower() == '?':
                            shutil.move(f'./batch/{img}', './Not_sure')
                            print('File moved into: Not_sure folder')
                else:
                    print(f'There are: 0 images left to sort. You have completed the set! Thanks for your help :)')
                    print('\\\\      //\\\\      //   ////////   //        //              \\\\\\\\\\\\         ////       //\\       //   ////////')
                    print(' \\\\    //  \\\\    //    //         //        //              \\\\   \\\\      //   //     // \\\\     //    //      ')
                    print('  \\\\  //    \\\\  //     ////////   //        //              \\\\    \\\\    //    //    //   \\\\   //     ////////')
                    print('   \\\\//      \\\\//      //         //        //              \\\\    //    //   //    //     \\\\ //      //      ')
                    print('    \\/        \\/       ////////   ////////  ////////        \\\\/////      ////     //       \\\\/       ////////')
                    break
            elif second_start.lower() == 'q':
                print('Thanks for your help, see you again soon...')
                active = False
        elif start.lower() == 'n':
            print('Thanks for your help, see you again soon...')
            active = False

    

