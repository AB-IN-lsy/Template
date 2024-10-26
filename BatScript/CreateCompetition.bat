@echo off
setlocal enabledelayedexpansion

:: VSCode Task: CreateCompetition
:: Powered by AB-IN

:: Arguments:
:: %1: folderName
:: %2: typeName
:: %3: suffixName
:: %4: NumberOfQuestion

:: Set descriptive variable names
set "folderName=%~1"
set "typeName=%~2"
set "suffixName=%~3"
set "numberOfQuestions=%~4"

:: Check if the folder exists, if not, create it
IF NOT EXIST "%folderName%" (
    MD "%folderName%"
    ECHO %folderName% competition creation completed.
) ELSE (
    ECHO Warning: The %folderName% competition has already been created.
)

:: Navigate to the folder
CD "%folderName%"

:: Initialize counter
set /a cnt=0

:: Loop through the alphabet
for %%i in (a b c d e f g h i j k l m n o p q r s t u v w x y z) do (
    set /a cnt+=1
    
    :: Check if subfolder exists, if not, create it
    IF NOT EXIST "%%i" (
        MD "%%i"
    )
    
    CD "%%i"

    :: Check if file exists, if not, create it from template
    IF NOT EXIST "%%i.%suffixName%" (
        TYPE "%TemplatePath%\template%typeName%.%suffixName%" > "%%i.%suffixName%"
        ECHO The file "%%i.%suffixName%" creation completed.
    ) ELSE (
        ECHO Warning: The file "%%i.%suffixName%" already exists.
    )

    CD ..

    :: Exit the loop if the desired number of questions is reached
    IF !cnt! EQU %numberOfQuestions% EXIT
)

:: End of script
EXIT /B 0
