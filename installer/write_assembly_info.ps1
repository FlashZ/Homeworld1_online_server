param(
    [Parameter(Mandatory = $true)]
    [string]$Path,

    [Parameter(Mandatory = $true)]
    [string]$Title,

    [Parameter(Mandatory = $true)]
    [string]$Product,

    [Parameter(Mandatory = $true)]
    [string]$AssemblyVersion,

    [Parameter(Mandatory = $true)]
    [string]$FileVersion,

    [Parameter(Mandatory = $true)]
    [string]$InformationalVersion
)

$lines = @(
    'using System.Reflection;',
    "[assembly: AssemblyTitle(""$Title"")]",
    "[assembly: AssemblyProduct(""$Product"")]",
    "[assembly: AssemblyVersion(""$AssemblyVersion"")]",
    "[assembly: AssemblyFileVersion(""$FileVersion"")]",
    "[assembly: AssemblyInformationalVersion(""$InformationalVersion"")]"
)

Set-Content -LiteralPath $Path -Value $lines -Encoding Ascii
