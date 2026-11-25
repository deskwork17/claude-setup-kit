# Registers the Obsidian Local REST API plugin as a user-scope MCP server for Claude Code.
# Run this yourself (not through Claude): it reads the plugin's API key, which Claude never sees.
#
#   powershell -ExecutionPolicy Bypass -File register_obsidian_mcp.ps1 -Vault "C:\Users\you\Documents\Wiki"
#
param(
    [Parameter(Mandatory = $true)][string]$Vault,
    [string]$Name = "obsidian",
    [int]$Port = 27123
)

$dataJson = Join-Path $Vault ".obsidian\plugins\obsidian-local-rest-api\data.json"
if (-not (Test-Path $dataJson)) {
    Write-Error "Not found: $dataJson`nInstall and enable the Local REST API plugin in this vault first, then rerun."
    exit 1
}

$key = (Get-Content $dataJson -Raw | ConvertFrom-Json).apiKey
if (-not $key) {
    Write-Error "No apiKey in the plugin's data.json. Open the plugin's settings once in Obsidian, then rerun."
    exit 1
}

if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
    Write-Error "The 'claude' command isn't on PATH. Install Claude Code or open a new terminal, then rerun."
    exit 1
}

# Replace any earlier registration with the same name.
claude mcp remove $Name --scope user *> $null

claude mcp add --transport http --scope user $Name "http://127.0.0.1:$Port/mcp/" --header "Authorization: Bearer $key"
if ($LASTEXITCODE -eq 0) {
    Write-Host "Registered '$Name' -> http://127.0.0.1:$Port/mcp/ (user scope). Restart Claude Code and check /mcp."
    Write-Host "Make sure 'Enable Non-encrypted (HTTP) Server' is on in the plugin settings, and Obsidian is open."
}
