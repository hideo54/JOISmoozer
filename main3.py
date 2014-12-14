import os

#The following is the default settings.
#If you need, rewrite as you want.
language = 'Python' #<-Rewrite the language name you wanna use.
file_format = '~/Desktop/JOI{prb}.py'
input_format = '~/Downloads/2014-yo-t{prb}-in{num}.txt'
output_format = 'anser{prb}-{num}.txt'

#Main program
problem = input("What's the number of the problem you're solving now? :")
file = file_format.format(prb=problem)

#I prepared two language, C and Python.
#If you rewrote line 5, add command using 'elif'.
if language == 'C':
    command_format = 'gcc {f}; ./a.out'
elif language == 'Python':
    command_format = 'python {f}'
else:
    command_format = input('What command you wanna use? Input the command writing {f} as filename')

try:
    for number in range(5):
        number += 1
        command = command_format.format(f=file)
        inpt = input_format.format(prb=problem, num=number)
        output = output_format.format(prb=problem, num=number)
        print('{cmd} < {IN} > {out}'.format(cmd=command, f=file, IN=inpt, out=output))
        os.system('{cmd} < {IN} > {out}'.format(cmd=command, f=file, IN=inpt, out=output))
    print('Successfully done')
except:
    print('Error! Check your settings; line 5-9')