import datetime


def my_fun_write_recdata_tofile(mydata):
        mytodattime=datetime.datetime.now()
        myfilename=str(mytodattime.year)+str(mytodattime.month)+str(mytodattime.day)+'-'+str(mytodattime.hour)+'-'+str(mytodattime.minute)+'-'+str(mytodattime.second)
        myfilename=myfilename+".bat"
        print(myfilename)

        #mydata=bytes((0x01,0x2,0x03,0x4,0x05,0x06))
        #print(mydata)
        myls=''
        for ii in mydata:
            y=(mydata[ii]+mydata[ii+1]*256)/10
            myls=myls+str(y)+'\n'
            ii=ii+2
            if(ii>=len(mydata)):
                break
        #print(myls)
        myfile = open(myfilename, "wt")
        myfile.write(myls)
        myfile.close()


######################################
myrecdata= ((0x01,0x2,0x03,0x4,0x05,0x06))
my_fun_write_recdata_tofile(myrecdata)

