$exclude = @("venv", "input_number_bot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "input_number_bot.zip" -Force