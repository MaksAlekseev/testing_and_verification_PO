$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
$src = Join-Path $root "src\main\java"
$build = Join-Path $root "build\classes"
$dist = Join-Path $root "dist"
$manifest = Join-Path $root "build\MANIFEST.MF"

New-Item -ItemType Directory -Force $build, $dist | Out-Null

$javaFiles = Get-ChildItem $src -Recurse -Filter *.java | ForEach-Object { $_.FullName }
if (-not $javaFiles) {
    throw "Java source files were not found."
}

javac -encoding UTF-8 -d $build $javaFiles

"Main-Class: ru.mirea.officebooking.OfficeBookingApp`r`n" | Set-Content -Encoding ASCII $manifest
jar cfm (Join-Path $dist "office-booking.jar") $manifest -C $build .

Write-Host "Built dist\office-booking.jar"

