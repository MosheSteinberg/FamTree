call C:\Users\MS13\AppData\Local\Continuum\anaconda3\Scripts\activate.bat
set /p person="Choose a person: "
python familytreemaker.py -a %person% -oo yes Steinbergfamily.txt > DotCodeTemp.txt
call dot DotCodeTemp.txt -Tpng > FamilyTree.png
del "DotCodeTemp.txt"
FamilyTree.png