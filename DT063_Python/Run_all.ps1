$ErrorActionPreference = "Stop"
$env:PYTHONIOENCODING = "utf-8"
Set-Location $PSScriptRoot
python --version
Write-Host "`n===== DEMO TAT CA 11 CA =====" -ForegroundColor Cyan
python demo.py --tat-ca
Write-Host "`n===== KHAO SAT n=5,20,100 =====" -ForegroundColor Cyan
python demo.py --khao-sat
Write-Host "`n===== BO KIEM THU 14 CA =====" -ForegroundColor Cyan
python tests/test_danh_sach_kep.py
Write-Host "`nEND_TO_END_OK: 11 demo, khao sat va bo kiem thu 14 ca da chay xong." -ForegroundColor Green
Write-Host "Mo web: python web/app.py  (http://127.0.0.1:8000)" -ForegroundColor Yellow
