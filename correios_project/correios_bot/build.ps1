$exclude = @("venv", "correios_bot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "correios_bot.zip" -Force