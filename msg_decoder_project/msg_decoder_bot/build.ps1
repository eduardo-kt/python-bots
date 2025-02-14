$exclude = @(".venv", ".env", "msg_decoder_bot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "msg_decoder_bot.zip" -Force