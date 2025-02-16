$exclude = @(".venv", ".env", "online_grocery_bot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "online_grocery_bot.zip" -Force