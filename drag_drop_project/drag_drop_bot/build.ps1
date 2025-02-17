$exclude = @("venv", "drag_drop_bot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "drag_drop_bot.zip" -Force