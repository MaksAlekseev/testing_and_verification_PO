$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
& (Join-Path $PSScriptRoot "build.ps1")

$jar = Join-Path $root "dist\office-booking.jar"
$input = Join-Path $root "build\jpackage-input"
$out = Join-Path $root "dist\exe"

if (-not (Get-Command jpackage -ErrorAction SilentlyContinue)) {
    throw "jpackage was not found. Install JDK 14+ to build an EXE launcher."
}

if (Test-Path $out) {
    Remove-Item -LiteralPath $out -Recurse -Force
}
if (Test-Path $input) {
    Remove-Item -LiteralPath $input -Recurse -Force
}
New-Item -ItemType Directory -Force $out, $input | Out-Null
Copy-Item -LiteralPath $jar -Destination $input -Force

jpackage `
    --type app-image `
    --name OfficeBooking `
    --input $input `
    --main-jar (Split-Path $jar -Leaf) `
    --main-class ru.mirea.officebooking.OfficeBookingApp `
    --dest $out

Write-Host "Built EXE app image in dist\exe\OfficeBooking"
