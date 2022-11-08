import math;
#Import math module to use the math.gcd() command

def enkripsiPesan():
    #Function which handles the encryption process
    enkripsiMasukkan = '';
    menangkal = 0;

    pesanTeks = input("Silahkan Masukkan Plaintext Anda: \n");
    pesanTeks = pesanTeks.upper();
    #Takes input and changes to capital letters.
    
    print('Silakan masukkan kunci enkripsi pertama Anda, pastikan itu adalah koprime 26: ');
    kunci = '5';
    kunciPertama = int(pengesahan(kunci));
    #Get variable "a" from validateType function, which takes inputType as the argument.
    #Used inputType as triger in validateType if it needs to be coprime or not.
    #See rest at def validateType();
    
    print('Silakan Masukkan Kunci Enkripsi kedua Anda: ');
    kunci = '8';
    kunciKedua = int(pengesahan(kunci));
    #Same situation, but with inputType as b.
    
    panjang = len(pesanTeks);
    #Get length of the inputed text for use in for loop.
    
    for x in range(panjang):
        nomorPesanTeks = ord(pesanTeks[x]);
        #Change the character to the Unicode number of it.
        if nomorPesanTeks >= 65 and nomorPesanTeks <= 90:
            #From 65 to 90 are the capital letters. Those are put into the encryption algorythm.
            enkripsiNomor = ((nomorPesanTeks - 65) * kunciPertama + kunciKedua) % 26;
            enkripsiMasukkan += chr( enkripsiNomor + 65);
            #Adds the encrypted letter to the end of the encrypted text after getting turned back to character.
            menangkal += 1;
            #This is for testing in case of errors.
        elif nomorPesanTeks == 32:
            #32 is whitespace, it gets converted back to character and added to end of string.
            enkripsiMasukkan += chr(nomorPesanTeks);
            menangkal += 1;
        #Ignores all other characters not specified.
            
    return  enkripsiMasukkan;
    #Returns the encrypted text to main function


#Similar workflow of code to encryption.
def deskripsiPesan():
    pesanTeks = '';
    menangkal = 0;
    
    enkripsiMasukkan = input('Silakan masukkan enkripsi teks Anda: \n');
    enkripsiMasukkan= enkripsiMasukkan.upper();
    
    print('Silakan masukkan kunci enkripsi pertama yang Anda gunakan, pastikan itu masih koprime 26: ');
    kunci = 'kunciPertama';
    kunciPertama = int(pengesahan(kunci));

    print('Silakan masukkan kunci enkripsi kedua Anda: ');
    kunci = 'kunciKedua';
    kunciKedua = int(pengesahan(kunci));

    length = len(enkripsiMasukkan);

    totalInvers = int(prosesInvers(kunciPertama, 26));
    #Takes integer "a" and inputs it into inverse function with 26 as the other argument.

    for x in range(length):
        enkripsiNomor = ord(enkripsiMasukkan[x]);
        if enkripsiNomor >= 65 and enkripsiNomor <= 90:
            #Decryption algorythm.
            nomorPesanTeks = (((enkripsiNomor - 65) - kunciKedua) * totalInvers) % 26;
            pesanTeks += chr(nomorPesanTeks + 65);
            menangkal += 1;
        elif enkripsiNomor == 32:
            plainText += chr(enkripsiNomor);
            menangkal += 1;

    return  pesanTeks;


def pengesahan(kunci):
    kunciPertama = input('');
    #Takes input
    
    while kunciPertama.isdigit() == False:
        #.isdigit() checks if variable before it is digit or not, returns False if not, therefor triggers while loop.
        a = input('Itu bukan nomor yang valid. Silakan coba lagi: \n');
    
    if kunci == 'kunciPertama':
        #Checks the argument variable inputType. If it is "a", goes into validateCoprime with argument "kunciPertama".
        pengesahanKoprime(kunciPertama);
        
    return kunciPertama;
    #Once function runs out, returns "a" to functions.


def pengesahanKoprime(kunciPertama):
    kunci = 'kunciPertama';
    #Assign inputType again, it has gone out of scope.
    testA = math.gcd(int(kunciPertama), 26);
    #Uses math function, which finds the greatest common divisor. 
    
    while testA != 1:
        #If gcd was not 1, it goes back to number validation.
        print('Angka itu bukan coprime dari 26. Silakan coba lagi: ');
        pengesahan(kunci);
        break;
        #Once its run through, it breaks out of the loops.

def prosesInvers(kunciPertama, z):
    kopi1 = 1;
    kopi2 = kunciPertama;

    teh1 = 0;
    teh2 = z;

    while teh2 != 0:
        #Keeps looping until b2 (remainder) is 0.
        susu = kopi2 // teh2;
        teh1, teh2, kopi1, kopi2 = (kopi1 - susu * teh1), (kopi2 - susu * teh2), teh1, teh2;
        #All on one line, so it all gets changed at same time, to the old value, not the updated one yet.
    return kopi1 % z;
    #A could be negative so we take the remainder of it, which will be positive to return.

def kopi():
    pilih = '';
    
    while pilih != 'keluar dari program':
    #This while loop doesnt actually do anything, it would still loop forever so I simplified it.
    #while 1 != 2:
        #Infinite loop, only way to break out of is by inputting "Exit" (or CTRL + C).
        pilih = input('Silakan masukkan jika Anda ingin mengenkripsi atau mendekripsi teks. \npilih tindakan "enkripsi pesan", "deskripsi pesan" atau "keluar dari program": \n');
        if pilih == 'enkripsi pesan':
            print(enkripsiPesan());
            #Prints out the returned value from encryption function.
        elif pilih == 'deskripsi pesan':
            print(deskripsiPesan());
        elif pilih == 'keluar dari program':
            break;
            #Once input is "Exit", break out of the loop to the end of it.
        else:
            print('Anda telah memasukkan pilihan yang salah.');
            pilih = kopi();
            #If not one of the options is inputted, starts again from the start of the main function and asks again.
    return pilih;
    #This is used to not loop through extra times if the else gets triggered.

kopi();
#This can also be triggered manually in command line, but starts the main function, starting off the whole process.


#test = input("Here: ");
#Test if it prints out Exit at end. If it is run normally, it will not, only in shell.