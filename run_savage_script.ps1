Write-Host "Starting SavageScript..." -ForegroundColor Cyan
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath
& "$scriptPath\venv\Scripts\Activate.ps1"
python "$scriptPath\src\savage_script.py"
Write-Host "Press any key to continue..." -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
