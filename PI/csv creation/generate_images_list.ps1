$currentimages = import-csv "C:\vscode\Github-giamariebose-personal\personalprojects\personalprojects\PI\csv creation\Beginning_images.csv" | select-object -expandproperty link

$index = 0
foreach ($imagelink in $currentimages) {
    $line = "images[$index] = `"$imagelink`""
    $line | out-file -filepath "C:\vscode\Github-giamariebose-personal\personalprojects\personalprojects\PI\csv creation\newimagelist.txt" -append -encoding utf8
    $index++
}

#$output | set-content -path "C:\vscode\Github-giamariebose-personal\personalprojects\personalprojects\PI\csv creation\script_output.txt"