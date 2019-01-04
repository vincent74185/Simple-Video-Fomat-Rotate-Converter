from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
import os

class RotateVideo:

    def metadataOff(self):
        self.FormatCombo.config(state='normal')

    def metadataOn(self):
        self.FormatCombo.set("Same As Original")
        self.FormatCombo.config(state='disabled')

    def InputFolderButtonClicked(self):
        self.InputFolder = filedialog.askdirectory()
        strFolder = str(self.InputFolder)
        self.InputFolderLabel.delete(0, 'end')
        self.InputFolderLabel.insert(0,strFolder)
        # print(folder)

    def InputFilesButtonClicked(self):
        self.InputFiles = filedialog.askopenfilenames()
        strFiles = str(self.InputFiles)
        self.InputFilesLabel.delete(0, 'end')
        self.InputFilesLabel.insert(0, strFiles)
        # print(files)
        # print(files[0])

    def OutputFolderButtonClicked(self):
        self.OutputFolder = filedialog.askdirectory()
        strFolder = str(self.OutputFolder)
        self.OutputFolderLabel.delete(0, 'end')
        self.OutputFolderLabel.insert(0, strFolder)

    def FolderOn(self):
        self.InputFolderButton.config(state=NORMAL)
        self.InputFolderLabel.config(state=NORMAL)
        self.InputFilesButton.config(state=DISABLED)
        self.InputFilesLabel.config(state=DISABLED)

    def FolderOff(self):
        self.InputFolderButton.config(state=DISABLED)
        self.InputFolderLabel.config(state=DISABLED)
        self.InputFilesButton.config(state=NORMAL)
        self.InputFilesLabel.config(state=NORMAL)

    def Convert(self):
        choice = self.RotateCombo.get()
        #print(choice)
        choice = int(choice)
        HardCodeDegree = choice
        if HardCodeDegree == 90:
            HardCodeDegree = 1
        elif HardCodeDegree == 180:
            HardCodeDegree = 3
        elif HardCodeDegree == 270:
            HardCodeDegree = 2

        SoftCodeDegree = choice
        if SoftCodeDegree == 90:
            SoftCodeDegree = -90
        elif SoftCodeDegree == 180:
            SoftCodeDegree = 180
        elif SoftCodeDegree == 270:
            SoftCodeDegree = 90

        #print(SoftCodeDegree)
        if self.v1.get() == True:
            #print("Folder input is selected")
            path = str(self.InputFolderLabel.get())
            if path.__len__() == 0:
                messagebox.showerror('Error', 'Please Select or Type a Path to the Folder')
            else:
                convertPath = str(self.OutputFolderLabel.get())
                if convertPath.__len__() == 0:
                    messagebox.showerror('Error', 'Please Select or Type a Path to the Folder')
                else:
                    messagebox.showinfo('Info', 'Converting')
                    dirs = os.listdir(path)
                    for name in dirs:
                        inputName = name
                        #print("The input name is %s",inputName)
                        temp = inputName.split('.')
                        filename = temp[0]
                        outputName = inputName
                        inputPath = path + '/' + inputName
                        outputPath = convertPath + '/' + outputName
                        command = None
                        if self.v2.get() == True:
                            ExtentionFormat = str(self.FormatCombo.get())
                            if ExtentionFormat != "Same As Original":
                                outputPath = convertPath + '/' + filename + ExtentionFormat
                            command = 'ffmpeg -y -i "{0}" -vf "transpose="{1}"" -qscale 0 -acodec copy "{2}"'.format(
                                inputPath, HardCodeDegree, outputPath)
                        else:
                            command = 'ffmpeg -y -i "{0}" -metadata:s:v rotate="{1}" -codec copy "{2}"'.format(
                                inputPath, SoftCodeDegree, outputPath)
                        try:
                            os.system(command)
                        except Exception as e:
                            #print('Command ', command, ' failed, error is: ', e)
                            messagebox.showerror('Error', e)
                    messagebox.showinfo('Info', 'Conversion is completed')
        else:
            # for inputPath in self.InputFilesLabel.get():
            #     print(inputPath)
            #print("\nThe input path is: ")
            #print(self.InputFilesLabel.get())
            #print(len(self.InputFilesLabel.get()))
            temp = self.InputFilesLabel.get()
            temp = temp[1:len(self.InputFilesLabel.get())-1]
            #print(temp)
            #print(len(temp))

            path = temp.split(',')
            #print(len(path))
            # path = path[0:len(path)-1]
            #print("\nThe converted path is: ")
            convertPath = str(self.OutputFolderLabel.get())
            #print(convertPath)
            if convertPath.__len__() == 0:
                messagebox.showerror('Error', 'Please Select or Type a Path to the Folder')
            else:
                messagebox.showinfo('Info', 'Converting')
                for inputPath in path:
                    actual = inputPath
                    if actual.__len__() == 0:
                        break
                    # if inputPath.__contains__('('):
                    #     actual = inputPath.replace('(',' ')
                    # if inputPath.__contains__(')'):
                    #     actual = inputPath.replace(')', ' ')
                    #print("\nThe actual path is: ")
                    actual = actual.replace("'",'')
                    actual = actual.lstrip()
                    #print(actual)
                    temp = actual.split('/')
                    #print(len(temp))
                    #print(temp[-1])
                    filename = temp[-1].split('.')[0]
                    extention = '.' + temp[-1].split('.')[1]
                    #print(filename,extention)
                    if self.v2.get() == True:
                        ExtentionFormat = str(self.FormatCombo.get())
                        if ExtentionFormat == "Same As Original":
                            outputPath = convertPath + '/' + filename + extention
                        else:
                            outputPath = convertPath + '/' + filename + ExtentionFormat
                            #print(outputPath)
                        command = 'ffmpeg -y -i "{0}" -vf "transpose="{1}"" -qscale 0 -acodec copy "{2}"'.format(
                            actual, HardCodeDegree, outputPath)
                    else:
                        outputPath = convertPath + '/' + filename + extention
                        command = 'ffmpeg -y -i "{0}" -metadata:s:v rotate="{1}" -codec copy "{2}"'.format(
                            actual, SoftCodeDegree, outputPath)
                    try:
                        os.system(command)
                    except Exception as e:
                        messagebox.showerror('Error', e)
                        messagebox.showinfo('Info', 'Conversion is completed')


    def __init__(self):
        #Form
        self.InputFiles = None
        self.InputFolder = None

        self.window = Tk()
        self.window.geometry('650x300')
        self.window.title("Rotate/Convert Format Video Helper")

        self.v1 = IntVar()
        self.v2 = IntVar()

        self.InputLabel = Label(self.window, width=12, text="Select Input")
        self.InputLabel.grid(column=0, row=0)
        self.InputFolderSelect = Radiobutton(self.window, text='Use Folder', value=True, variable=self.v1, command=self.FolderOn)
        self.InputFilesSelect = Radiobutton(self.window, text='Use Files', value=False, variable=self.v1, command=self.FolderOff)
        self.InputFolderSelect.grid(column=1, row=0)
        self.InputFilesSelect.grid(column=2, row=0)
        self.InputFolderLabel = Entry(self.window,width=50)
        self.InputFolderLabel.grid(column=2, row=1)
        self.InputFilesLabel = Entry(self.window,width=50)
        self.InputFilesLabel.grid(column=2, row=2)
        self.InputFolderButton = Button(self.window,width=15, text="Select Folder", command=self.InputFolderButtonClicked)
        self.InputFolderButton.grid(column=1, row=1)
        self.InputFilesButton = Button(self.window,width=15, text="Select Files", command=self.InputFilesButtonClicked)
        self.InputFilesButton.grid(column=1, row=2)
        self.InputFolderSelect.invoke()
        # Testing
        # self.InputFolderLabel.insert(0,"F:/Drive D/V/BJ/Input")
        # self.InputFilesSelect.invoke()
        # #Testing
        # self.InputFilesLabel.insert(0,"('F:/Drive D/V/BJ/Input/[4K][직캠 Fancam] 170825 걸크러쉬(Girl Crush) (보미) Fever @ 안지랑곱창 곱페스티벌.mp4',)")

        self.RotateLabel = Label(self.window, text="Rotate Clockwise")
        self.RotateLabel.grid(column=0, row=3)
        self.RotateCombo = Combobox(self.window,state='readonly')
        self.RotateCombo['values'] = (0, 90, 180, 270)
        self.RotateCombo.current(0)
        self.RotateCombo.grid(column=1, row=3)

        self.HardEncodeLabel = Label(self.window, text="Hard Encode Enable")
        self.HardEncodeLabel.grid(column=0, row=4)

        self.HardEncodeOn = Radiobutton(self.window, text='On', value=True, variable=self.v2, command =self.metadataOff)
        self.HardEncodeOff = Radiobutton(self.window, text='Off', value=False, variable=self.v2, command =self.metadataOn)
        self.HardEncodeOn.grid(column=1, row=4)
        self.HardEncodeOff.grid(column=2, row=4)

        self.FormatLabel = Label(self.window, text="Format")
        self.FormatLabel.grid(column=0, row=5)
        self.FormatCombo = Combobox(self.window)
        self.FormatCombo['values'] = ("Same As Original", "Type your own")
        self.FormatCombo.current(0)
        self.FormatCombo.grid(column=1, row=5)
        self.HardEncodeOff.invoke()

        self.OutputLabel = Label(self.window, width=12, text="Select Output")
        self.OutputLabel.grid(column=0, row=6)
        self.OutputFolderLabel = Entry(self.window, width=50)
        self.OutputFolderLabel.grid(column=2, row=6)
        self.OutputFolderButton = Button(self.window, width=15, text="Select Folder",
                                        command=self.OutputFolderButtonClicked)
        self.OutputFolderButton.grid(column=1, row=6)
        # Testing
        # self.OutputFolderLabel.insert(0,"F:/Drive D/V/BJ/Converted")

        self.StartLabel = Label(self.window, width=30, text="Start By Clicking the Start Button")
        self.StartLabel.grid(column=0, row=7)
        self.StartButton = Button(self.window,width=15, text="Start Converting", command=self.Convert)
        self.StartButton.grid(column=1, row=7)
        self.window.mainloop()

main = RotateVideo()