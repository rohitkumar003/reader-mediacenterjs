@echo off
git rev-parse --short head > info.txt
set /p commit=<info.txt
git rev-parse --abbrev-ref head > info.txt
set /p branch=<info.txt
del info.txt
set prefix=%branch%-%commit%
rmdir /S /Q reader-mediacenterjs.wiki
git clone https://github.com/rohitkumar003/reader-mediacenterjs.wiki.git
cd reader-mediacenterjs.wiki
echo checking if %prefix%.zip already exists.
jar -cMf .\%prefix%.zip ..\build\debug
Set filename=%prefix%.zip
For %%A in ("%filename%") do (
    Set Folder=%%~dpA
    Set Name=%%~nxA
)
find /c "%Name%" testpage.md && ( echo File %Name% exists. && pause && exit ) 
echo File %Name% does not exists.
@echo: >> testpage.md 
echo [%prefix%](%prefix%.zip)>>testpage.md
git status -s
git add %prefix%.zip
git add testpage.md
git commit -m "Uploading artifact"
git push
cd .