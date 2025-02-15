$exclude = @("venv", "login_page_bot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "login_page_bot.zip" -Force